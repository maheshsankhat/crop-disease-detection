# Professional app.py for Crop Disease Detection
import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

# Page Config
st.set_page_config(
    page_title="Crop Disease Detection",
    page_icon="🌿",
    layout="centered"
)

# Load Model
model = tf.keras.models.load_model("trained_model.keras")

# Class Names
class_names = [
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato_Target_Spot',
    'Tomato_Tomato_YellowLeaf_Curl_Virus',
    'Tomato_Tomato_mosaic_virus',
    'Tomato_healthy'
]

# Title
st.title("🌿 AI Crop Disease Detection")

st.markdown(
    """
    Upload a plant leaf image and the AI model will detect:
    - Plant Disease
    - Healthy/Diseased Status
    - Prediction Confidence
    """
)


# Upload Image
uploaded_file = st.file_uploader(
    "📤 Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open Image
    img = Image.open(uploaded_file)

    # Display Image
    st.image(img, caption="Uploaded Leaf Image", use_container_width=True)

    # Resize Image
    img = img.resize((224, 224))

    # Convert to Array
    img_array = image.img_to_array(img)

    # Expand Dimensions
    img_array = np.expand_dims(img_array, axis=0)

    # Normalize
    img_array = img_array / 255.0

    # Prediction
    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = np.max(prediction) * 100

    # Clean Name
    clean_name = predicted_class.replace("___", " - ").replace("_", " ")

    st.success(f"✅ Prediction: {clean_name}")

    st.info(f"📊 Confidence: {confidence:.2f}%")

    # Healthy or Diseased
    if "healthy" in predicted_class.lower():
        st.success("🌱 Plant Status: Healthy")
    else:
        st.error("⚠️ Plant Status: Diseased")

# Footer
st.markdown("---")
st.caption("Developed using TensorFlow, MobileNetV2, and Streamlit")