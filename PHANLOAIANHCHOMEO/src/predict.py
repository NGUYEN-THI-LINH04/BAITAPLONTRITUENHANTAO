import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models/mobilenet_dog_cat.h5")

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = ["Mèo", "Chó"]  # cats=0, dogs=1

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)[0]
    class_index = np.argmax(preds)
    confidence = preds[class_index] * 100

    return CLASS_NAMES[class_index], round(confidence, 2)
