import streamlit as st
import requests
from PIL import Image

# Set up page config
st.set_page_config(page_title="Toxic Comment Classifier", layout="centered")

# Labels for display only
LABELS = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

# Base URL of your FastAPI backend
API_URL = "http://localhost:8000/predict" 

# Centered header image
header_image = Image.open("assets/header.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(header_image, width=200)

# App title and instructions
st.title("💀 Toxic Comment Classifier")
st.write("Detect toxicity in comments with a fine-tuned BERT model.")

st.markdown("---")

# Text input
user_input = st.text_area("Enter a comment:", height=100)

# Predict button
if st.button("🔍 Predict"):
    if not user_input.strip():
        st.warning("Please enter a comment.")
    else:
        with st.spinner("Analyzing..."):
            try:
                # Send POST request to FastAPI backend
                response = requests.post(API_URL, json={"text": user_input})
                if response.status_code == 200:
                    data = response.json()
                    predictions = data["predictions"]
                    scores = [item["score"] for item in predictions]
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
                    st.stop()
            except requests.exceptions.ConnectionError:
                st.error("Failed to connect to the backend. Is it running?")
                st.stop()

        # Thresholding (same as backend, mirrored here)
        thresholds = [0.69, 0.44, 0.60, 0.47, 0.32, 0.55]
        predicted_labels = [
            label for label, score, th in zip(LABELS, scores, thresholds) if score >= th
        ]

        st.success("Prediction complete!")

        st.markdown("### ☢️ Detected Toxic Labels")
        if predicted_labels:
            st.write(", ".join([f"`{label}`" for label in predicted_labels]))
        else:
            st.write("✔️ No toxic labels detected.")

        st.markdown("### 📊 Confidence Scores")
        for label, score in zip(LABELS, scores):
            st.write(f"**{label.capitalize()}**: `{round(score, 2)}`")
            st.progress(score)