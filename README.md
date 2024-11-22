&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hi👋, welcome to this tutorial on using the Raspberry Pi 4B to detect if a person has fallen! This project series will be divided into three parts, and today you will enter the first part, which focuses on how to prepare, run the code, and implement the core functionality.  

Next, we will walk you through the following steps 📜, diving deep into the source code and making it easy for you to get started with this project! Ready? Let’s get started 🚀!  
- 📝 Project Overview  
-✨ Features  
-🏗 Project Structure  
-🚀 Installation and Running  
-🔧 Usage Instructions  
-🔮 Next Episode Preview  
-Note: This project is a modification of the KNN 3D Human Skeleton Recognition project, demonstrating the complete tutorial on how to run it on the Raspberry Pi.  
  
# Raspberry Pi Fall Detection Project   
## Project Overview:  
This project uses the Raspberry Pi to first connect to the PC via SSH and transfer important files like VSCode. Then, after importing the code package into VSCode on the Raspberry Pi, the code is run in sequence. First, the train code is executed to extract and train human keypoints, and the keypoint positions are saved to a CSV file. Using this CSV file, we can test the code by uploading a video or opening the Raspberry Pi camera. By standing in front of the camera and performing actions, the system will detect if a fall has occurred. If a fall is detected, it will display "fall"; if no fall is detected and the keypoints are normal, it will display "normal."  

This article also provides detailed instructions on installing VSCode for programming, using FileZilla for file transfer, and using MobaXterm for remote connection to the Raspberry Pi.  

The article will summarize common error issues encountered and address Python version incompatibility problems.  


Features:  
-📏 Detect human keypoints.    
-🎉 Determine if a fall has occurred, improving the rescue rate.   
## Project Description Files:  
``` 


│── test.py # Camera testing code    
│── First_train.py # Step 1: Training file  
│── second_KNN.py # Step 2: Calling the KNN model  
│── Third_testing.py # Step 3: Open the camera for testing or upload a video  
│── GIF # Result display

  
```
### Prerequisites    
Software Dependencies：__Arduino IDE__、__VScode__ or __text__ ..
Hardware Requirements：__USB-C data cable__、__, Raspberry Pi 4B__, etc  
Library Dependencies：__opencv__、__pandas__  
### Arduino IDE Installation Steps 

## Python Version Compatibility Issue   
⚠️ Important: Do not uninstall the pre-installed Python version on Raspberry Pi OS, as it will cause system instability.  

Currently, the Python version provided in the Raspberry Pi system is the latest (Python 3.11). If compatibility issues arise, here are steps to reinstall and adjust the Python version  

Recommended Version:   
Installing Python 3.7 is suggested for better stability and compatibility with Raspberry Pi applications.    
    
-###1.Update the Raspberry Pi system     
``` 
1 sudo  apt-get  update  
2 sudo apt-get upgrade -y  
```
-###2.Install prerequisites  
```
sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev    
```
-###3.Download and install Python 3.7   
```
1 wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz  
2 tar zxvf Python-3.7.1.tgz  
```
-###4.Verify the Python installation   
```
1 cd Python-3.7.1    
2 sudo ./configure && sudo make && sudo make install  
```

5.Create a Symbolic Link  
After installing Python 3.7, we can check the Python version.     
```
1 python --version  
2 python3 --version   
```

##  
6.- ###Error Issues  
![image](https://github.com/user-attachments/assets/2adf55d0-fb75-4fff-b839-368261629fc8)  

  
```
sudo apt-get install libffi-dev  
```
Solution: “ModuleNotFoundError: No module named '_ctypes'”
![image](https://github.com/user-attachments/assets/eed2707f-cc15-48c6-9e33-b4a40a5d12de)  



7.Create a Symbolic Link  
After installing Python 3.7, you can check the Python version:  
```
1 python --version
2 python3 --version
```

8.To simplify usage, create a symbolic link for Python 3.7.1 pointing to the python command.   

Check the locations of the python and python3.7 commands:  
```
1 which python
2 which python3
```

9.Create the symbolic link:   
```
1 sudo mv /usr/bin/python /usr/bin/python2.7.13
2 sudo ln -s /usr/local/bin/python3 /usr/bin/python
```

10.Test the Installation   
```
1 ls -al /usr/local/bin/python*
2 python --version
```


![image](https://github.com/user-attachments/assets/44ec15a4-8126-4484-8635-ce7a358f8dbc)  

11.Create a Virtual Environment  
```
python -m venv pytorch  
```

Activate the virtual environment:    
```
source pytorch/bin/activate  
```

Adapting the numpy Version：   
![image](https://github.com/user-attachments/assets/c7790cfc-bf1a-472e-98d2-790fa5f94fa3)  


## Installation and Execution  
1.Steps to Install OpenCV     
Download opencv-python 和 opencv-contrib-python    
opencv-python地址：piwheels - opencv-python   https://www.piwheels.org/project/opencv-python/   
opencv-contrib-python地址：piwheels - opencv-contrib-python   https://www.piwheels.org/project/opencv-contrib-python/   

2.Check the suitable OpenCV version for your Raspberry Pi using the following command:   
![image](https://github.com/user-attachments/assets/8986a20b-48bf-4dec-ad9c-06245554ee95)  

![image](https://github.com/user-attachments/assets/4bb34404-9fe2-482c-b59d-7ed8cfcb0b37)  

![image](https://github.com/user-attachments/assets/49634ccd-5037-4766-9f2b-8ed612ff9bf5)  


3.Troubleshooting Installation Errors:    
![image](https://github.com/user-attachments/assets/43b705ff-4113-46d1-94aa-6547f1a8850b)  

4.To install the package on the desktop, navigate as follows:    
```
cd Desktop  
ls  
pip3 install <name>
```
![image](https://github.com/user-attachments/assets/00986329-4855-405b-ac91-54aa601aaedc)  


5.Install numpy Dependency   
```
sudo apt-get install python3-h5py  
pip3 install numpy （Tab）  

```
![image](https://github.com/user-attachments/assets/d544cdb9-672e-4c3c-91ad-aa330b484f04)  
|
### Dependencies  
Install Other OpenCV Dependencies：    
```
sudo apt-get install libhdf5-dev  
sudo apt-get install libatlas-base-dev   
sudo apt-get install libjasper-dev  
sudo apt-get install libqt4-test  
sudo apt-get install libqtgui4   
sudo apt-get update
```
When the confirmation screen appears, press Enter directly without typing "y":    
![image](https://github.com/user-attachments/assets/80ab771f-c615-48c5-980e-31cc855b6c60)  

Following the above steps, OpenCV should be successfully installed:   

![image](https://github.com/user-attachments/assets/5e7a7468-28f1-4540-abeb-a2b7ac895e7a)  

Install vscode:  
![image](https://github.com/user-attachments/assets/6b45c5e3-785c-4a4c-93c1-855bb8b8bec2)  


![image](https://github.com/user-attachments/assets/9df9bad7-ef5e-4db8-bf7c-22ed2fb9c107)  




## How to Contact the Maintainer or Developer   
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

__Source Code Adapted __
[KNN-Fall-Detection-main]([https://github.com/Sarah-C/M5StickC_Plus_Slot_Machine](https://github.com/Code-Deer/KNN-Fall-Detection/blob/main/README.md))

