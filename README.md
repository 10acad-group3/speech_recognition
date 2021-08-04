# African language Speech Recognition

In this project we are going to build deep learning model  to process and convert African language (Amharic) speech/voice to text format.

## Table of Content
- [Introduction](#introduction)
- [Install](#instalation)
- [Data](#data)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Technologies used](#technologies-used)

### Introduction
The World Food Program wants to deploy an intelligent form that collects nutritional information of food bought and sold at markets in three different countries in Africa - Ethiopia and Kenya.  

The design of this intelligent form requires selected people to install an app on their mobile phone, and whenever they buy food, they use their voice to activate the app to register the list of items they just bought in their own language. The intelligent systems in the app are expected to live to transcribe the speech-to-text and organize the information in an easy-to-process way in a database. 

 Our responsibility is to build a deep learning model that is capable of transcribing a speech to text. The model we produce should be accurate and is robust against background noise.

### Instalation
- **Install Required Python Moduls**
``` 
git clone https://github.com/10acad-group3/speech_recognition
cd speech_recognition
pip install -r requirements.txt
```

- **Jupiter Notebook**
```
cd notebooks
jupyter notebook
```

- **Model Training ui (not-implimented)**
```
mlflow ui
```

- **Dashboard (not-implimented)**
```
streamlit run app.py
```

### Data
Description about the types of data we have in this folder, their type and purpose.

### Notebooks

- ```1.0 preprocessing.ipynb``` : explain 
- ```2.0 acoustic_modeling.ipynb```: explain
- ```3.0 speech_recognition.ipynb```: explain

### Scripts
- ```clean_audio.py ``` : explain
- ```config.py ```: explian
- ```file_handler.py ```: explain
- ```log.py```: explain
- ```script.py```: explain

### Technologies used
- [DVC](https://dvc.org/) : For Data Storage
- [MLflow](https://www.mlflow.org/): Model training and visualization
- [CML](https://github.com/iterative/cml): Showing model result and usefull information during pull requests
- [Streamlit](https://streamlit.io/): Display Web interface and dashboard


## Contributors
1. [Natnael Sisay](https://github.com/NatnaelSisay)
2. [Elias Andualem](https://github.com/eandualem)
3. [Ethani Caphace](https://github.com/Caphace-Ethan)
4. [Behigu Gizachew](https://github.com)
5. [Michael Tekle Woji](https://github.com/maxi1571)
6. [Fumbani Banda](https://github.com/deadex-ng)
