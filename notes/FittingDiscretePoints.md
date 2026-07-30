给定一个函数在离散点上的函数值， 要求在一个便于计算的简单函数类中找一个函数与给定的离散数据点最接近。（数据拟合）

插值法不同的是 **不要求所求的函数经过所有数据点**，这是因为数据不一定准确且有可能数据是大量的。

# 最小二乘拟合

To minify discrete 2-norm of error vector.

Similarly we can solve by
$$
G_n\vec a=((y, \varphi_1), (y, \varphi_2), \cdots, (y, \varphi_n))^T
$$

## Polynomial Fitting
When use $1,x,x^2,\cdots$ as the basis function

$$
G(i;j):=\sum_{k=0}^m x_k^{i+j}.
$$

$$
(y, \varphi_i)=\sum_{k=0}^m y_kx_k^i.
$$