import benchmark_functions as bf
from MDP_algorithm import OriginalMDP
from plot_utils import plot_convergence

POP_SIZE = 1
NDIM = 50
MAX_ITER = 50000

func = bf.Schwefel(n_dimensions=NDIM)
lb, ub = func.suggested_bounds()

problem = {
    "obj_func": func._evaluate,
    "bounds": {"lb": lb, "ub": ub},
    "name": func._name
}

model = OriginalMDP(epoch=MAX_ITER, pop_size=POP_SIZE)
g_best = model.solve(problem)

# ── PROCESAMIENTO Y GRÁFICAS DELEGADOS ───────────────────────────────────
plot_convergence(
    fitness_list=model.history.list_global_best_fit,
    dist_start_list=model.history.dist_from_start,
    dist_base_list=model.history.dist_from_baseline,
    func_name=func._name,
    ndim=NDIM
)

# ── RESULTADOS FINALES ───────────────────────────────────────────────────
print(f"[{func._name}][dim_{NDIM}] Fitness final: {g_best.target.fitness}")
print(f" Best solution: {g_best.solution}")