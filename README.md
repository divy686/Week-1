#  Garbage Classification Project

##  Project Overview
This project uses a Convolutional Neural Network (CNN) to classify garbage images into 6 categories:  
**Cardboard, Glass, Metal, Paper, Plastic, Trash**  
The goal is to assist in automating waste segregation using machine learning.

---

##  Dataset
**Kaggle Dataset Link:**  
[Trash Type Image Dataset – Kaggle](https://www.kaggle.com/datasets/farzadnekouei/trash-type-image-dataset)

---

##  Model File (.h5)
- After training the CNN, the model was saved as `garbage_classification_model.h5`.
- This file is loaded during web app deployment using `load_model()`.
- Due to large size, this file may not be uploaded to GitHub.
-  **If needed, you can access it from Google Drive or provide the file on request.**
  
[Download Trained Model (.h5)](https://drive.google.com/file/d/1BYKXTaiysGncSXobx2O17VAwCKTIavqo/view?usp=sharing) 

---

##  Week 1 – Data Loading, Preprocessing & Model Training

- Loaded dataset and visualized samples
- Applied image augmentation using `ImageDataGenerator`
- Built CNN model using `Keras` with Conv2D, MaxPooling, Flatten, Dense layers
- Trained model on training data and saved it as `garbage_classification_model.h5`

---

##  Week 2 – Model Evaluation & Testing

- Evaluated accuracy and loss on validation data
- Plotted training vs validation accuracy & loss graphs
- Generated classification report and confusion matrix
- Tested model on custom sample images using prediction logic

---

##  Week 3 – Web App Deployment using Gradio

- Created a simple web interface using **Gradio**
- Saved trained model and loaded it using `load_model()`
- Processed uploaded image and predicted class label with confidence
- Created an `app.py` file for deployment

###  Steps to Run app.py


## Step 1: Move to the project directory
cd path/to/garbage_classification_project

## Step 2: Activate environment (if any)
conda activate garbage-env

## Step 3: Run the app
python app.py
