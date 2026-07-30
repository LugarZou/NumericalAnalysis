# Problem and Method

Fit the following data with polynomials and rational functions.

| x | 0 | 0.1  | 0.2 | 0.3  | 0.5  | 0.8  |
| - | - | ---- | --- | ---- | ---- | ---- |
| y | 1 | 0.41 | 0.5 | 0.61 | 0.91 | 2.02 |

When fitting with polynomials we use $1,x,x^2,\cdots$ as the base functions and we solve Gramar matrix equation.

When optimising rational model, we simply call `scipy.optimize.curve_fit()`.

According the visualisation result of polynomial fitting, we choose functions

$$
R(m,n):=\frac{\sum_{i=m}^1p_ix^i+1}{\sum_{i=n}^1q_ix^i+1},
$$

where $m+n$ is the total number of parameters we should learn.

# Result and Analysis

## Polynomial interpolation

We test polynomial fitting with degree $0,1,2,3,4,5$, where deg-$5$ polynomial with 6 parameters is a perfect fit.

The visualisation result are shown below.

![image-20240622121424337](/home/lugar/.config/Typora/typora-user-images/image-20240622121424337.png)

| degree | MSE                   |
| ------ | --------------------- |
| 0      | 0.2913805555555556    |
| 1      | 0.11714552529182877   |
| 2      | 0.015030987844547176  |
| 3      | 0.008758200837862547  |
| 4      | 0.0008683976568533322 |
| 5      | 9.32704262205976e-21  |

![image-20240622123238791](/home/lugar/.config/Typora/typora-user-images/image-20240622123238791.png)

We can see that as the degree of the fitting polynomial approaches the \#data points-1, the marginal benefit decreases.

## Rational Fitting

| MSE | 1                     | 2                      | 3                     | 4                     |
| --- | --------------------- | ---------------------- | --------------------- | --------------------- |
| 1   | 0.11005960797947695   | 0.0016106949411686111  | 3.78085218100902e-05  | 3.697785493223493e-32 |
| 2   | 0.005037957489930283  | 7.707154323434576e-06  | 6.162975822039155e-33 |                       |
| 3   | 0.0008882674551970257 | 2.5679065925163146e-33 |                       |                       |
| 4   | 4.108650548026103e-33 |                        |                       |                       |

![image-20240622131633659](/home/lugar/.config/Typora/typora-user-images/image-20240622131633659.png)

According to the heat map we can see that the diagonal has similar performance since they have same number of parameters. Additionally, in the same diagonal the cell near the mid has better performance.

### Visualisation

**For $R(1,n)$**

Note that the flat of $R(1,1)$ is resulted from truncation to enable proper visualisation.

![image-20240622130909942](/home/lugar/.config/Typora/typora-user-images/image-20240622130909942.png)

**For $R(2,n)$**

![image-20240622125732231](/home/lugar/.config/Typora/typora-user-images/image-20240622125732231.png)

**For $R(3,n)$**

![image-20240622125838897](/home/lugar/.config/Typora/typora-user-images/image-20240622125838897.png)

**For $R(4,n)$**

![image-20240622130211747](/home/lugar/.config/Typora/typora-user-images/image-20240622130211747.png)

We can see that then the denominator polynomial has higher degree, the function become smoother.

## Comparation

We know that the third and fourth diagonal rational function methods have same number of parameters as deg-$3,4$ polynomials. 

From the visualisations provided above we can see that rational function fits data points in a smoother way, which makes sense as it utilises a wider range of functions including polynomials.
