# Garbage Classification using CNN - Week 1

This is my Week 1 submission for the **Garbage Classification Project** under the **i-Shell in AI internship by Edunet Foundation**.

---

## Objective

To build a Convolutional Neural Network (CNN) model that classifies garbage images into 6 categories:
- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

---

## Dataset Used

- **Source:** [Kaggle - Trash Type Image Dataset](https://www.kaggle.com/datasets/farzadnekouei/trash-type-image-dataset)
- The dataset was downloaded, extracted, and used for model training.
- Images were resized to **150x150 pixels** for processing.

---

## Work Done in Week 1

- Downloaded & prepared the dataset
- Applied image preprocessing using `ImageDataGenerator`
- Built a basic CNN model using TensorFlow/Keras
- Trained the model for 5 epochs
- Plotted **Training & Validation Accuracy/Loss** graphs

---

## Model Architecture

- Conv2D → MaxPooling2D  
- Conv2D → MaxPooling2D  
- Flatten  
- Dense (ReLU)  
- Dense (Softmax - 6 classes)

---

## Output Graphs

The following graphs were plotted after training:

- Training vs Validation Accuracy
- Training vs Validation Loss

---

## Tools Used

- Python
- Jupyter Notebook
- TensorFlow / Keras
- Matplotlib
- NumPy

---

##  Status

-  Dataset Loaded & Preprocessed  
-  CNN Model Built  
-  Trained on 6 Classes  
-  Accuracy & Loss Graphed  




