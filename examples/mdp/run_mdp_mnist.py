import numpy as np
from tensorflow.keras.datasets import mnist
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

from MDP_algorithm import OriginalMDP
from plot_utils import plot_convergence

POP_SIZE = 1
MAX_ITERATIONS = 100000
N_OBJ = 5000
SEED = None
HIDDEN_LAYER_SIZES = (32,)
ARCH = [784, *HIDDEN_LAYER_SIZES, 10]

# Dataset
(X_train_raw, y_train_raw), (X_test_raw, y_test_raw) = mnist.load_data()

X_train_flat = X_train_raw.reshape(-1, 784).astype(np.float32)/255.0
X_test_flat  = X_test_raw.reshape(-1, 784).astype(np.float32)/255.0

X = np.vstack((X_train_flat, X_test_flat))
y = np.concatenate((y_train_raw, y_test_raw))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=SEED, stratify=y_train
)

idx = np.random.RandomState(SEED).choice(
    len(X_train), min(N_OBJ, len(X_train)), replace=False
)
X_obj, y_obj = X_train[idx], y_train[idx]

# Dimension and bounds
D  = sum(ARCH[i]*ARCH[i+1] + ARCH[i+1] for i in range(len(ARCH)-1))
LB = np.full(D, -1.0)
UB = np.full(D,  1.0)

# Neural network
def decode(w):
    layers, idx = [], 0
    for i in range(len(ARCH)-1):
        ni, no = ARCH[i], ARCH[i+1]
        W = w[idx:idx+ni*no].reshape(ni, no)
        b = w[idx+ni*no:idx+ni*no+no]
        layers.append((W, b))
        idx += ni*no + no
    return layers

def forward(X, layers):
    h = X
    for i, (W, b) in enumerate(layers):
        h = h @ W + b
        if i < len(layers)-1: h = np.maximum(0, h)
    e = np.exp(h - h.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)

def cross_entropy(w):
    p = forward(X_obj, decode(w))
    return -np.mean(np.log(p[np.arange(len(y_obj)), y_obj] + 1e-12))

def accuracy(w, X, y):
    pred = np.argmax(forward(X, decode(w)), axis=1)
    return np.mean(pred == y)

# Problem definition
problem = {
    "obj_func": cross_entropy,
    "bounds": {"lb": LB, "ub": UB},
    "name": "MNIST Neural Network Optimization"
}

model  = OriginalMDP(epoch=MAX_ITERATIONS, pop_size=POP_SIZE)
g_best = model.solve(problem)

# Adam optimization
clf = MLPClassifier(
    hidden_layer_sizes=HIDDEN_LAYER_SIZES, 
    solver='adam',
    max_iter=MAX_ITERATIONS, 
    random_state=SEED,
    # tol=1e-12,
    # n_iter_no_change=MAX_ITERATIONS
)

clf.fit(X_obj, y_obj)

w = g_best.solution

print(f"\n{problem['name']} (D={D:,})")
print("Objective: Cross-Entropy Loss")

print("\nMDP")
print(f"  Best Objective Value : {g_best.target.fitness:.4g}")
print(f"  Train Accuracy       : {accuracy(w, X_obj, y_obj)*100:.1f}%")
print(f"  Validation Accuracy  : {accuracy(w, X_val, y_val)*100:.1f}%")
print(f"  Test Accuracy        : {accuracy(w, X_test, y_test)*100:.1f}%")

print("\nAdam")
print(f"  Final Objective Value: {clf.loss_:.4g}")
print(f"  Train Accuracy       : {clf.score(X_obj, y_obj)*100:.1f}%")
print(f"  Validation Accuracy  : {clf.score(X_val, y_val)*100:.1f}%")
print(f"  Test Accuracy        : {clf.score(X_test, y_test)*100:.1f}%")

plot_convergence(
    fitness_list=model.history.list_global_best_fit,
    dist_start_list=model.history.dist_from_start,
    dist_base_list=model.history.dist_from_baseline,
    func_name=problem["name"],
    ndim=D,
    compare_curve=clf.loss_curve_,
    compare_label="Adam (Reference)",
    title1="MDP Convergence Curve on MNIST",
    ylabel1="Cross-Entropy Loss"
)