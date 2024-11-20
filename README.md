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


## 功能特点
- 📏 识别人体节点。
- 🎉 判断是否摔倒，提高救助率。
- 
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
###运行代码，安装opencv需要的步骤：
下载 opencv-python 和 opencv-contrib-python 库；
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
sudo apt-get install python3-h5py
pip3 install numpy （按Tab键自动补全）
![image](https://github.com/user-attachments/assets/d544cdb9-672e-4c3c-91ad-aa330b484f04)

opencv依赖的其他库安装：

sudo apt-get install libhdf5-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqt4-test
sudo apt-get install libqtgui4
sudo apt-get update
当出现以下确认画面时不要输入y,直接点击enter：
![image](https://github.com/user-attachments/assets/80ab771f-c615-48c5-980e-31cc855b6c60)

安装上述步骤走完基本就已经成功安装OpenCV了：

![image](https://github.com/user-attachments/assets/5e7a7468-28f1-4540-abeb-a2b7ac895e7a)

安装vscode:
![image](https://github.com/user-attachments/assets/6b45c5e3-785c-4a4c-93c1-855bb8b8bec2)


![image](https://github.com/user-attachments/assets/9df9bad7-ef5e-4db8-bf7c-22ed2fb9c107)

安装成功后：
![image](https://github.com/user-attachments/assets/ea277509-b497-4b76-8566-23958d801273)

![image](https://github.com/user-attachments/assets/e1fd0d58-100b-4a9d-9c0f-8c8b502a46c4)

打开远程：
![82990c40bce1d5be8c360ba056338d25](https://github.com/user-attachments/assets/cec0a368-4f14-44ba-962c-bc4a5e0921d1)

打开摄像头步骤：
![9c0e721c3f94b627fbdb724d603371dc_720](https://github.com/user-attachments/assets/a193f9e8-d4eb-4a9c-8845-c5084e809d11)
![b2a24c5c7c22cb5aba1b6f481550edd0_720](https://github.com/user-attachments/assets/8c07e88d-383f-45b5-823d-7dc8498c10d9)
![d15f0dc4e379cefef9fd5be1c07ea376_720](https://github.com/user-attachments/assets/368f96ad-6e79-450c-9deb-be89f488f3cd)

![b24b0293acafce3bc31c192cc4b936dc_720](https://github.com/user-attachments/assets/c0374e32-99a7-4f82-9cdf-e530fc689b8b)
![e16696d17803db088ca54a734c738734_720](https://github.com/user-attachments/assets/db3541a1-9984-4921-b087-f9a26a6a4c26)

树莓派上的IDE python运行位置：
![cad7f71ca307bc83acc661290aa79f46_720](https://github.com/user-attachments/assets/c712ccad-a02f-4b49-8583-6b7db1d85103)

配置code:好处，改报错更加方便：
![image](https://github.com/user-attachments/assets/0296ca26-4ec2-44ed-9d7f-1b638cccae26)
打开过程：
![image](https://github.com/user-attachments/assets/31c92f39-8236-4eb4-a818-a11273778458)

### 先决条件
软件依赖：__Arduino IDE__、__VScode__ or __text__ 等   
硬件要求：__USB-C数据线__、__树莓派4B__ 等  
依赖要求：__opencv库__、__pandas库__
### Arduino IDE 安装步骤

opencv依赖的其他库安装：

sudo apt-get install libhdf5-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqt4-test
sudo apt-get install libqtgui4
sudo apt-get update


### 安装依赖


### 编译运行
1、完成安装依赖后，打开好下载的压缩包  

![QQ_1726107516108](https://github.com/user-attachments/assets/cb2362f7-1871-418e-94dd-92ddfe7284b7)  

2、使用USB-C将Plus2连接至电脑，选择Tools->Port选择自己的端口  

![QQ_1726107673971](https://github.com/user-attachments/assets/17f0392a-b753-4aba-946c-ede75ba9092f)  

3、点击编译，待编译完成后再点击上传  

![QQ_1726107957719](https://github.com/user-attachments/assets/c1f953ad-5355-44e8-af0c-ac5da7542aa6)  

## python版本不兼容问题 不要卸掉树莓派系统自带的python，卸掉了系统会崩溃
-### 树莓派烧录系统中，目前提供的python只有最新版本3.11，本次介绍如何将python重装的问题。
-###建议安装python3.7版本更为适配树莓派使用更加稳定    
-###1.更新树莓派系统  

1 sudo  apt-get  update
2 sudo apt-get upgrade -y
-###2.安装python依赖环境

sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev
-###3.下载python3.7版本源码并解压

1 wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
2 tar zxvf Python-3.7.1.tgz
-###4.安装编译

1 cd Python-3.7.1
sudo ./configure && sudo make && sudo make install

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

创建虚拟环境
python -m venv pytorch
激活虚拟环境
source pytorch/bin/activate
适配numpy版本：
![image](https://github.com/user-attachments/assets/c7790cfc-bf1a-472e-98d2-790fa5f94fa3)




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

