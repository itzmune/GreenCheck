import numpy as np
from tensorflow.keras.preprocessing import image
import cv2

def preprocess_image(img_path, target_size=(224, 224)):
    """
    Loads and preprocesses an image from disk for model prediction.

    Parameters:
        img_path (str): Path to the image file.
        target_size (tuple): Image size for the model input (default: 224x224).

    Returns:
        np.ndarray: Preprocessed image array ready for model prediction.
    """
    try:
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize to [0, 1]
        return img_array
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")

def preprocess_opencv(img_path, target_size=(224, 224)):
    """
    Alternative preprocessing using OpenCV.

    Parameters:
        img_path (str): Path to the image file.
        target_size (tuple): Size to resize the image to.

    Returns:
        np.ndarray: Normalized image suitable for input to a model.
    """
    try:
        img = cv2.imread(img_path)
        img = cv2.resize(img, target_size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        return img
    except Exception as e:
        raise ValueError(f"OpenCV failed to process image: {e}")
