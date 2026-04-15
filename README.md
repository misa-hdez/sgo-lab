SGOLab
=========================

SGOLab is a research initiative under the program *Towards Scalable Geometric Optimization*, exploring a geometric reinterpretation of *black-box* optimization.

The project's central hypothesis states that the optimization process can be approached from an alternative space with reduced dependence on the codomain, introducing a conceptual separation between the domain and the objective function.

Under this approach, instead of explicitly modeling the function, SGOLab leverages the geometry of the bounded domain by constructing a relative reference system that dynamically guides the search process

## Motivation

> *"Give me a lever and a place to stand and I will move the earth"*
>
> Archimedes

In general terms, the No Free Lunch (NFL) Theorem states that no optimization algorithm is universally superior to others and that, in the absence of assumptions regarding the problem's structure, all algorithms exhibit the same average performance. The apparent superiority of a method emerges only when it successfully exploits specific regularities within the objective function's structure.

In the context of *black-box* optimization, such regularities are not accessible a priori and must be inferred from evaluated points. This process becomes prohibitively expensive in high-dimensional scenarios or when each evaluation involves significant computational cost, severely limiting the efficiency of traditional approaches.

Under these conditions, a fundamental question arises:

> Is it possible to guide the search process efficiently without explicitly reconstructing the function's landscape?

Throughout history, in both mathematics and physics, complex problems have been addressed by representing them in alternative spaces where certain structures become more accessible—as seen with Fourier and Laplace transforms.

While most current approaches focus on learning or approximating codomain information to model functional behavior, SGOLab starts from a different premise: the domain is not an inert space, but a potential source of structure. In this context, the research does not focus on landscape reconstruction, but on smart navigation of the space through geometric reference systems induced by the relationships between samples.

## Preview

Text

## Dependencies

Text

## Availability

Text

## TODO

Text

