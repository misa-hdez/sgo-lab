import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plot_convergence(
    fitness_list,
    dist_start_list,
    dist_base_list,
    func_name,
    ndim,
    compare_curve=None, 
    compare_label="Reference Model",
    title1="Global Best Fitness",
    ylabel1="Fitness Value"
):
    fitness_curve = np.array(fitness_list, dtype=float)
    rel_dist_init = np.array(dist_start_list, dtype=float)
    rel_dist_base = np.array(dist_base_list, dtype=float)

    # Cálculo de ratios
    baseline_distance = rel_dist_base[0]
    rel_dist_init /= baseline_distance
    rel_dist_base /= baseline_distance

    _draw_convergence_plot(
        fitness_curve=fitness_curve,
        rel_dist_init=rel_dist_init,
        rel_dist_base=rel_dist_base,
        func_name=func_name,
        ndim=ndim,
        compare_curve=compare_curve,
        compare_label=compare_label,
        title1=title1,
        ylabel1=ylabel1
    )

def _draw_convergence_plot(
    fitness_curve, rel_dist_init, rel_dist_base, func_name, ndim,
    compare_curve, compare_label, title1, ylabel1
):
    
    fig = plt.figure(figsize=(10, 8), constrained_layout=True)
    spec = gridspec.GridSpec(2, 2, figure=fig, hspace=0.1)

    ax1 = fig.add_subplot(spec[0, :])
    ax2 = fig.add_subplot(spec[1, 0])
    ax3 = fig.add_subplot(spec[1, 1])
 
    fig.suptitle(f"{func_name} (D={ndim:,})", fontsize=14, fontweight='bold')
    ax1.semilogy(fitness_curve, color='blue', label='MDP')
    
    if compare_curve is not None:
        final_adam_loss = compare_curve[-1] 
        ax1.axhline(y=final_adam_loss, color='darkorange', linestyle='--', linewidth=1.5,
                    label=f"{compare_label}")
        ax1.legend(loc="upper right")

    ax1.set_title(title1)
    ax1.set_ylabel(ylabel1)
    ax1.grid(True)

    best_fitness = fitness_curve[-1]
    text_label = f"Best Fitness: {best_fitness:.4e}"
    ax1.text(0.7, 0.25, text_label, transform=ax1.transAxes, ha="left", va="top",
             bbox=dict(boxstyle="round", fc="white", alpha=0.8))

    ax2.plot(rel_dist_init, color='green')
    ax2.set_title(r'$L_1$ Ratio Convergence from Initial Point')
    ax2.set_ylabel(r'$L_1$ Distance Ratio')
    ax2.grid(True)
    plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')

    ax3.plot(rel_dist_base, color='crimson')
    ax3.set_title(r'$L_1$ Ratio Convergence from Baseline Point')
    ax3.set_ylabel(r'$L_1$ Distance Ratio')
    ax3.grid(True)
    plt.setp(ax3.get_xticklabels(), rotation=30, ha='right')

    fig.supxlabel('Function Evaluations')

    plt.show() 
    plt.close(fig)