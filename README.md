# study_timer 공부해보자구

### 서비스 설명

본 서비스는 웹캠에서 사용자의 공부하는 모습을 받아와 출력한다. 또 웹캠에서 받아온 영상을 입력으로 순수한 공부시간만을 출력한다. 사용자가 목표시간을 설정할 수 있게 하고 목표시간과 순수한 공부시간을 비교하여 그 통계를 시각적으로 표시한다. 여기서 순수한 공부시간이란 딴짓을 하지 않고 오롯이 공부에 집중한 시간을 말한다.

 공부시간 측정 알고리즘이란 웹캠에서 사용자의 공부하는 모습을 받아와 순수한 공부시간만을 출력하는 것이다. 작동방식은 다음과 같다. 먼저 사용자의 공부하는 모습을 영상으로 받아와 일정한 시간마다 영상을 캡처한다. 그 후 캡처된 사진에서 핸드폰이 보이거나 펜은 있지만 손은 존재하지 않을 시 사용자가 딴짓을 하고 있다고 간주한다. 순수 공부시간은 현재 측정된 시간에서 딴짓하는 시간을 측정하여 뺀 값을 갱신하여 표시한다. 

### 설치방법

 - 용량이 큰 파일은 git에 올리지 않았다.
 - yolo와 roboflow의 설치는 google colab에서 진행하였다.
 - 모델 학습은 google colab에서 진행하였다.

model 설치
 ```
 pip install opencv-python
 pip install numpy
 pip install torch
 pip install tensorflow
 pip install roboflow 
 git clone https://github.com/ultralytics/yolov5.git
 pip install -r requirements.txt
 ```
웹 데이터 크롤링
 ```
 pip install selenium
 pip install request
 ```
서버 설치
 ```
 pip install django
 pip install django-bootstrap4
 ```
 
### 의존성

for model
 ```
 python==3.x
 opencv-python==4.6.0.66
 numpy==1.23.5
 torch==1.2.0
 torchvision==0.4.0a0+6b959ee
 tensorflow==2.10.1
 yolov==https://github.com/ultralytics/yolov5.git
 glob
 yaml
 ```
 
for 웹 데이터 크롤링
 ```
 selenium==3.8.1
 requests==2.28.1
 ChromeDriver
 ```
 
for server
 ```
 Django==4.1.4
 django-bootstrap4==22.3
 virtualenv==20.17.0
 ```
 
for web
 ```
node.js==18.9.0
Chart.js==2.4.0
html2canvas==1.4.1 
 ```

### 사용 데이터

구글 이미지 크롤링을 통해 이미지 파일들을 받고 roboflow를 통하여 dataset을 구성하였다.

### 실행 방법

서버 오픈
 ```
python manage.py runserver
 ```
 
 ![ezgif com-gif-maker](https://user-images.githubusercontent.com/49019187/206849937-56618a90-d061-40ae-b987-81c90016c7b4.gif)


### 사용 방법

![ezgif com-gif-maker](https://user-images.githubusercontent.com/49019187/206850211-2fa6e5d4-d0da-4226-abad-e8ffc55032b2.gif)
