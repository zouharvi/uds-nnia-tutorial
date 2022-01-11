---
title:
- Convolutional Neural Networks + Assignment 7, 8
subtitle: |
    | (Neural Networks Implementation and Application Tutorial)
author:
- Vilém Zouhar, Noon Pokaratsiri Goldstein
theme:
- Boadilla
date: 12th, 13th January 2022
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

- Assignment 7
- Content
- Assignment 8

# Assignment 8

- What was the hardest part?

Emoji check \think \monocle \upside

# Questions

- What is convolution?
- What is a _kernel_?
- What is _stride_ and _padding_?
- What is _pooling_?

# AlexNet - How many parameters?


::: columns

:::: column
![AlexNet [1]](img/alexnet.png){width=300px}
::::

. . .

:::: column

layer | weights | biases |
- | - | -
conv1 | 96 $\cdot$ 11 $\cdot$ 11 $\cdot$ 3 | 96
conv2 | 256 $\cdot$ 5 $\cdot$ 5 $\cdot$ 96 | 256
conv3 | 384 $\cdot$ 3 $\cdot$ 3 $\cdot$ 256 | 384
conv4 | 256 $\cdot$ 3 $\cdot$ 3 $\cdot$ 384 | 256
fc1   | 6 $\cdot$ 6 $\cdot$ 256 $\cdot$ 4096 | 4096
fc2   | 4096 $\cdot$ 4096 | 4096
fc3   | 4096 $\cdot$ 1000 | 1000

\text{} \qquad In total 62378344

::::
:::

# Assignment 9

Any questions?

# Resources

- [1] AlexNet image [researchgate.net/figure/AlexNet-Structure-11-41_fig3_340644618](https://www.researchgate.net/figure/AlexNet-Structure-11-41_fig3_340644618)