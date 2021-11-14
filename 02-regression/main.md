---
title:
- Regression + Assignment 1
subtitle: |
    | (Neural Networks Implementation and Application Tutorial)
author:
- Vilém Zouhar, Noon Pokaratsiri Goldstein
theme:
- Boadilla
date: 17th November 2021
aspectratio: 169
header-includes:
  - \usepackage{graphicx}
  - \graphicspath{ {./img/} }
  - \newcommand{\think}{\includegraphics[width=0.4cm]{thinking_face.png}}
  - \newcommand{\monocle}{\includegraphics[width=0.4cm]{monocle_face.png}}
---

# Overview 


- Assignment 1
- Regression
- Assignment 2

# Assignment 1

::: frame
##  Organization
- Late submissions (>10mins) will not be accepted unless previously agreed upon
- Other questions?
- How long did it take?
:::

- \emph{Tutor cue:} go through the assignment
- Questions?
- Did it work?
- Were you able to collaborate?

# Regression

- What is the difference between classification and regression? \monocle
- 

## Regression to Classification \think \think
Assume that we have a function that outputs a score for every class, e.g. \emph{Predict sentiment into (positive, negative, neutral)}:
$$
(15.0, -2.3, 4.1)
$$

> - How do we use this for classification? 
>   - Argmax
> - Can we get a probability distribution?
>   - Softmax: $\frac{\exp x_i}{\sum_k \exp x_k}$

# Assignment 2

- Any questions?

# Resources

TODO