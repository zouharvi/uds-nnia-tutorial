---
title:
- Neural Networks Hello World + Assignments 2, 3
subtitle: |
    | (Neural Networks Implementation and Application Tutorial)
author:
- Vilém Zouhar, Noon Pokaratsiri Goldstein
theme:
- Boadilla
date: 24th, 25th November 2021
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

- Organization - Bonus points
- Assignment 2
- Gradient
- PyTorch's Autograd
- NN Hello World
- Assignment 3

# Organization - Bonus points

- 2 points for solution presentation
- 1-2 points for session contribution
- Max 2 points per session

# Assignment 2

- *Tutor cue:* go through the assignment
- Typesetting:
  - $test accuracy = 0.5$ or $\text{test accuracy} = 0.5$?
    - `$\text{test accuracy} = 0.5$`
  - The `*` symbol is used for convolution. Use `\cdot` instead.
    - $a * b$, $a\cdot b$
- Cheating
  - Discussion vs. blatant copying
- What were the biggest issues? Coding or theory?
- Do you feel they are too easy/hard?
- Do you feel they are unrelated to the lecture content?

# Optimization

::: columns
:::: column
## Gradient \think
> - What is it? 
> - How do we denote it?
>   - $\nabla f(p) = [\frac{\delta f}{\delta x_1}(p), \ldots, \frac{\delta f}{\delta x_k}(p)]$
> - Why is it important?
>   - Optimalization
::::

. . .

:::: column
![Function parameter landscape from [1]](img/landscape_3d.png){width=100%}
::::
:::

# Optimization


::: columns
:::: column
## Few questions \monocle
> - How does step/gradient-based optimization work?
> - How is the step size determined?
> - Why do we subtract the gradient and not add it?
> - If we start in different places will we always find the same spot?
> - Will we always find the global minimum?
::::

:::: column
![Function parameter landscape from [2]](img/landscape_2d.png){width=100%}
::::
:::

# Autograd & PyTorch

## How to get the gradient at $(x,y) = (2,3)$ of $x\cdot y + \sin(\pi \cdot x)$?
> - By hand \tired
> - Autograd \starstruck

. . .


::: columns
:::: {.column width=35%}
## By hand
\begin{align*}
& \frac{\delta}{\delta x} = y + \pi \cdot \cos(\pi \cdot x) \rightarrow 3 + \pi \\
& \frac{\delta}{\delta y} = x \rightarrow 2 \\
& \nabla f (2,3) \rightarrow (3+\pi, 2)
\end{align*}
::::

. . .

:::: {.column width=60%}
## Autograd
```
import torch
import numpy as np
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)
out = x*y + torch.sin(np.pi*x)
out.backward() # trigger gradient computation
assert np.isclose(x.grad, 3+np.pi)
assert np.isclose(y.grad, 2)
```
::::
:::

# Assignment 3

- Any questions?

# Resources

- [1] Optimization & landscapes [offconvex.org/2018/11/07/optimization-beyond-landscape/](http://www.offconvex.org/2018/11/07/optimization-beyond-landscape/)
- [2] Optimization Introduction by Scipy [scipy-lectures.org/advanced/mathematical_optimization/](https://scipy-lectures.org/advanced/mathematical_optimization/)