import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image


model = load_model("garbage_classification_model.h5")


class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']  


def classify(img):
    img = img.resize((150, 150))  
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    class_label = class_names[class_index]
    confidence = prediction[0][class_index]
    
    return f"Predicted: {class_label} (Confidence: {confidence:.2f})"

# 4. Gradio Interface
interface = gr.Interface(fn=classify, 
                         inputs=gr.Image(type="pil"), 
                         outputs="text",
                         title="Garbage Classification App")

# 5. Launch
interface.launch()
