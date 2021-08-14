# African language Speech Recognition

In this project we are going to build deep learning model to process and convert African language (Amharic) speech/voice to text format.

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
This project is made on the fourth week of 10Academy Machine Learning training session.

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

The folder is being tarcked with DVC and the files are only shown after cloning and setting up locally. The sub-folder `AMHARIC` contain `training` and `testing` files for our model. Both files contain similar file structure.

- **`wav/`** : a folder containing all audio files
- **`text`** : file contining the metadata (audio file name and cropsonding transcription)
- **`spk2utt`**, **`trsTest.txt`**, **`utt2spk`**, **`wav.scp`** : this are files provided with the dataset, Currently they don't have a purpose but could be used for future analysis.

### Notebooks

- `1.0 preprocessing.ipynb` : Notebook file showing **metada-generation**, **new features**, **Data exploration**, **Removing outliers**, **Clean audio** and **clean text **
- `1.0 acoustic_modeling_v2.ipynb`: Notebook file similar to `1.0 preprocessing.ipynb`, but contain more analysis on audio visualization and text data anlysis
- `2.0 outliers.ipynb`: visualize the effect of ourlier removal on features of the dataset. finally save the outlier cleaned file.
- `3.0 speech_recognition.ipynb`: Notebook file, showing how to Tokenize, Augument and Generate data, from outlier cleaned data.
- `audio_visualization` : Google colab file showing how to visualize audio file using audio wave and spectogram.
- `4.0 acoustic_modeling`: on progress ...

### Scripts

- **`audio_vis.py `** : Helper class for visualizing and playing audio files
- **`clean_audio.py `** : Helper class for cleaning audio files
- **`config.py `**: Project configration and file paths
- **`file_handler.py `**: Helper class for reading files
- **`log.py`**: Helper class for logging
- **`script.py`**: Utility functions

### Technologies used

- [DVC](https://dvc.org/) : Remote Data Storage
- [MLflow](https://www.mlflow.org/): Model training and visualization
- [CML](https://github.com/iterative/cml): Display Model result and usefull information during pull requests
- [Streamlit](https://streamlit.io/): Display Web interface and dashboard

## Contributors

1. [Natnael Sisay](https://github.com/NatnaelSisay)
2. [Elias Andualem](https://github.com/eandualem)
3. [Ethani Caphace](https://github.com/Caphace-Ethan)
4. [Behigu Gizachew](https://github.com/behigu)
5. [Michael Tekle Woji](https://github.com/maxi1571)
6. [Fumbani Banda](https://github.com/deadex-ng)
7. [Christian ZANOU](https://github.com/Zchristian955)
8. [Robert Ssebudandi](https://github.com/rssebudandi)
