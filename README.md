&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Hi👋__，欢迎来到这个关于使用 树莓派4B 实现检测人体是否摔倒项目的教程！这次的项目系列将分为三个部分，而今天你将进入第一个部分，重点介绍如何做好准备工作、运行代码以及实现核心功能。  
  接下来，将通过以下几个步骤📜，带你深入源码，轻松上手这个项目！准备好了吗？让我们开始吧🚀！  
- 📝 项目简介
- ✨ 功能特点
- 🏗 项目结构
- 🚀 安装与运行
- 🔧 使用说明
- 🔮 下期预告
  
[演示视频📺]()
# 树莓派检测人体摔倒 项目
## 项目简介:
这个项目通过使用树莓派首先通过SSH连接PC端传输vscode等重要文件，接着导入代码包到树莓派中的vscode后，按顺序运行代码。先运行train训练代码，进行提取和训练人体结点后，保存节点位置到csv文件中。利用刚刚得到的csv文件，我们来测试代码，我们可以通过上传一段视频或者打开树莓派摄像，自身站在摄像头前做出动作，如果检测到人体有摔倒那么显示fall,如果检测到人体没有摔倒节点正常那么显示normal。 

本篇文章同时也会详细讲述，安装vscode编程代码,安装FileZilla进行互传文件，安装MobaXtarm进行远程连接树莓派的教程。

将遇到的报错问题总结好，以及将python版本不兼容问题一并解决。

项目采用了 1.14 英寸的TFT显示屏，展现了五列炫酷的转盘，每列包含 10 个不同的图标，转盘旋转时充满动感🎡。  
  通过 M5StickC Plus2 的按钮交互，玩家可以轻松控制游戏的启动与停止，仿佛置身于真实的老虎机🎮。这个项目不仅展示了 M5StickC Plus2 在图形显示和硬件控制方面的强大能力，还为玩家提供了乐趣满满的互动体验，是硬件开发和游戏开发爱好者绝佳的学习和参考项目💡！

## 功能特点
- 📏 体积小巧：轻便的设计，适合随身携带，轻松搭建。
- 🎉 趣味十足：互动性强，仿佛置身于真实的老虎机游戏世界。
- 🔋 功耗低：高效能低功耗，延长设备使用时间
## 项目结构
``` 
│──  README.md                # 项目说明文件
│──  M5StickCPlus2_slot       # 源代码文件夹
  │──  M5StickCPlus2_slot.ino   # 源代码文件
  │──  Slot.cpp                 # Slot功能实现文件
  │──  SLot.h                   # Slot功能定义文件
  │──  image                    # 图片素材文件夹
    │──  slot_bar.h               # esp32图标
    │──  slot_cherry.h            # 樱桃图标
    │──  slot_lemon.h             # 柠檬图标 
    │──  slot_openelab.h          # OpenELAB logo
    │──  slot-orange.h            # 橘子图标
    │──  slot_seven.h             # 数字7图标
    │──  slot_symbols.h           # 图标数据
```
## 安装与运行

