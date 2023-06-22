# [Statistical Learning]hw2

###### 顾格非 3210103528

### Q3

写出后验概率如下，我们即要找k
$$
p_k(x) = \frac {\pi_k \frac {1} {\sqrt{2 \pi} \sigma_k} \exp(- \frac {1} {2 \sigma_k^2} (x - \mu_k)^2) } {\sum { \pi_l \frac {1} {\sqrt{2 \pi} \sigma_k} \exp(- \frac {1} {2 \sigma_k^2} (x - \mu_l)^2) }}
$$

我们记常数 $C' = \frac { \frac {1} {\sqrt{2 \pi}}} {\sum { \pi_l \frac {1} {\sqrt{2 \pi} \sigma_k} \exp(- \frac {1} {2 \sigma_k^2} (x - \mu_l)^2) }}$

方程变成 $p_k(x) = C' \frac{\pi_k}{\sigma_k} \exp(- \frac {1} {2 \sigma_k^2} (x - \mu_k)^2)$

取log：$log(p_k(x)) = log(C') + log(\pi_k) - log(\sigma_k) + (- \frac {1} {2 \sigma_k^2} (x - \mu_k)^2)$

$=log(p_k(x)) = (- \frac {1} {2 \sigma_k^2} (x^2 + \mu_k^2 - 2x\mu_k)) + log(\pi_k) - log(\sigma_k) + log(C')$

可以看出贝叶斯分类器是二次的。

### Q12

a. 
$$
log ~odds = \hat\beta_0+\hat\beta_1x
$$
b. 
$$
log~odds=log~odds\frac{\hat Pr(Y=orange | X=x)}{\hat Pr(Y=apple | X=x)}=log \frac{\exp(\hat\alpha_\text{orange0}+\hat\alpha_\text{orange1}x)}{\exp(\hat\alpha_\text{apple0}+\hat\alpha_\text{apple1}x)}\\=\hat{\alpha}_{\text{orange0}}+\hat{\alpha}_{\text{orange1}}x-\hat{\alpha}_{\text{apple0}}-\hat{\alpha}_{\text{apple1}}x
$$
c.
$$
\hat{\alpha}_{\text{orange0}},\hat{\alpha}_{\text{orange1}},\hat{\alpha}_{\text{apple0}},\hat{\alpha}_{\text{apple1}}满足如下等式：\\
\begin{gathered}
3=\hat{\beta}_0 \approx\hat{\alpha}_{\text{orange}0} -\hat{\alpha}_{\text{apple}0} \\
-2=\hat{\beta}_1 \approx \hat{\alpha}_{\text{orange1}} - \hat{\alpha}_{\text{apple1}} 
\end{gathered}
$$
d.
$$
\begin{gathered}
\hat{\beta}_0 \approx\hat{\alpha}_{\text{orange}0} -\hat{\alpha}_{\text{apple}0} \\
\hat{\beta}_1 \approx \hat{\alpha}_{\text{orange1}} - \hat{\alpha}_{\text{apple1}} 
\end{gathered}
\begin{gathered}
\approx 1.5-3.6=-2.1 \\
\approx-2.4-0.8=-3.2 
\end{gathered}
$$

e.虽然系数不一样，但两种方法最终得到的结果应该是吻合的。

### Q14

a.

```
library(ISLR)
attach(Auto)
mpg01 <- rep(0, length(mpg))
mpg01[mpg > median(mpg)] <- 1
Auto <- data.frame(Auto, mpg01)
```

b.

```
cor(Auto[, -9])
pairs(Auto)
```

![image-20230508215814789](C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508215814789.png)

```R
boxplot(cylinders ~ mpg01, data = Auto, main = "Cylinders vs mpg01")
boxplot(displacement ~ mpg01, data = Auto, main = "Displacement vs mpg01")
boxplot(horsepower ~ mpg01, data = Auto, main = "Horsepower vs mpg01")
boxplot(weight ~ mpg01, data = Auto, main = "Weight vs mpg01")
boxplot(acceleration ~ mpg01, data = Auto, main = "Acceleration vs mpg01")
boxplot(year ~ mpg01, data = Auto, main = "Year vs mpg01")
```

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508220159324.png" alt="image-20230508220159324" style="zoom: 25%;" /><img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508220332727.png" alt="image-20230508220332727" style="zoom:25%;" />

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508220417621.png" alt="image-20230508220417621" style="zoom:25%;" /><img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508220443520.png" alt="image-20230508220443520" style="zoom:25%;" />

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508220504341.png" alt="image-20230508220504341" style="zoom:25%;" /><img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508220531813.png" alt="image-20230508220531813" style="zoom:25%;" />

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508221256225.png" alt="image-20230508221256225" style="zoom:25%;" /><img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230508221428534.png" alt="image-20230508221428534" style="zoom:25%;" />

由箱线图可以看出，mpg01和cylinders，displacement，horsepower，weight是相关的。

```
lda.fit11 = lda(mpg01 ~ cylinders + weight + displacement + horsepower, data = Auto, subset = train)
lda.pred = predict(lda.fit11, Auto.test)
mean(lda.pred$class != mpg01.test)
```
得到：**LDA**的test error rate是 0.1263736

```
qda.fit11 = qda(mpg01 ~ cylinders + weight + displacement + horsepower, data = Auto, subset = train)
qda.pred = predict(qda.fit11, Auto.test)
mean(qda.pred$class != mpg01.test)
```

得到：**QDA**的test error rate是0.1318681

```
fit.glm <- glm(mpg01 ~ cylinders + weight + displacement + horsepower, data = Auto, family = binomial, subset = train)
probs <- predict(fit.glm, Auto.test, type = "response")
pred.glm <- rep(0, length(probs))
pred.glm[probs > 0.5] <- 1
mean(pred.glm != mpg01.test)
```

得到：**logistic regression**的test error rate是0.1208791

```
train.X <- cbind(cylinders, weight, displacement, horsepower)[train, ]
test.X <- cbind(cylinders, weight, displacement, horsepower)[!train, ]
train.mpg01 <- mpg01[train]
set.seed(1)
pred.knn <- knn(train.X, test.X, train.mpg01, k = 1)
mean(pred.knn != mpg01.test)
```

| value of K | test errorrate |
| ---------- | -------------- |
| 1          | 0.1538462      |
| 3          | 0.1373626      |
| 5          | 0.1483516      |
| 7          | 0.1483516      |
| 9          | 0.1593407      |
| 19         | 0.1483516      |
| 99         | 0.1428571      |

上面是一些不同的K做的实验，可以看出在做的K中，K=3效果最好

***

### Q2

a. $P=\frac{n-1}{n}$ （因为有n-1个样本不包含第j个）

b. $P=\frac{n-1}{n}$

c. 等价于对于n次抽样，每次都没有抽到第j个观测的概率。则$P=(\frac{n-1}{n})^n$

d. 由c知： $P=1-(\frac{n-1}{n})^n=0.67232$

e.$P=1-(\frac{n-1}{n})^n=0.633968$

f. $P=1-(\frac{n-1}{n})^n=0.632305$

g. 如下图所示。可以看到，随着n增大，第j个观测在bootstrap sample的概率显示快速下降，后来趋向于1-1/e。

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230509195643735.png" alt="image-20230509195643735" style="zoom:25%;" />

h. 运行所给代码得到0.6343，跟上面的结果很接近。

### Q5

a.

```R
library(ISLR)
attach(Default)
set.seed(1)
fit.glm <- glm(default ~ income + balance, data = Default, family = "binomial")
```

b.

```
train <- sample(dim(Default)[1], dim(Default)[1] / 2)
fit.glm <- glm(default ~ income + balance, data = Default, family = "binomial", subset = train)
probs <- predict(fit.glm, newdata = Default[-train, ], type = "response")
pred.glm <- rep("No", length(probs))
pred.glm[probs > 0.5] <- "Yes"
mean(pred.glm != Default[-train, ]$default)
```

代码如上，最后得到验证集上的错误率=0.0286。

c. 运行上面的代码3次，得到0.0252，0.0246，0.0266三个不同的错误率。

d. 按下面的代码加入哑变量student进行预测，得到0.0264，并没有太多的区别。

```
fit.glm <- glm(default ~ income + balance + student, data = Default, family = "binomial", subset = train)
```

### Q6

```
fit.glm <- glm(default ~ income + balance, data = Default, family = "binomial")
summary(fit.glm)
```

```
## 
## Call:
## glm(formula = default ~ income + balance, family = "binomial", 
##     data = Default)
## 
## Deviance Residuals: 
##     Min       1Q   Median       3Q      Max  
## -2.4725  -0.1444  -0.0574  -0.0211   3.7245  
## 
## Coefficients:
##               Estimate Std. Error z value Pr(>|z|)    
## (Intercept) -1.154e+01  4.348e-01 -26.545  < 2e-16 ***
## income       2.081e-05  4.985e-06   4.174 2.99e-05 ***
## balance      5.647e-03  2.274e-04  24.836  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## (Dispersion parameter for binomial family taken to be 1)
## 
##     Null deviance: 2920.6  on 9999  degrees of freedom
## Residual deviance: 1579.0  on 9997  degrees of freedom
## AIC: 1585
## 
## Number of Fisher Scoring iterations: 8
```

三个参数 $β_0, β_1 ~ β_2 $的标准差是 $0.4347564, 4.985167210^{-6} ~2.273731410^{-4}$.

b.

```
boot.fn <- function(data, index) {
    fit <- glm(default ~ income + balance, data = data, family = "binomial", subset = index)
    return (coef(fit))
}
```

c.

```
library(boot)
boot(Default, boot.fn, 1000)
```

```
## 
## ORDINARY NONPARAMETRIC BOOTSTRAP
## 
## 
## Call:
## boot(data = Default, statistic = boot.fn, R = 1000)
## 
## 
## Bootstrap Statistics :
##          original        bias     std. error
## t1* -1.154047e+01 -8.008379e-03 4.239273e-01
## t2*  2.080898e-05  5.870933e-08 4.582525e-06
## t3*  5.647103e-03  2.299970e-06 2.267955e-04
```

三个参数的标准差分别是 $0.4239, 4.583 *10^{-6} ,2.268 * 10^{-4}$

d. 对于斜率及income的系数的标准误差，logistic回归略大于bootstrap方法，balance系数的标准误差，logistic回归略小于bootstrap方法。
