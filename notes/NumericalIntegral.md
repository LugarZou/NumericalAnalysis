Sometimes there're no close-form solution or the calculation is too complex.

$$
I:=\int_a^bf\text dx.\\
\ \\
I_n[f]:=\sum_{i=0}^nA_if(x_i).\\
\ \\
R_n(f):=I-I_n[f].
$$

构造或确定一个求积公式，要讨论解决

1. 确定求积系数 $A_k$ 和求积节点 $x_k$ ($A_i$ should be only related to $x_i$ this it's general)
2. 求积公式的误差估计和收敛性

# Newton-Cotes Formula

**Definition**

代数精度

数值求积方法是近似方法，为要保证精度，我们自然希望求积公式能对“尽可能多”的函数准确地成立，这就提出了所谓代数精度的概念．由于闭区间 [a,b]上的连续函数可用多项式逼近，所以一个求积公式能对多大次数的多项式成为准确等式，是衡量该公式的精确程度的重要指标，为此给出以下定义。

如果某个求积公式对于 $1,x,x^2,\cdots,x^m$ 均能准确地成立，但对于 $x^{m+1}$ 就不一定准确，则称该求积公式具有m次代数精度。

According to this we can ascertain that the coefficient should satisfy

$$
R_n[f]=0,\forall n\in[1,m]\cap\Z.
$$

So if we ask for that to hold on $[a,b]$, we get

$$
\begin{pmatrix}
1 & 1 & \cdots & 1 \\
x_0 & x_1 & \cdots & x_n \\
x_0^2 & x_1^2 & \cdots & x_n^2 \\
\vdots & \vdots & \ddots & \vdots \\
x_0^m & x_1^m & \cdots & x_n^m \\
\end{pmatrix}
\begin{pmatrix}
A_0 \\
A_1 \\
A_2 \\
\vdots \\
A_n \\
\end{pmatrix}
=
\begin{pmatrix}
b - a \\
\frac{1}{2}(b^2 - a^2) \\
\vdots \\
\frac{1}{m+1}(b^{m+1} - a^{m+1}) \\
\end{pmatrix}
$$

这是关于 $A_k$ 的线性方程组，其系数矩阵是 **范德蒙矩阵**，当 $x_k (k = 0, 1, \cdots, n)$ 互异时非奇异，故 $A_k$ 有唯一解

and this gives us $m$ algebraic accuracy.

When the sampling points have same distance between each other, it's Newton-Cotes method.

After calculation we know that

$$
A_k=(b-a)C_k^{(n)},
$$

where

$$
C_k^{(n)}:=
\frac{(-1)^{n-k}}{n k! (n-k)!} \int_{0}^{n} \left( \prod_{\substack{i=0 \\ i \ne k}}^{n} (t - i) \right) \text dt, \quad k = 0, 1, \cdots, n
$$

柯特斯系数不但与被积函数无关，而且与积分区间也无关

当 n = 8 时，从表中可以看出出现了负系数，从而影响稳定性 ($A_k>0$) 和收敛性，因此实际计算并不用 n 较大的公式。将区间 [a,b] 分割成若干个小区间，对每个或几个小区间应用 n 较小的公式去计算

当阶数n为偶数时，牛顿-柯特斯公式的代数精度至少是 n+1 else it's $n$.

# Convergence

**Definition**

*Supposition*

$$
h:=\max\{x_{i+1}-x_i\}.
$$

*Condition*

$$
\lim_{n\to\infty,h\to0}R_n[f]=0.
$$

*Definition*

This integral method is **convergent**.

---

Due to Runge phenomenum, 节点数较多时Newton-Cotes 公式不收敛。因此当节点比较多时，采用分段计算。

If

$$
\lim_{h\to0}\frac{R_n[f]}{h^p}=C\neq 0
$$

Then we say this method is **$p$-order convergent**.

# Stable

If

$$
\forall\varepsilon>0,\exist\delta>0\left((f(x_k)-\tilde f_k\leq\delta)\to(|\sum_{k=0}^nA_k(f(x_k)-\tilde f_k)|\leq\varepsilon)\right).
$$

Then we say this formula is stable. Namely the error of initial data doesn't make the outcome error so much bigger.

Conclusion

If $\forall k(A_k>0)$, then this method is stable. Proof: let $\delta=\epsilon/(b-a)$.

# Interpolation Integral Formula

First we figure its interpolation polynomial

$$
f(x)\approx L_n(x):=\sum_{i=0}^nf(x_i)l_i(x).
$$

Then we integrate the equation and get

$$
\int_a^bf(x)\text dx\approx
\int_a^bL_n(x)\text dx=
\sum_{i=0}^n\left(\int_a^bl_i(x)\text dx\right)f(x_i)=:
\sum_{i=0}^nA_if(x_i).
$$

So

$$
A_i=\int_a^bl_i(x)\text dx.
$$

If an integral formula has form like $\sum A_if(x_i)$, it has $n$ algebraic accuracy $\iff$ it's interpolation integral formula.

# Gauss

If you can choose where $x_i$ are, you can get a more accurate formula.

With $x_k,A_k,k=0,1,\cdots n$, you can have $2n+1$ algebraic accuracy at most.

But get its Verdemond matrix like Newton-Cotes is not viable since it's non-linear and big, even solve it numerically would be expensive.

So Gauss says

1. We find $x_i$ first, in this case called Gauss points
2. Then we calculate $A_i$ like we did in Newton-Cotes

**定理5.5** 插值求积公式 $\int_{a}^{b} f(x) \rho(x) dx \approx \sum_{k=0}^{n} A_k f(x_k)$ 的节点 $a \le x_0 < x_1 < \cdots < x_n \le b$ 是高斯点的充**分必要条件** 是 以这些点为零点的多项式 $w_{n+1}(x) = (x - x_0) \cdots (x - x_n)$ 与任意次数不超过 $n$ 的多项式 $P(x)$ 带权 $\rho(x)$ 正交，即

$$
\int_{a}^{b} P(x) w_{n+1}(x) \rho(x) dx = 0 \tag{5.5.1}
$$

Thanks to this, we can first find $n+1$-deg orthogonal polynomial first then calculate its zero points as Gauss points.