### 先决条件
软件依赖：__Arduino IDE__、__VScode__ or __text__ 等   
硬件要求：__USB-C数据线__、__M5StickCPlus2__ 等  
依赖要求：__M5StickCPlus2库__、__Arduino库__
### Arduino IDE 安装步骤
```
链接：稍后上传
```
### 安装依赖
1、安装好Arduino IDE后，打开Arduino设置，复制M5开发板链接到图示箭头处后点击OK保存
```
https://static-cdn.m5stack.com/resource/arduino/package_m5stack_index.json
```
![QQ_1726105473838](https://github.com/user-attachments/assets/367bd060-13ab-4eda-9a43-13fbc0250580)  
  
2、打开Tools->Board->Boards Manager  

![QQ_1726105693629](https://github.com/user-attachments/assets/e70b4f19-c21a-4ea5-80e2-4d150b54a35f)  
  
3、搜索M5Stack，并选择安装，本主机已经安装所以不再重复安装  

![QQ_1726105854495](https://github.com/user-attachments/assets/11b18b6c-c8db-4ea4-b209-d22dd26eebbe) 

4、选择开发版，Tools->Board->M5Stack Arduino->M5StickCPlus2  

![QQ_1726106317846](https://github.com/user-attachments/assets/203d874b-f316-4ae7-827b-2e01493ce08d)


5、接下来安装M5StickCPlus2库，选择Tools->Manage Libraries，搜索M5StickCPlus2，再选择安装，此处已经安装就不再重复安装。

![QQ_1726106703496](https://github.com/user-attachments/assets/312bc9e1-521c-479e-831a-a3c22e45a6ec)  

### 编译运行
1、完成安装依赖后，打开好下载的压缩包  

![QQ_1726107516108](https://github.com/user-attachments/assets/cb2362f7-1871-418e-94dd-92ddfe7284b7)  

2、使用USB-C将Plus2连接至电脑，选择Tools->Port选择自己的端口  

![QQ_1726107673971](https://github.com/user-attachments/assets/17f0392a-b753-4aba-946c-ede75ba9092f)  

3、点击编译，待编译完成后再点击上传  

![QQ_1726107957719](https://github.com/user-attachments/assets/c1f953ad-5355-44e8-af0c-ac5da7542aa6)  

## python版本不兼容问题 不要卸掉树莓派系统自带的python，卸掉了系统会崩溃
-### 树莓派烧录系统中，目前提供的python只有最新版本3.11，本次介绍如何将python重装的问题。
-###1.更新树莓派系统

1 sudo  apt-get  update
2 sudo apt-get upgrade -y
1
2
-###2.安装python依赖环境

sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev
1
-###3.下载python3.7版本源码并解压

1 wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
2 tar zxvf Python-3.7.1.tgz
1
2
-###4.安装编译

1 cd Python-3.7.1
1
2

sudo ./configure && sudo make && sudo make install
1
5.建立软连接
安装python3.7以后我们可以查看python的版本

1 python --version
2 python3 --version

##报错问题
- ###
![image](https://github.com/user-attachments/assets/2adf55d0-fb75-4fff-b839-368261629fc8)

假如 Python安装报错：”ModuleNotFoundError:No module named _ctypes“ 的解决方案
sudo apt-get install libffi-dev

![image](https://github.com/user-attachments/assets/eed2707f-cc15-48c6-9e33-b4a40a5d12de)


.建立软连接
安装python3.7以后我们可以查看python的版本

1 python --version
2 python3 --version

将python3.7.1软链接到python上,方便使用

查看python和python3.7命令在哪

1 which python
2 which python3

建立软链接

1 sudo mv /usr/bin/python /usr/bin/python2.7.13
2 sudo ln -s /usr/local/bin/python3 /usr/bin/python

6.测试是否成功

1 ls -al /usr/local/bin/python*
1 python --version


![image](https://github.com/user-attachments/assets/44ec15a4-8126-4484-8635-ce7a358f8dbc)


## 使用说明
- ### 图片顺序、个数
老虎机共五列，每一列都可以放置 10 个图标，而且你可以随意调整它们的顺序！💡目前，我们已经准备了 6 个 48x48 像素的素材图标，它们的 RGB565 十六进制数据已经在代码里了，分别对应 slot_symbols 数组中的 0 到 5 号元素。如果你想调整每列的图标顺序和数量，只需要轻松修改 symbolIndices 数组中的数字，就能改变每一列的图标显示效果！🔧🎨  

![QQ_1726108827608](https://github.com/user-attachments/assets/45b5878d-3624-47b5-a671-fc40937d1898)

- ### 列与列、图与图的间隔
通过更改PAD_X以及PAD_Y可以更改列与列、图与图的间隔，通常默认是2，0  

![QQ_1726109192019](https://github.com/user-attachments/assets/3e14c412-8342-486d-ba00-b6a0f4d357ac)

- ### 转盘转动速度、停止减小速度
```
#define Speed_MAX 800//老虎机旋转的最高速度
#define Speed_MIN 50//老虎机旋转最低速
#define Acceleration_MAX 12 //老虎机加速时的加速度
#define Acceleration_MIN -20//老虎机减速时的加速度
```
  ![QQ_1726109492610](https://github.com/user-attachments/assets/aaa6b4a0-79b1-491a-8dbd-ca76cc8c1eee)

## 下期预告
下期将详细介绍怎么更改老虎机的图片，我们会通过对图片取模获得图片的十六进制参数，并调整成我们想要的格式，然后在老虎机上呈现出我们所需要的图片 __敬请期待!!!__  

![QQ_1726122393803](https://github.com/user-attachments/assets/71507de5-dad0-4688-84bf-56cc25878e35)  

[第二部分链接](https://github.com/OpenELAB/OpenELAB-M5StickCPlus2-Slot-2.git)
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

