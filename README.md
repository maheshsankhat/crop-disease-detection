# 🌱 Crop Disease Detection System

An AI-powered **Crop Disease Detection System** that identifies plant diseases from leaf images using **Deep Learning (CNN)**. The application provides fast and accurate disease prediction through an easy-to-use **Streamlit** web interface, helping farmers detect diseases at an early stage.

---

## 🚀 Features

* Upload crop leaf images
* Detect healthy and diseased leaves
* Deep Learning (CNN) based prediction
* Displays predicted disease name
* Shows confidence score
* Simple and responsive Streamlit interface
* Fast and accurate prediction
* Easy to deploy and use

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* Pandas
* Matplotlib
* Streamlit
* Pillow

---

## 📂 Project Structure

```text
Crop-Disease-Detection/
│
├── dataset/
├── models/
│   └── crop_disease_model.keras
├── app.py
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── assets/
```

---

## 📊 Dataset

The model is trained using the **PlantVillage Dataset**, which contains thousands of healthy and diseased crop leaf images across multiple crop categories.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/maheshsankhat/Crop-Disease-Detection.git
cd Crop-Disease-Detection
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your web browser.

---

## 🧠 Model Workflow

1. Upload a crop leaf image.
2. Resize and preprocess the image.
3. Pass the image to the trained CNN model.
4. Predict the disease.
5. Display the disease name and confidence score.

---

## 📈 Future Improvements

* Mobile Application
* Multi-language Support
* Disease Treatment Suggestions
* Fertilizer Recommendations
* Weather-based Disease Alerts
* Cloud Deployment
* Real-time Camera Detection

---


