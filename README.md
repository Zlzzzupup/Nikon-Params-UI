# Nikon-Params-UI

> **这是一个用于给照片批量添加Nikon相机参数水印工具。**

如果您觉得程序对您有所帮助的话，可以点击star点亮下本项目，谢谢！

**特别感谢小红书中提供水印抠图的 [鱼虾一整晚](https://www.xiaohongshu.com/user/profile/64736c3400000000100357fa?xhsshare=CopyLink&appuid=63ed7d6d000000002501f612&apptime=1708878092)**

## 效果展示
|||
|-|-|
|![](images/test1.jpg)|![](images/test.jpg)|
|![](images/test2.jpg)|![](images/test3.jpg)|


## 使用教程
1. 安装依赖库
    ```pip install -r requirements.txt```

2. 将需要添加水印的图像放入**inputs文件夹**
3. 运行程序
   ```python main.py```
4. 添加后的水印图像保存于**outputs文件夹**

## TODO
1. 目前仅完成了横向构图的图像水印添加，竖向构图的还在准备；
2. 将项目编译为Windows下的可执行文件；
3. 代码逻辑优化，以及显示细节的完善；