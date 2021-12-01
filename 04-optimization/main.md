---
title:
- Optimization + Assignments 3, 4
subtitle: |
    | (Neural Networks Implementation and Application Tutorial)
author:
- Vilém Zouhar, Noon Pokaratsiri Goldstein
theme:
- Boadilla
date: 1st, 2nd December 2021
aspectratio: 169
header-includes:
  - \usepackage{graphicx}
  - \graphicspath{ {./img/} }
  - \newcommand{\think}{\includegraphics[width=0.4cm]{thinking_face.png}}
  - \newcommand{\monocle}{\includegraphics[width=0.4cm]{monocle_face.png}}
  - \newcommand{\upside}{\includegraphics[width=0.4cm]{upside_down_face.png}}
  - \newcommand{\tired}{\includegraphics[width=0.4cm]{tired_face.png}}
  - \newcommand{\starstruck}{\includegraphics[width=0.4cm]{starstruck_face.png}}
---

# Overview 

- Assignment 1
- Hessian and Jacobian
- Saddle Point
- Assignment 2

# Assignment 3

- Points for presentation \starstruck
- What was the hardest part?

# Hessian and Jacobian

## Functions
> - $\
  f_1: \mathbb{R} \rightarrow \mathbb{R} \qquad
  f_2: \mathbb{R}^{m} \rightarrow \mathbb{R} \qquad
  f_3: \mathbb{R} \rightarrow \mathbb{R}^{n} \qquad
  f_4: \mathbb{R}^{m} \rightarrow \mathbb{R}^{n}$
> - What are some model examples for these functions?

. . .

## Questions \think
> - What is the Jacobian? 
<!-- first derivatives wrt all outputs -->
> - What is the Hessian?
<!-- second derivatives -->
> - What are the matrix dimensions of Jacobian for $f_1, f_2, f_3, f_4$?
<!-- f1: 1x1, f2: mx1, f3: 1xn, f4: mxn -->
> - What are the matrix dimensions of Hessian for $f_1, f_2, f_3, f_4$?
<!-- f1: 1x1, f2, mxm, f3: undefined?, f4: undefined? -->

# Saddle Point

- What is the saddle point? Is it good?

\centering

![](img/surface_1.png){width=70%}

![](img/surface_2.png){width=70%}

# Assignment 4

Any questions?

# Resources

- [How can it be trapped in a saddle point?](https://stats.stackexchange.com/questions/278104/how-can-it-be-trapped-in-a-saddle-point)
