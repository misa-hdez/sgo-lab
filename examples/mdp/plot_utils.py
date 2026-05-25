# graficas_utils.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plot_convergence(fitness_list, dist_start_list, dist_base_list, func_name, ndim):
    """
    Función principal a llamar desde tu script.
    Recibe las listas crudas del algoritmo, calcula los ratios y genera la gráfica.
    """
    # 1. Conversión a arrays de NumPy
    fitness_curve = np.array(fitness_list, dtype=float)
    rel_dist_init = np.array(dist_start_list, dtype=float)
    rel_dist_base = np.array(dist_base_list, dtype=float)

    # 2. Cálculo de ratios (Normalización)
    baseline_distance = rel_dist_base[0]
    rel_dist_init /= baseline_distance
    rel_dist_base /= baseline_distance

    # 3. Llamada interna a la función de graficado
    _draw_convergence_plot(
        fitness_curve=fitness_curve,
        rel_dist_init=rel_dist_init,
        rel_dist_base=rel_dist_base,
        func_name=func_name,
        ndim=ndim
    )


def _draw_convergence_plot(fitness_curve, rel_dist_init, rel_dist_base, func_name, ndim):
    """
    Lógica interna de Matplotlib para estructurar y mostrar la figura.
    """
    fig = plt.figure(figsize=(10, 8), constrained_layout=True)
    spec = gridspec.GridSpec(2, 2, figure=fig, hspace=0.1)

    ax1 = fig.add_subplot(spec[0, :])
    ax2 = fig.add_subplot(spec[1, 0])
    ax3 = fig.add_subplot(spec[1, 1])
 
    fig.suptitle(f"{func_name} (D={ndim:,})", fontsize=14, fontweight='bold')

    # --- Gráfico 1: Global Best Fitness ---
    # Usamos semilogy ya que en optimización las caídas son exponenciales.
    # Si la función tiene fitness negativo, cambia esto a ax1.plot()
    ax1.semilogy(fitness_curve, color='blue')
    ax1.set_title("Global Best Fitness")
    ax1.set_ylabel("Fitness Value")
    ax1.grid(True)

    # Extraemos el mejor fitness directamente de la curva (el último valor)
    best_fitness = fitness_curve[-1]
    text_label = f"Best Fitness: {best_fitness:.4e}"  # Formato científico para mayor legibilidad
    
    ax1.text(
        0.7, 0.25,
        text_label,
        transform=ax1.transAxes,
        ha="left", va="top",
        bbox=dict(boxstyle="round", fc="white", alpha=0.8)
    )

    # --- Gráfico 2: L1 Ratio desde el punto inicial ---
    ax2.plot(rel_dist_init, color='green')
    ax2.set_title(r'$L_1$ Ratio Convergence from Initial Point')
    ax2.set_ylabel(r'$L_1$ Distance Ratio')
    ax2.grid(True)

    # --- Gráfico 3: L1 Ratio desde el punto base ---
    ax3.plot(rel_dist_base, color='crimson')
    ax3.set_title(r'$L_1$ Ratio Convergence from Baseline Point')
    ax3.set_ylabel(r'$L_1$ Distance Ratio')
    ax3.grid(True)

    fig.supxlabel('Function Evaluations')

    plt.show() 
    plt.close(fig)