# 误差的来源

- 模型误差：数学模型与实际问题之间的误差

- 观测误差：观察模型参数值产生的误差

- 方法误差：也称**截断误差，数值方法计算的误差**

- 舍入误差：计算过程中取**有限数字**引起的误差

在数值计算中将着重研究**截断误差、舍入误差**

# Error

设x是某实数的精确值， $\tilde x$是它的一个近似值，则称$e(x):=|x-\tilde x|$为近似值的绝对误差，或简称误差。若$x\neq 0$，称$e_r:=e(x)/|x|$为近似值的相对误差.

If

$$
e(x)\leq\varepsilon,
$$

then $\varepsilon$ is called a **limit of absolute error**. And if $x\neq0$,

$$
\varepsilon_r:=\varepsilon/|x|
$$

is called a **relative error limit**.

Since $x$ is unknown, we can use $e(x)/|\tilde x|$ to represent relative error and also relative error limit.

Apply Taylor we can know that

$$
e(f(\tilde x))\approx |f'(\tilde x)|e(\tilde x).
$$



# 有效数字

**Definition**

*Supposition*

Write a number in the form of

$$
\tilde x=0.d_1d_2\cdots d_k\times 10^m.
$$

*Condition*

$$
|x-\tilde x|\le 0.5*10^{m-n}.
$$

*Definition*

$n$ is called the number of significant digits of $\tilde x$.

---
**Property**

1,

If $\tilde x$ has $n$ significant digits, then

$$
|\tilde x-x|/|\tilde x|\le \frac 1{2d_1}*10^{-n+1}.
$$

2,

If
$$
|\tilde x-x|/|\tilde x|\le \frac 1{2d_1+2}*10^{-n+1},
$$

then $\tilde x$ has at least $n$ significant digits.
