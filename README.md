<img src="https://capsule-render.vercel.app/api?type=waving&color=ab51ef&height=150&section=header&text=AI_Model&fontSize=50&fontColor=ffffff" />


# **목차**
-[개요](#개요)
  
-[INPUT](#INPUT)

-[이상치&결측치](#이상치&결측치)

-[df.corr()](#df.corr())

-[Model](#Model)

-[MAE](#MAE)

## **개요**
- ✏️**프로젝트 주제**✏️ : Pytorch만 사용하여 배수지의 유량 적산차를 예측
  
<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/85af91c5-31c3-4c85-a4e2-2f7a3d6e3b5a" width="400px">

- 📆**프로젝트 지속기간**📆 : 2023.05.01~2023.05.31
  
- 💻**개발환경 및 개발언어**💻 :

  ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

  
## **INPUT**

-[인구](#인구)

-[날씨](#날씨)

-[cos_24_1](#cos_24_1)

-[미니게임3](#미니게임3)




### **인구** : 김천시 인구 변화

<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/e155f3ba-aee3-4f57-bbe8-6d97c6537c56" width="400px">

### **날씨** : 기온 , 강수량 , 습도

<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/2a2f9da1-a4f1-4004-bf66-00b07583bf2b
" width="400px">

### **cos_24_1** : 시간에 대한 코사인 값

- 특정 시간에 대한 주기성
  
- 시간에 따른 변동성을 나타내는 특징이므로, 시계열 데이터의 적산차 예측에 사용

<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/d9e126f5-f07d-4dc8-a201-c92f5937d823
" width="400px">

## **이상치&결측치**
- 이상치 처리 : amount(적산차) 값이 완전 동떨어져 있는 값을 지우고, 그 전 값으로 대체
- 결측치 처리 : 시간열 데이터이므로 이전 값으로 대체

##**df.corr()** : 데이터프레임의 각 열간의 상관 관계를 계산하기 위해 사용되는 메소드

<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/c1ac5cd4-6d60-45c7-b8f9-9c44629c57c6" width="400px">

## **Model** : LSTM 모델

<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/5ca7c780-735c-4a84-8ba7-2dc3c3b80857" width="400px">

## **MAE*
- predicted 열 : 예측 데이터
- actual 열 : 실제 데이터
- difference : 예측 데이터와 실제 데이터의 차이
 
<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/bb8440dc-5320-4ea2-baef-8293f5f39ac5" width="400px">

- MAE : 95
  
<img src = "https://github.com/SeoooooNyeong/LSTM_AI_Model/assets/113419106/f442c75a-5fe5-4bf1-b02c-1e79b1ec3bfa" width="400px">

