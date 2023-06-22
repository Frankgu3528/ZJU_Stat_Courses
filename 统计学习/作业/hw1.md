# hw1

###### 顾格非 3210103528

### 1.

**P**值表明，TV和radio的系数估计值是显著不为0的，说明在TV，radio和newspaper都投放广告时，TV和radio对销售有正向影响，而newspaper对销售没有什么影响。

### 5.

$$
\hat{y}_i=x_i \frac{\sum_{=1}^n x_j y_j}{\sum_{k=1}^n x_k^2}=\sum_{j=1}^n \frac{x_i x_j}{\sum_{k=1}^n x_k^2} y_j=\sum_{j=1}^n a_j y_j\\
\Rightarrow a_{i^{'}} =\frac{x_i x_{i^{'}}}{\sum_{k=1}^n x_k^2}
$$

### 8.

```R
library(ISLR)
data(Auto)
fit <- lm(mpg ~ horsepower, data = Auto)
summary(fit)
```

```
Call:
lm(formula = mpg ~ horsepower, data = Auto)

Residuals:
     Min       1Q   Median       3Q      Max 
-13.5710  -3.2592  -0.3435   2.7630  16.9240 

Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) 39.935861   0.717499   55.66   <2e-16 ***
horsepower  -0.157845   0.006446  -24.49   <2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 4.906 on 390 degrees of freedom
Multiple R-squared:  0.6059,	Adjusted R-squared:  0.6049 
F-statistic: 599.7 on 1 and 390 DF,  p-value: < 2.2e-16
```

1. F-statistic 远大于1，其P值非常小，可以拒绝原假设认为mpg和horsepower之间是**有相关性**的。

2. mpg均值为23.44592，RSE的值为4.906，误差百分比约为20.92%。R2值为0.6059，表明mpg的**60.59%**的变异可以由horsepower解释。

3. **negative.**

4. `predict(fit, data.frame(horsepower = 98), interval = "confidence")` ：

  ```
         fit      lwr      upr
  1 24.46708 23.97308 24.96108
  ```

  `predict(fit, data.frame(horsepower = 98), interval = "prediction")`

  ```
         fit     lwr      upr
  1 24.46708 14.8094 34.12476
  ```

(b)

```
plot(Auto$horsepower, Auto$mpg, main = "Scatterplot of mpg vs. horsepower", xlab = "horsepower", ylab = "mpg", col = "blue")
abline(fit, col = "red")
```

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230328221059016.png" alt="image-20230328221059016" style="zoom:33%;" />

(c)

```
par(mfrow = c(2, 2))
plot(fit)
```

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230328221207295.png" alt="image-20230328221207295" style="zoom:33%;" />

数据中存在非线性关系，以及有一些异常点。

### 9.

1. `pairs(Auto)`

   <img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230328221834072.png" alt="image-20230328221834072" style="zoom: 33%;" />
   
2. ![image-20230329224057540](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230329224057540.png)

3. ```
   fit2 <- lm(mpg ~ . - name, data = Auto)
   summary(fit2)
   ```

```
## 
## Call:
## lm(formula = mpg ~ . - name, data = Auto)
## 
## Residuals:
##     Min      1Q  Median      3Q     Max 
## -9.5903 -2.1565 -0.1169  1.8690 13.0604 
## 
## Coefficients:
##                Estimate Std. Error t value Pr(>|t|)    
## (Intercept)  -17.218435   4.644294  -3.707  0.00024 ***
## cylinders     -0.493376   0.323282  -1.526  0.12780    
## displacement   0.019896   0.007515   2.647  0.00844 ** 
## horsepower    -0.016951   0.013787  -1.230  0.21963    
## weight        -0.006474   0.000652  -9.929  < 2e-16 ***
## acceleration   0.080576   0.098845   0.815  0.41548    
## year           0.750773   0.050973  14.729  < 2e-16 ***
## origin         1.426141   0.278136   5.127 4.67e-07 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 3.328 on 384 degrees of freedom
## Multiple R-squared:  0.8215, Adjusted R-squared:  0.8182 
## F-statistic: 252.4 on 7 and 384 DF,  p-value: < 2.2e-16
```

1. F-statistic远大于1，其P值非常小，可以拒绝零假设，即至少有一个预测变量与相应变量是显著相关的。

2. displacement, weight, year, and origin

3. 系数是0.750773，表示每过一年，mpg增长为0.750773。

**9d**

```
par(mfrow = c(2, 2))
plot(fit2)
```

残差与拟合值的关系图表明数据中存在非线性，另外标准化残差与杠杆的关系图表明存在一些异常值（高于2或低于-2）和一个高杠杆点（点14）。

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230329224834217.png" alt="image-20230329224834217" style="zoom:33%;" />

**9e**

```
fit3 <- lm(mpg ~ cylinders * displacement+displacement * weight, data = Auto[, 1:8])
summary(fit3)
```

```
## 
## Call:
## lm(formula = mpg ~ cylinders * displacement + displacement * 
##     weight, data = Auto[, 1:8])
## 
## Residuals:
##      Min       1Q   Median       3Q      Max 
## -13.2934  -2.5184  -0.3476   1.8399  17.7723 
## 
## Coefficients:
##                          Estimate Std. Error t value Pr(>|t|)    
## (Intercept)             5.262e+01  2.237e+00  23.519  < 2e-16 ***
## cylinders               7.606e-01  7.669e-01   0.992    0.322    
## displacement           -7.351e-02  1.669e-02  -4.403 1.38e-05 ***
## weight                 -9.888e-03  1.329e-03  -7.438 6.69e-13 ***
## cylinders:displacement -2.986e-03  3.426e-03  -0.872    0.384    
## displacement:weight     2.128e-05  5.002e-06   4.254 2.64e-05 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 4.103 on 386 degrees of freedom
## Multiple R-squared:  0.7272, Adjusted R-squared:  0.7237 
## F-statistic: 205.8 on 5 and 386 DF,  p-value: < 2.2e-16
```

从P-value得出，displacement和weight是显著的。cylinders and displacement不是。

**9f**

```
par(mfrow = c(2, 2))
plot(log(Auto$horsepower), Auto$mpg)
plot(sqrt(Auto$horsepower), Auto$mpg)
plot((Auto$horsepower)^2, Auto$mpg)
```

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230329225304555.png" alt="image-20230329225304555" style="zoom: 33%;" />

对horsepower，acceleration以及weight做变换后，发现displacement的系数在统计上不显著不为0了，而$horsepower，horsepower^2，weight，weight^2$的系数在统计上都显著不为0了，$log(acceleration)，sqrt(acceleration)$的系数在统计上也是显著不为0的。不过有$log(acceleration)$的模型对数据拟合得更好。
