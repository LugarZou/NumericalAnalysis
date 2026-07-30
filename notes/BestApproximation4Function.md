当一个函数给定时，要求:

在一个**便于计算的简单函数类**中找一个函数与给定函数最接近。

这里有一个如何衡量函数之间的接近程度的问题。

逼近存在误差，常用的误差度量方法有：$n$-norm

$n$ best approximation: polynomial degree under $k$ s.t. minimize $n$-norm

# Orthogonal Polynomials

We define the **inner-product of polynomials on a discrete point set $\mathcal X$** as

$$
(f,g)=\sum_{i=0}^n w_if(x_i)g(x_i),
$$

where $w_i$ is the weight. And $x_i\in \mathcal X$.

continuous : change the weight to a function and then integrate

---

**Property**

1,

Orthogonal polynomials are linearly independent.

$\varphi_0,\varphi_1,\cdots,\varphi_n$ are linearly independent $\iff$ its Gramer determinant $|G_n|\ne 0$, where $G_n(i,j):=(\varphi_i,\varphi_j)$.

2,

$\varphi_n(x)$ 有n个不同的零点

3,

In the intervals produced by $a,b$ and all the zero-point of $\varphi_n(x)$, each interval has a zero-point of $\varphi_{n+1}(x)$.

## Constructing Orthogonal Polynomials

$$
\begin{aligned}
&P_0(x)=1,\\
\ \\
&P_1(x)=x-a_0,\\
\ \\
&P_{n+1}(x)=(x-a_n)P_{n}(x)-b_nP_{n-1}(x),n\geq 1,
\end{aligned}
$$

where

$$
a_k:=\frac{(xP_{k},P_{k})}{(P_{k},P_{k})},\quad b_k:=\frac{(P_{k},P_{k})}{(P_{k-1},P_{k-1})}.
$$

### Gramma-smidt

$$
P_0(x)=1,\\
\ \\
P_k(x)=x^k-\sum_{i=0}^{k-1}\frac{(x^k,P_i)}{(P_i,P_i)}P_i(x),\quad k\geq 1.
$$

---

**Example**

| Name      | Weight function    | Interval       |
| --------- | ------------------ | -------------- |
| Legendre  | $1$              | $[-1,1]$     |
| Chebyshev | $(1-x^2)^{-1/2}$ | $[-1,1]$     |
| Laguerre  | $e^{-x}$         | $[0,\infty)$ |
| Hermite   | $\exp(-x^2)$     | $\mathbb R$  |

# Approximation of continuous function

using polynomials.

Suppose you have a group of base.

Then you can figure out their coefficient by

$$
G_n\vec a=((f,\varphi_0),(f,\varphi_1),\cdots)^T
$$

Furthermore, 误差function $\delta(x):=f(x)-\varphi^*(x)$ 与基函数正交

And

$$
||\delta||_2^2=||f||_2^2-\sum_{i=0}^na_i(\varphi_i,f).
$$

You can scale $x\in[a,b]\to t=t\cdot(b-a)/2+(b+a)/2\in[-1,1]$ to simplify intervals thus utilise known orthogonal polynomials.
