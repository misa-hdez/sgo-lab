# graficas_utils.py
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def convergence_plot(global_best_fit, rel_dist_init_curve, rel_dist_base_curve, best_fitness, func_name, conv_percentage, ndim):
    """
    Genera y muestra los gráficos de convergencia y tracking posicional.
    """
    fig = plt.figure(figsize=(10, 8), constrained_layout=True)
    spec = gridspec.GridSpec(2, 2, figure=fig, hspace=0.1)

    ax1 = fig.add_subplot(spec[0, :])
    ax2 = fig.add_subplot(spec[1, 0])
    ax3 = fig.add_subplot(spec[1, 1])
 
    
    fig.suptitle(f"{func_name} (D={ndim:,})", fontsize=14, fontweight='bold')

    exts = (".png", ".pdf")
    dpi_setting = 300


    # --- Gráfico 1: Global Best Fitness ---
    # ax1.plot(global_best_fit, color='blue')
    ax1.semilogy(conv_percentage, color='blue')
    # ax1.plot(conv_percentage, color='blue')
    ax1.set_title("Global Best Fitness")
    ax1.set_ylabel("Absolute error")
    ax1.grid(True)

    text_label = f"Best Fitness: {best_fitness}"
    ax1.text(
        0.7,
        0.25,
        text_label,
        transform=ax1.transAxes,
        ha="left",
        va="top",
        bbox=dict(boxstyle="round", fc="white", alpha=0.8)
    )

    # --- Gráfico 2: L1 Ratio desde el punto inicial ---
    ax2.plot(rel_dist_init_curve, color='green')
    ax2.set_title(r'$L_1$ Ratio Convergence from Initial Point')
    ax2.set_ylabel(r'$L_1$ Distance Ratio')
    ax2.grid(True)

    # --- Gráfico 3: L1 Ratio desde el punto base ---
    ax3.plot(rel_dist_base_curve, color='crimson')
    ax3.set_title(r'$L_1$ Ratio Convergence from Baseline Point')
    ax3.set_ylabel(r'$L_1$ Distance Ratio')
    ax3.grid(True)

    fig.supxlabel('Function Evaluations')

    # for ext in exts:
        # plt.savefig(
        # f"{full_path}{ext}",
        # dpi=dpi_setting if ext == ".png" else None,
        # bbox_inches='tight'
    # )
    plt.show() 
    plt.close(fig)
   