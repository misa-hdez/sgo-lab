from opfunu.cec_based import cec2017
from MDP_algorithm import OriginalMDP
from plot_utils import plot_convergence

POP_SIZE = 1
NDIM = 100
MAX_ITER = 100000


func = cec2017.F282017(ndim=NDIM)

problem = {
    "obj_func": func.evaluate,
    "bounds": {"lb": func.lb, "ub": func.ub},
    "name": func.name
}

model = OriginalMDP(epoch=MAX_ITER, pop_size=POP_SIZE)
g_best = model.solve(problem)

# ── PROCESAMIENTO Y GRÁFICAS DELEGADOS ───────────────────────────────────
plot_convergence(
    fitness_list=model.history.list_global_best_fit,
    dist_start_list=model.history.dist_from_start,
    dist_base_list=model.history.dist_from_baseline,
    func_name=func.name,
    ndim=NDIM
)

# ── RESULTADOS FINALES ───────────────────────────────────────────────────
print(f"[{func.name}][dim_{NDIM}] Fitness final: {g_best.target.fitness}")
print(f" Best solution: {g_best.solution}")