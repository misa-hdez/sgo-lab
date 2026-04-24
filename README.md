SGOLab
=========================

![Research-In-Progress](https://img.shields.io/badge/Status-Research--In--Progress-orange)
![License](https://img.shields.io/badge/License-MIT-green.svg)

*If you wish, you can consult the original Spanish version of this document:* [Spanish version](README_es.md)

SGOLab is a personal research project within the program *Towards Scalable Geometric Optimization*, exploring a geometric reinterpretation of *black-box* optimization.

The project's central hypothesis is that the optimization process can be approached from an alternative space with less reliance on the codomain, by introducing a conceptual separation between the domain and the objective function.

Under this framework, instead of explicitly modeling the function, SGOLab leverages the geometry of the bounded domain by constructing a relative reference system that dynamically guides the search process

## Motivation

Broadly speaking, the No Free Lunch (NFL) Theorem states that no optimization algorithm is universally superior to others and that, in the absence of assumptions about the structure of the problem, all algorithms exhibit the same average performance. The apparent superiority of a method emerges only when it successfully exploits specific regularities in the objective function.

In the context of *black-box* optimization, such regularities are not accessible a priori and must be inferred from sampled evaluations. This quickly becomes prohibitively expensive in high-dimensional scenarios or when each evaluation involves significant computational cost, severely limiting the efficiency of traditional approaches.

Under these conditions, a fundamental question arises:

> Is it possible to efficiently guide the search process without explicitly reconstructing the function landscape?

Throughout history, in both mathematics and physics, complex problems have been addressed by representing them in alternative spaces where certain structures become more accessible, as seen with Fourier and Laplace transforms.

While most current approaches focus on learning or approximating codomain information to model functional behavior, SGOLab starts from a different premise: *the domain is not an inert space, but a potential source of structure.* In this context, the research does not focus on reconstructing the function landscape, but on intelligently navigating the space through geometric reference systems induced by relationships between samples.

## Research Progress

> *"Give me a lever and a place to stand and I will move the earth"* — Archimedes

The SGOLab reference system is designed to enable navigation in *black-box* environments through a scale-independent internal metric. Its construction is based on anchoring reference points and defining a base unit of distance, enabling:

- Delimitation of search regions
- Structured displacements
- Monitoring progress through relative measures

This approach does not aim to solve the original problem directly, but rather to translate it into an environment where analysis becomes analytically tractable and allows the use of more powerful mathematical tools.

### Experimental Validation (Preliminary)

The following results illustrate the behavior of a single-solution algorithm operating in a purely exploratory setting. They suggest that navigation based on domain geometry can enable stable convergence even without explicitly reconstructing the function landscape.

#### Scalability with Fixed Evaluation Budget

Convergence curves are presented for the Hypersphere and Schwefel functions under a strict budget of 50,000 evaluations. The analysis focuses on the percentage of improvement obtained through dimensional sweeps. The main interest lies in the stability of the convergence pattern, which remains consistent as the problem scale increases.

- **Unimodal function: Hypersphere**

<p align="left">
  <img src="results/preliminary-results/benchmark-functions/hypersphere/scalability-hypersphere.png" width="70%" style="height:auto;" alt="Scalability Hypersphere"/>
</p>

- **Multimodal function: Schwefel**

<p align="left">
  <img src="results/preliminary-results/benchmark-functions/schwefel/scalability-schwefel.png" width="70%" style="height:auto;" alt="Scalability Schwefel"/>
</p>

### Extreme Dimensions

Performance is evaluated in *Large Scale Global Optimization* (LSGO) scenarios using the Hypersphere and Ackley functions in 100,000 dimensions. With a budget of 1,000,000 evaluations, the absolute error relative to the known optimum is reported.

Experiments at this scale help validate the robustness of the model in extreme-complexity scenarios, which remain largely undocumented in current technical literature. Relative progress measures are also introduced visually, with technical details provided in later sections.

- **Ackley function (100,000 dimensions)**

<p align="left">
  <img src="results/preliminary-results/benchmark-functions/ackley/dim_100000/Convergence_Ackley_D100000_run1.png" width="70%" style="height:auto;" alt="Ackley D100000"/>
</p>

- **Hypersphere function (100,000 dimensions)**

<p align="left">
  <img src="results/preliminary-results/benchmark-functions/hypersphere/dim_100000/Convergence_Hypersphere_D100000_run1.png" width="70%" style="height:auto;" alt="Hypersphere D100000"/>
</p>

- **Hypersphere function (1,000,000 dimensions)**

<p align="left">
  <img src="results/preliminary-results/benchmark-functions/hypersphere/dim_1000000/Convergence_Hypersphere_D1000000_run1.png" width="70%" style="height:auto;" alt="Hypersphere D1000000"/>
</p>

*Additional experiments can be found here:* [Benchmark Functions](results/preliminary-results/benchmark-functions).

### Importance of Relative Progress Measures

This section introduces navigation metrics based on relative distances ($L_1$ Ratio) calculated from reference points to the best solution found. When analyzing hybrid functions from the CEC 2017 suite (F18 and F19), a fundamental contrast emerges: while absolute error curves suggest premature stagnation, relative measures reveal intense activity and high variability throughout the process.

Unlike the smoother transitions observed in extreme-dimensional scenarios, oscillation here is persistent. This phenomenon reinforces the purely exploratory nature of the current prototype. The exploitation phase, currently under development, aims to reduce this variability and stabilize convergence in highly complex landscapes.

- **Hybrid Function 9**

<p align="left">
  <img src="results/preliminary-results/opfunu/cec2017/F18-Hybrid-Function-9/dim_100/convergence_analysis.png" width="70%" style="height:auto;" alt="F18 convergence"/>
</p>

- **Hybrid Function 10**
<p align="left">
  <img src="results/preliminary-results/opfunu/cec2017/F19-Hybrid-Function-10/dim_100/convergence_analysis.png" width="70%" style="height:auto;" alt="F19 convergence"/>
</p>

*Additional results using the CEC 2017 benchmark suite can be found here:* [CEC 2017 - Opfunu](results/preliminary-results/opfunu/cec2017).

## Dependencies

Development, testing, and experimental execution rely on the following libraries and tools:

- [**Mealpy**](https://github.com/thieu1995/mealpy)
- [**Opfunu**](https://github.com/thieu1995/opfunu)
- [**Benchmark Functions - A Python Library**](https://gitlab.com/luca.baronti/python_benchmark_functions)

## Availability

Since the mathematical model is currently undergoing formal documentation for publication in whitepapers and academic journals, access to the source code is temporarily restricted.

If you are a researcher, interested in learning more about this work, or open to technical collaboration, feel free to reach out via email:

- **Contact:** [misa.hdez97@proton.me](mailto:misa.hdez97@proton.me)

## Roadmap

Coming soon...

