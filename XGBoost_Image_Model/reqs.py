# Import Path from pathlib for file path operations  
from pathlib import Path  
# Import OpenCV for image processing 
import cv2
# Import Pipeline from sklearn for creating a ML pipeline  
from sklearn.pipeline import Pipeline  
# Import StandardScaler for feature scaling  
from sklearn.preprocessing import StandardScaler  
# Import XGBClassifier for the classification model  
from xgboost import XGBClassifier  
# Import numpy for numerical operations  
import numpy as np  # Import the required Python module
# Import pyplot from matplotlib for plotting  
from matplotlib import pyplot as plt  
# Import sklearn metrics for model evaluation  
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay  
# Import files from google.colab for file operations  
#from google.colab import files  

# Import ONNX runtime to run the inference
import onnxruntime as rt