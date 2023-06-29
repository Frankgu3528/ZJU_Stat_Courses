# 基于U-Net的portrait matting尝试

📌Github链接：https://github.com/ZJU-FrankGu/Portrait-Matting-Demo-with-UNet/tree/main

### 背景

抠图，matting，目标是分离出前景与背景。该领域有一个著名公式
$$
C=αF+(1−α)B
$$
于 1984 年被提出， C是实际观察到的图像， $\alpha$ 是透明度，F是前景， B是背景，其中 C已知，要估计$\alpha,F,B$ 三个未知数，无法解，因此需要引入其他约束，需要人们指明图像中哪些是感兴趣的区域，如 trimap 和基于涂鸦的方案；或者人为去掉一些未知量，假设背景是固定值，只需要估计 $\alpha$ 和 F ，绿幕就是这一类，更为简单。

### 算法survey

目前流行的抠图算法大致可以分为两类，一种是需要先验信息的Trimap-based的方法，宽泛的先验信息包括Trimap、粗糙mask、无人的背景图像、Pose信息等，网络使用先验信息与图片信息共同预测alpha；另一种则是Trimap-free的方法，仅根据图片信息预测alpha，对实际应用更友好。

其中最早的抠图算法基本都是基于trimap，传统的算法有[贝叶斯抠图](https://github.com/MarcoForte/bayesian-matting), KNN抠图。今年来基于深度学习提出了很多性的算法，比如Adobe提出的[Deep Image Matting](https://arxiv.org/abs/1703.03872), 需要先验的Trimap输入，但效果很好，以及沈小勇课题组做的[Deep Automatic Portrait Matting](http://www.cse.cuhk.edu.hk/~leojia/projects/automatting/papers/deepmatting.pdf),实现了end-end端的不需要用户提供Trimap的抠图 , 另外分割领域的经典算法（FCN，UNet，以及很火的SAM）也能进行抠图的任务。

在调研后，我就采用了诞生于医学图像分割的UNet，因为其训练比较方便且在小的数据集也能表现良好。

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230510114546949.png" alt="image-20230510114546949" style="zoom:33%;" />

### 训练过程

数据集：沈小勇网站中提供的数据集：为2000张人脸照片。

<img src="https://frank-first.oss-cn-hangzhou.aliyuncs.com/images/image-20230510152236389.png" alt="image-20230510152236389" style="zoom:33%;" />

我在RTX 2080Ti上训练了25轮，得到的`checkpoint_epoch25.pth`。参数如下：（在笔记本上需要减小batch size，不然会爆显存）

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230510151611440.png" alt="image-20230510151611440" style="zoom: 33%;" />

我尝试了不同的优化器，效果大同小异，最后还是用了原来的RMSprop，相比SGD会跟稳定一些。

在模型训练中，训练的loss随着训练的进行显著下降，但后来在验证集上却略有上升，猜测可能是出现了一些过拟合现象。

### 结果展示

下面是在原数据集的测试集上的效果展示，可以看到网络确实有一定效果。

<img src="https://frank-first.oss-cn-hangzhou.aliyuncs.com/images/image-20230510120226056.png" alt="image-20230510120226056" style="zoom: 19%;" /><img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230510120245293.png" alt="image-20230510120245293" style="zoom: 33%;" />

<img src="https://frank-first.oss-cn-hangzhou.aliyuncs.com/images/image-20230510120307117.png" alt="image-20230510120307117" style="zoom: 33%;" /><img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230510120316412.png" alt="image-20230510120316412" style="zoom: 33%;" />

另外，我也用一些其他的肖像照测试了模型的泛化能力，模型在自己的证件照这种简单的背景上表现十分优秀：

<img src="C:\Users\阿漆\Desktop\微信图片_20230510115952.jpg" alt="微信图片_20230510115952" style="zoom: 25%;" />

<img src="https://frank-first.oss-cn-hangzhou.aliyuncs.com/images/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202305101159521.jpg" alt="微信图片_202305101159521" style="zoom:25%;" />

当然，面对一些复杂的场景，模型也出现了一些问题，如左图因为小猫干扰了结果，右图的坐下因为暗光环境让模型很难决策。

<img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230510153304214.png" alt="image-20230510153304214" style="zoom: 20%;" /><img src="C:\Users\阿漆\AppData\Roaming\Typora\typora-user-images\image-20230510153442284.png" alt="image-20230510153442284" style="zoom:20%;" />

### 使用方法

训练： 

```python
python train.py
```

测试

```
python predict.py -i test/00002.png -o output.png --model checkpoints/checkpoint_epoch25.pth -v
```

另外我写好了一个脚本，直接`bash scripts/test.sh `就可以在output中得到一些生成的mask图片。详细的使用参数可以参照`README.md`

### 结论

这次训练暂时比较满意，模型确实学到了一些东西，在肖像分割上可以做一些简单的抠图。

我也有几个改进思路：

1. 通过对2000张的原始数据进行数据增强，比如对图片进行明暗，饱和，模糊以及一定的旋转当成新数据来训练模型，这样更多的数据可以增强模型的鲁棒性，减少一些过拟合。参考：pytorch中的[image transform](https://pytorch.org/vision/stable/transforms.html)
2. 设置更大的Downscaling factor of the images，我训练的时候一直设置成0.5
3. train longer + 根据情况调整学习率。

<img src="https://frank-first.oss-cn-hangzhou.aliyuncs.com/images/image-20230613143401836.png" alt="image-20230613143401836" style="zoom:33%;" />

![image-20230613143817049](https://frank-first.oss-cn-hangzhou.aliyuncs.com/images/image-20230613143817049.png)
