# 数据集介绍

***

本代码使用RDD2022数据集，原始数据保存在src/original_data中。此外，laugh12321整理了大部分道路病害数据集（包括RDD），在一定条件下可以与RDD2022混用，链接如下：https://www.cnblogs.com/laugh12321/p/17874752.html

本代码中对数据集进行修改，分为五类：横向裂缝，纵向裂缝，网状裂缝，坑洼，修补后路面。可以通过修改txt_generate文件和yaml_generate文件，自定义修改数据集。

# 运行结果介绍

***

运行后的结果放置在src/yolo/runs文件夹中。权重保存在weights文件夹中。该权重以450 epochs，16 batch size训练得到。

# 代码运行

***

通过依次运行ini文件夹下的img_process，txt_generate，shuffle_data三个文件，可以在src/processed_data中得到符合yolo标注格式的train文件夹。

img_process文件夹中使用**双边滤波算法**对图像文件进行了去噪处理


在得到数据之后，通过运行train_model内的yaml_generate文件，生成自定义的yaml文件，之后运行Train文件。

在运行完之后，结果保存在src/yolo/runs中。

之后可以运行visulize文件，使用模型预测验证集/测试集，进行预测结果的可视化。可视化结果保存在src/predict中
