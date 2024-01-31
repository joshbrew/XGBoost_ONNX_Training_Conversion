## ONNX XGBoost Jupyter Notebook

This XGBoost model is design to classify images, labeled by folder. Open Image_XGBoost_Training.ipynb in your preferred notebook environment (we use plain VSCode) and follow the instructions to install dependencies. You may also find the model hosted on Google Colab [here](https://colab.research.google.com/drive/1rPobgC9eD59c4nIeJK2LpJPMhzNRXCuP?usp=sharing)

After, you can use the Image_XGBoost_Testing.ipynb to make sure it works, and otherwise you may export the .onnx model to your applications generically.

Follow along in the Notebook otherwise to understand what is going on in the program.

## Project Installation

This project relies on the following major dependencies:

- [**Python**](https://www.python.org/downloads/): The primary programming language used. We're using the latest Python3
- [**Jupyter Notebook**](https://jupyter.org/install): Handles the .ipynb format file execution.
- [**VSCode**](https://code.visualstudio.com/): Code editor and simple notebook environment.
- **Libraries**: 
  - `opencv-python`: For image processing and computer vision tasks.
  - `scikit-learn`: For machine learning algorithms and data preprocessing.
  - `xgboost`: An efficient implementation of gradient boosting framework.
  - `numpy`: Essential for numerical operations.
  - `matplotlib`: For plotting and visualization of data.
  - `onnxconverter-common`: Common utilities for ONNX model conversion.
  - `onnxmltools`: Tools for converting machine learning models to ONNX format.
  - `skl2onnx`: Specifically for converting scikit-learn models to ONNX format.
  - `google.colab`: Google Colaboratory ONLY - Python notebook format.

Easy Jupyter Notebook installation (with Python3 already installed):
- Open this file in [VSCode](https://code.visualstudio.com/) and use extensions (VSCode will prompt you) to configure and run the python and jupyter env.

### Install Dependencies:

#### In your command prompt with Python 3 installed, type:
`pip install -r requirements.txt`

## Data Download and Extraction:

### Download the dataset and unzip it (linux example calls)
`wget https://storage.googleapis.com/fishazam-sample-dataset/fillet_dataset_small.zip`

`unzip fillet_dataset_small.zip -d ./content`