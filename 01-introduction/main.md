---
title:
- Introduction
subtitle: |
    | (Neural Networks Implementation and Application Tutorial)
author:
- Vilém Zouhar, Noon Pokaratsiri Goldstein
theme:
- Boadilla
date: 28th November 2021
aspectratio: 169
header-includes:
  - \AtBeginDocument{}
---

# Overview 

- Introduction
- Requirements
- Materials
- Assignments
- TODO (lecture content)
- Current assignment
- QA

# Hello

\centering

\large Who am I?

. . .

\LARGE Who are you?

![](img/thinking_face.png){width=25px}

# Introduction

Choose and answer at least two questions:

- On scale from 1-10 how proficient are you in programming and mathematics?
- What topics of Neural Networks excite you the most?
- What topics of Neural Networks excite you the least?
- What programming languages do you know?
- How best can the tutotial sessions be helpful to your needs?

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
- TODO pt for fixing errors in tutorial presentations
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
- Possible
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
- Public forum (please use Piazza) (link TODO)
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

- Lecture: Tuesdays 14:15-15:45
- Tutorials:
  - Vilém: Wednesday 16:00-18:00
  - Noon: Thursday 08:30-10:00
- Assignments
  - Released (usually) by Wednesday 08:30 (available in Teams)
  - Deadline (next) by Wednesday 08:30 (submit in Teams)
- Exam: TBD

# Tutorial Content

- Review of the topics covered in class
- Presentation of the past assignment
- Discussing doubts in current assignment

# Current Homework

- Assignment 1
- Previous assignment to review:
	- Assignment 0

# Linear Algebra Basics

Let's go over the definitions and some examples of these terms:

- Scalars
- Vectors
- Matrices
- Tensors

# Linear Algebra Basics

::: frame
## Some operations and properties involving matrices:

- transpose
- inverse
- dot product (i.e. matrix multiplication)
:::

# Linear Algebra  Basics

\centering
Review: matrix multiplication or dot production

$C = AB$

$C_{i,j} = \sum_{k} A_{i,k}B_{k,j}$

# Linear Algebra Basics

::: frame
## Common Properties:


- $A(B+C) = AB + AC$
- $A(BC) = (AB)C$
- $AB \neq BA$
- $(AB)^T = B^TA^T$
:::

# Linear Algebra Basics

::: frame
## True or False?
- Every real matrix has an eigenvalue decomposition.
- Every real matrix has a singular value decomposition.
- Any real symmetric matrix has an eigenvalue decomposition.
:::

TODO: examples/definitions for the following 

Definitions:

- eigenvector
- eigenvalue
- eigendecomposition
- singular value decomposition (SVD)


# Numpy Basics

TODO (Examples in Jupyter Notebook?)

# Resources

1. Course Website: [lsv.uni-saarland.de/neural-networks-implementation-and-application-winter-2021-2022-2](https://www.lsv.uni-saarland.de/neural-networks-implementation-and-application-winter-2021-2022-2/)
2. Piazza: <https://piazza.com/class/kvc3vzhsvh55rt> 
3. Tutorial repository [github.com/zouharvi/uds-nnia-tutorial](https://github.com/zouharvi/uds-nnia-tutorial)
4. Lecture & tutorial teams channels
