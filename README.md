&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Hi👋__，欢迎来到这个关于使用 树莓派4B 实现检测人体是否摔倒项目的教程！这次的项目系列将分为三个部分，而今天你将进入第一个部分，重点介绍如何做好准备工作、运行代码以及实现核心功能。  
  接下来，将通过以下几个步骤📜，带你深入源码，轻松上手这个项目！准备好了吗？让我们开始吧🚀！  
- 📝 项目简介
- ✨ 功能特点
- 🏗 项目结构
- 🚀 安装与运行
- 🔧 使用说明
- 🔮 下期预告
- #注：本项目是基于KNN_人体3D识别骨架的项目进行修改，展示了在树莓派上如何展示的全教学过程。
  
[演示视频📺]()
# 树莓派检测人体摔倒 项目
## 项目简介:
这个项目通过使用树莓派首先通过SSH连接PC端传输vscode等重要文件，接着导入代码包到树莓派中的vscode后，按顺序运行代码。先运行train训练代码，进行提取和训练人体结点后，保存节点位置到csv文件中。利用刚刚得到的csv文件，我们来测试代码，我们可以通过上传一段视频或者打开树莓派摄像，自身站在摄像头前做出动作，如果检测到人体有摔倒那么显示fall,如果检测到人体没有摔倒节点正常那么显示normal。 

本篇文章同时也会详细讲述，安装vscode编程代码,安装FileZilla进行互传文件，安装MobaXtarm进行远程连接树莓派的教程。

将遇到的报错问题总结好，以及将python版本不兼容问题一并解决。


## 功能特点
- 📏 识别人体节点。
- 🎉 判断是否摔倒，提高救助率。
- 
## 项目结构
``` 
│──  README.md                # 项目说明文件
│──  test.py                  # 打开摄像头测试代码
  │──  train.py               # 训练文件
  │──  Slot.cpp                 # Slot功能实现文件
  │──  SLot.h                   # Slot功能定义文件
  │──  image                    # 图片素材文件夹

  
```
### 先决条件  
软件依赖：__Arduino IDE__、__VScode__ or __text__ 等   
硬件要求：__USB-C数据线__、__树莓派4B__ 等  
依赖要求：__opencv库__、__pandas库__  
### Arduino IDE 安装步骤  

## python版本不兼容问题 不要卸掉树莓派系统自带的python，卸掉了系统会崩溃  
-### 树莓派烧录系统中，目前提供的python只有最新版本3.11，本次介绍如何将python重装的问题。   
-###建议安装python3.7版本更为适配树莓派使用更加稳定       
-###1.更新树莓派系统     
``` 
1 sudo  apt-get  update  
2 sudo apt-get upgrade -y  
```
-###2.安装python依赖环境  
```
sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev  
```
-###3.下载python3.7版本源码并解压  
```
1 wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz  
2 tar zxvf Python-3.7.1.tgz  
```
-###4.安装编译  
```
1 cd Python-3.7.1    
2 sudo ./configure && sudo make && sudo make install  
```

5.建立软连接  
安装python3.7以后我们可以查看python的版本    
```
1 python --version  
2 python3 --version  
```

