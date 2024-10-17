本代码使用RDD2022数据集，原始数据保存在src/original_data中。此外，laugh12321整理了大部分道路病害数据集（包括RDD），在一定条件下可以与RDD2022混用，链接如下：https://www.cnblogs.com/laugh12321/p/17874752.html
通过依次运行ini文件夹下的img_process，txt_generate，shuffle_data三个文件，可以在src/processed_data中得到符合yolo标注格式的train文件夹。
对数据集进行修改，分为五类：横向裂缝，纵向裂缝，网状裂缝，坑洼，修补后路面。可以通过修改txt_generate文件和yaml_generate文件，自定义修改数据集。

在得到数据之后，通过运行train_model内的yaml_generate文件，生成自定义的yaml文件，之后运行Train文件。
在运行完之后，结果保存在src/yolo/runs中。
