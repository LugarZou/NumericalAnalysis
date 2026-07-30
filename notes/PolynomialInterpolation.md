Given $(x_i,y_i),i=0,1,\cdots,n$, we want to find a polynomial $P(x)$ of degree $n$ such that $P(x_i)=y_i$, $i=0,1,\cdots,n$.

Vandermonde matrix: such polynomial uniquely exists.

lagrange polynomial: how to construct

lagrange residue

$$
R_n(x):=\frac{f^{(n)}(\xi)}{(n+1)!}\prod(x-x_i)
$$

Note this is precise for all polynomial with degree less than or equal to $n$.

consider $f(x)=x^i$, we get

$$
\sum_{k=0}^nx_k^il_k(x)=x^i.
$$

Lagrange插值的两个问题：
（1）重新计算、计算量大
（2）截断误差难以估计

n越大，端点附近抖动越厉害，称为龙格（Runge）现象

函数的高阶导数未知，如何估计截断误差？

# Newton Polynomial

> For any given finite set of data points, there is only one polynomial of least possible degree that passes through all of them. Thus, it is appropriate to speak of the "Newton form", or "Lagrange form", etc., of the interpolation polynomial. However, different methods of computing this polynomial can have differing computational efficiency.
>
> Wikipedia

With base function $n_0:\equiv1,n_1:=(x-x_0),n_2:=(x-x_0)(x-x_1),\cdots$.

We define **divided difference** $f[x_0,x_1]$ as $\frac{f(x_1)-f(x_0)}{x_1-x_0}$.

Then $f[x_0,x_1,x_2]:=\frac{f[x_2,x_1]-f[x_1,x_0]}{x_2-x_0}$.

Actually you just need to assure that the term in the denominator is the one left out in the numerator.

According to the definition you can verify that the coefficient of $n_i(x)$ is $f[x_0,x_1,\cdots,x_i]$.

You can use a table to calculate the divided difference.

| $x_0$ | $f(x_0)$ |                |                    |
| ------- | ---------- | -------------- | ------------------ |
| $x_1$ | $f(x_1)$ | $f[x_0,x_1]$ |                    |
| $x_2$ | $f(x_2)$ | $f[x_1,x_2]$ | $f[x_0,x_1,x_2]$ |

where a term is determined by (left - left up)/(max index in left - min index in left up).

If $f^{(n)}\exist,f[x_0,x_1\cdots,x_n]=\frac{f^{(n)}(\xi)}{n!}$

According to this we can know the Newton form of remainder is

$$
R(x)=f[x,x_0,\cdots,x_t]n_{t+1}(x).
$$

当插值多项式从n-1次增加到n次时，Lagrange插值多项式必须重新计算所有的基本的插值多项式，而对于牛顿插值只需用表格再计算一个n阶均差，然后加上一项即可

No exam requirement

在等距插值的情况下，差分与均差有以下的关系

$$
f[x,x_0,\cdots,x_t]=\frac{\Delta^kf_0}{k!h^k},
$$

where $h$ is the step length of 差分.

牛顿后前插值公式适合于计算函数表表尾处附近的函数值。

# Hermite Polynomial

插值多项式要求在插值节点上函数值相等，有的实际问题还要求在节点上导数值相等，甚至高阶导数值也相等，满足这种条件的插值多项式称为埃米尔特（Hermite）插值多项式

We can use a similar method as in Newton Polynomial, except for we define

$$
f[x_i,x_i,\cdots,x_i(n+1\text{ in total})]:=f^{(n)}(x_i)/n!.
$$

If a point is given $k$ derivatives in total, you copy $k$ of it in the points.

Say you have $f(x_1),f'(x_1),f(x_2),f'(x_2),f''(x_2)$

then you use $x_1,x_1,x_2,x_2,x_2$ to calcualte Newton Polynomial.

And error is the same of Newton Polynomial too.

# 分段低次插值

同时，插值误差除来自截断误差外，还来自初始数据的误差和计算过程中的舍入误差。插值次数越高，计算工作量越大，积累误差也可能越大。

因此，在实际操作过程中，常常用分段低次插值进行计算，即把整个插值区间分成若干个小区间，在每个小区间上进行低次插值。

基本思想：就是将被插值函数逐段多项式化

# Spline interpolation

No test requirement

为得到光滑度更高、应用方便的插值函数 , 我们引入样条插值函数。

“样条”名词来源于工程中船体、汽车、飞机等的外形设计：给出外形曲线上的一组离散点( 样点 ) ，将有弹性的细长木条或钢条 (样条) 在样点上固定，使其在其它地方自由弯曲，这样样条所表示的曲线，称为样条曲线 ( 函 数 )

低阶的样条插值还具有“保凸”的重要性质

**Definition**

*Supposition*

1. $a<x_0<x_1<\cdots<x_n<b.$

*Condition*

1. $S(x)\in C^{n-1}[a,b].$
2. On each interval $[x_k,x_{k+1}]$, $S(x)$ is a polynomial with degree $n$.

*Definition*

1. $S(x)$ is $n$-degree spline function.

If we add condition that $S(x_i)=f(x_i)$, then it's a spline interpolation function.

三次样条与分段 Hermite 插值的根本区别在于 S(x) 自身光滑，不需要知道 f 的导数值（除了在 2 个端点可能需要）；而 Hermite 插值依赖于$f$在所有插值点的导数值