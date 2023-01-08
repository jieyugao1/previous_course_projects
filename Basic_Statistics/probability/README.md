# Basic Probability

## Conditional Probability

**Bayes Rule**

```math
    P(A|B) = \frac{P(B|A)P(A)}{P(B)}
```
If P(A|B)= P(A), then A and B are independent. 

If A and B are conditional independent given C:
```math
    P(A \cap B | C) = P(A|C)P(B|C)
```
## Law of Total Probability

```math
    P(A) = P(A|B_{1})P(B_{1}) + ... + P(A|B_{n})P(B_{n})
```
## Random Variables

A random variable is a quantity with an associated probabilty distribution. It can be either discrete or continuous. The probability distribution associated with a discrete random variable is a probabilty mass function (PMF), and that associated with a contunious randome variable is a proabiblity density function (PDF).

**Discrete**:

```math
    \sum_{x\in X} f_{X}(x) = 1
```

**Continuous**:

```math
    \int_{-\infty}^{\infty}f_{X}(x)dx = 1
```

```math
    f_{X}(x) = \int_{-\infty}^{\infty} f_{Y}(y)f_{X|Y}(x|y)dy
```

## Markov Chains

A Markov chain is a process in which there is a finite set of states, and the probability of being in a particular state is only dependent on the previous state. The Markov property is such that, given the current state, the past and future states it will occupy are conditionally independent. 

```math
    P = \begin{pmatrix}
p_{11} & ... & p_{1n}\\
... & ... & ...\\
p_{m1} & ... & p_{mn}
\end{pmatrix}
```