##报错问题  
- ###
![image](https://github.com/user-attachments/assets/2adf55d0-fb75-4fff-b839-368261629fc8)  

假如 Python安装报错：”ModuleNotFoundError:No module named _ctypes“ 的解决方案  
```
sudo apt-get install libffi-dev  
```

![image](https://github.com/user-attachments/assets/eed2707f-cc15-48c6-9e33-b4a40a5d12de)  


.建立软连接  
安装python3.7以后我们可以查看python的版本  
```
1 python --version
2 python3 --version
```

将python3.7.1软链接到python上,方便使用   

查看python和python3.7命令在哪    
```
1 which python
2 which python3
```

建立软链接    
```
1 sudo mv /usr/bin/python /usr/bin/python2.7.13
2 sudo ln -s /usr/local/bin/python3 /usr/bin/python
```

6.测试是否成功  
```
1 ls -al /usr/local/bin/python*
2 python --version
```


![image](https://github.com/user-attachments/assets/44ec15a4-8126-4484-8635-ce7a358f8dbc)  

创建虚拟环境  
```
python -m venv pytorch  
```

激活虚拟环境  
```
source pytorch/bin/activate  
```

适配numpy版本：  
![image](https://github.com/user-attachments/assets/c7790cfc-bf1a-472e-98d2-790fa5f94fa3)  


## 安装与运行
###运行代码，安装opencv需要的步骤：  
下载 opencv-python 和 opencv-contrib-python 库  
opencv-python地址：piwheels - opencv-python   https://www.piwheels.org/project/opencv-python/  
opencv-contrib-python地址：piwheels - opencv-contrib-python   https://www.piwheels.org/project/opencv-contrib-python/  

使用uname -a查询自己树莓派合适的opencv版本    
![image](https://github.com/user-attachments/assets/8986a20b-48bf-4dec-ad9c-06245554ee95)  

![image](https://github.com/user-attachments/assets/4bb34404-9fe2-482c-b59d-7ed8cfcb0b37)  

![image](https://github.com/user-attachments/assets/49634ccd-5037-4766-9f2b-8ed612ff9bf5)  

安装报错的解决方法：  
![image](https://github.com/user-attachments/assets/43b705ff-4113-46d1-94aa-6547f1a8850b)  


在桌面上：  
```
cd Desktop
ls 
pip3 install <安装包名>
```
![image](https://github.com/user-attachments/assets/00986329-4855-405b-ac91-54aa601aaedc)  


之后分别使用如下指令进行安装依赖的numpy  
```
sudo apt-get install python3-h5py  
pip3 install numpy （按Tab键自动补全）  

```
![image](https://github.com/user-attachments/assets/d544cdb9-672e-4c3c-91ad-aa330b484f04)  
|
### 安装依赖
opencv依赖的其他库安装：  
```
sudo apt-get install libhdf5-dev  
sudo apt-get install libatlas-base-dev   
sudo apt-get install libjasper-dev  
sudo apt-get install libqt4-test  
sudo apt-get install libqtgui4  
sudo apt-get update
```
当出现以下确认画面时不要输入y,直接点击enter：  
![image](https://github.com/user-attachments/assets/80ab771f-c615-48c5-980e-31cc855b6c60)  

安装上述步骤走完基本就已经成功安装OpenCV了：  

![image](https://github.com/user-attachments/assets/5e7a7468-28f1-4540-abeb-a2b7ac895e7a)  

安装vscode:  
![image](https://github.com/user-attachments/assets/6b45c5e3-785c-4a4c-93c1-855bb8b8bec2)  


![image](https://github.com/user-attachments/assets/9df9bad7-ef5e-4db8-bf7c-22ed2fb9c107)  




## 如何联系维护者或开发者
__OpenELAB:__   
[![OpenELAB_logo_resized_150](https://github.com/user-attachments/assets/5d3de375-359c-46a3-96bb-aaa211c6c636)](https://openelab.io)  
__YouTube:__  
[![youtube_logo_200x150](https://github.com/user-attachments/assets/d2365e7f-4ffe-4124-bf62-21eba19a71e4)](https://www.youtube.com/@OpenELAB)  
__X :__  
[![X_logo_150x150](https://github.com/user-attachments/assets/4ad5095f-2573-4791-9360-b355530093bf)](https://twitter.com/openelabio)  
__FaceBook:__  
[![facebook_logo_cropped_150x150](https://github.com/user-attachments/assets/52f2dc9a-a564-49a5-b72e-30eafbbc281f)](https://www.facebook.com/profile.php?id=61559154729457)  
__Discord__  
[![resized_image_150x150](https://github.com/user-attachments/assets/93ecd098-3391-45bb-9d80-b166c197a475)](https://discord.gg/VQspWyck)  

__源码改自于__
[M5StickCPlus](https://github.com/Sarah-C/M5StickC_Plus_Slot_Machine)

