---
title:
- Introduction
subtitle: |
    | (Neural Networks Implementation and Application Tutorial)
author:
- Vilém Zouhar, Noon Pokaratsiri Goldstein
theme:
- Boadilla
date: 10th November 2021
aspectratio: 169
header-includes:
  - \AtBeginDocument{}
---

# Overview 

- Introduction
- Requirements, Materials, Assignments
- PCA, SVD
- Current assignment
- QA

# Hello

\centering

\large Who am I?

. . .

\LARGE Who are you?

![](img/thinking_face.png){width=25px}

# Introduction

## Choose and answer at least two questions:

- On scale from 1-10 how proficient are you in programming and mathematics?
- What topics of Neural Networks excite you the most?
- What topics of Neural Networks excite you the least?
- What programming languages do you know?
- How best can the tutorial sessions be helpful to your needs?

## Also the following:
- Who is your groupmate?
- Will you be attending Vilém's or Noon's tutorials?

<!--
from SNLP
# Topics

- Language properties, Zipf's Law, Basic statistical formalism
- Information theory (Shannon's game, Code Length, Compression), Entropy
- Language modelling, Backing-off models (interpolation, discounting, smoothing)
- Text classification, Algorithms (kNN, Decision Trees, SVM, \ldots)
- Word Sense Disambiguation, Algorithms (Dictionary based-, translation-, Collocation-based)
- Information retrieval, Latent Semantic Analysis, Singular Value Decomposition
- Machine Translation, Word alignment
- POS Tagging, Named Entity Recognition 
- - Sequence labeling (Hidden Markov models, Conditional Random Fields)
-->

# Requirements

::: frame
## Tutorial Requirements (exam admission)
- 60% of mandatory points (~10 assignments, 10 points each)
- Tutorial points only for exam admission (no final grade influence)
:::

\vspace{-0.1cm}

::: frame
## Tutorial Bonus Points
- ~2pts for extra exercises in the assignments
- 1pt for answering a question  in a tutorial
- ??pt for fixing errors in tutorial presentations
  - [github.com/zouharvi/uds-nnia-tutorial](https://github.com/zouharvi/uds-nnia-tutorial)
:::

\vspace{-0.5cm}

::: columns
:::: column
## Final Project
- None
::::

:::: column
## Transfer from last year
- Maybe possible (tbd)
- Assignments recommended (because of the exam)
::::
:::

# What's available

- Lectures by Prof. Klakow (recorded)
- Tutorials (not recorded, but allowed for private sharing)
- Corrected homework
- Consultations
  - Only in specific cases
  - By default **no** email and **no** personal chat
  - Ask questions during the lecture / tutorials
- Public forum (please use [Piazza](https://piazza.com/class/kvc3vzhsvh55rt))
  - Ask questions
  - Other students will also benefit from the answers
  - You can answer someone else's issue

<!--
# Cheating

. . .

\centering \footnotesize

no
-->

# Assignments

- Mandatory groups of 2
- Usually 2 exercises per assignment + a possible bonus question
- Jupyter notebook templates
  - Assignment + solution in the same notebook
  - Can use Google Colab or local runtime
  - Write solutions in Python files and import them
  - Submitted notebook must only contain your analysis and outputs
- Only one submission per group
  - Submit through Teams

# Dates / Times

- Lecture:
  - Tuesday 14:15-15:45
- Tutorials:
  - Vilém: Wednesday 16:00-18:00
  - Noon: Thursday 08:30-10:00
- Assignments
  - Released (usually) by Wednesday 08:00 (available in Teams)
  - Deadline (next) by Wednesday 08:00 (submit in Teams)
- Exam: TBD

# Tutorial Content

- Review of the topics covered in class
- Presentation of the past assignment
- Discussing the current assignment

# Organization

\centering

Questions?

# Assignment 0

- Questions?
- Did it work?
- How long did it take?

## Feedback:
- Change \textcolor{red}{TODO} to \textcolor{green}{Solution}.
- Don't forget to write amount of work.
  - Useful for our estimates of difficulty.

# Linear Algebra Basics

Few definitions (+how are they implemented in Python/Numpy/PyTorch)

- Scalars
- Vectors
- Matrices
- Tensors

. . .

Identify the following objects (Python lists):

- `[5.0, 3.0]`
- `5.0`
- `[True]`
- `[[5, 1], [0, 4]]`
- `[[True, False], [False, True]]`
- `[ [[0,1], [0,1], [0,1]], [[0,1], [0,1], [0,1]] ]`

# Linear Algebra Basics

::: frame
## A few operations and properties involving matrices:

- Transpose
- Inverse
- Dot product (i.e. matrix multiplication)
  - $C=AB, C_{i,j} = \sum_{k} A_{i,k}B_{k,j}$
:::

::: frame
## Common Properties:

- $A(B+C) = AB + AC$
- $A(BC) = (AB)C$
- $AB \neq BA$
- $(AB)^T = B^TA^T$
:::

# Linear Algebra Basics


## Definitions:

> - Eigenvector, Eigenvalue
>   - $Av = \lambda v, v\neq \overrightarrow{0}$
> - Eigendecomposition
>   - $A = Q \cdot L \cdot Q^{-1}$
> - Singular value decomposition (SVD)
>   - $A = U \Sigma V^T$
> - Principal Component Analysis:
>   - Eigendecomposition or SVD of covariance matrix $W=\frac{A^TA}{n-1}$
<!-- Possible with eigendecomposition becauset A^TA is symmetric rectangular -->
>   - Assume ordering of \{eigen,singular\}values from highest to lowest
>   - Project to $k$ dimensions: $A_k = A Q_k$

## True or False? ![](img/thinking_face.png){width=15px}
- Every real matrix has an eigenvalue decomposition (in $\mathbb{R}$).
<!-- No, non-square matricies don't. -->
- Every real matrix has a singular value decomposition (in $\mathbb{R}$).
<!-- Yes. -->
- Every real symmetric matrix has an eigenvalue decomposition (in $\mathbb{R}$).
<!-- Yes. -->

# Linear Algebra Basics - True or False? ![](img/monocle_face.png){width=15px}

\qquad $A = \begin{pmatrix} 4 & 2 \\ 2 & 4 \end{pmatrix}$

1. Is $v_1 = (1, -1)$ an eigenvector of $A$?
2. Is $v_2 = (2, 1)$ an eigenvector of $A$?
3. Is $v_3 = (2, 2)$ an eigenvector of $A$?

# PCA

::: {}

\centering
![](img/weight_height.png){width=40%}

:::

## Questions ![](img/monocle_face.png){width=15px}
> - What will be the first principal component?
> - Does anyone know how PCA works?
> - What does it mean that we take only $k$ largest principal components?

<!-- 
```
1.   standardize data = raw data - mean / standard deviation of data
2.   M = covariant_matrix(standardize data)
3.   eigenvalues, eigenvectors = eig(M)
4.   feature_vector = select_n_highest_components(eigenvectors)
5.   projected data = standardized_data dot feature_vector
```
-->

# PCA

- Is it safe to say that the first component will always contain the most important information? ![](img/thinking_face.png){width=15px}

. . .

::: columns
:::: column
![](img/pca_1.png)
::::

:::: column
![](img/pca_7.png)
::::
:::

# Standardization

- Is not normalization! ($x' = \frac{x}{|x|}$)
- $X = \frac{X - \text{mean}(X)}{\text{std}(X)}$
- Compute either:
  - With Numpy: `X = (X-X.mean())/np.std(X)`
  - With Scikit: `StandardScaler().fit_transform(X)`

- Why do we need standardization for PCA? ![](img/thinking_face.png){width=15px}

# Assignment 1

- Any questions?

# Typesetting Tips

- Do **not** write $A*B$, use `\cdot` or `\times`: $A\cdot B, A \times B$.
- Use LaTeX functions when available, e.g. `\log, \sin`: $\log(x), \sin(x)$, **not** $log(x), sin(x)$.
- Do **not** write plain text in math mode, use `$\text{ComputeEigenvalues}(X)$`

# Resources

1. Course Website: [lsv.uni-saarland.de/neural-networks-implementation-and-application-winter-2021-2022-2](https://www.lsv.uni-saarland.de/neural-networks-implementation-and-application-winter-2021-2022-2/)
2. Piazza: <https://piazza.com/class/kvc3vzhsvh55rt> 
3. Tutorial repository [github.com/zouharvi/uds-nnia-tutorial](https://github.com/zouharvi/uds-nnia-tutorial)
4. Lecture & tutorial teams channels
