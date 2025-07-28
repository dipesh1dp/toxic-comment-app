<p align="center">
  <img src="streamlit_frontend\assets\header.png" alt="App Header" width="200"/>
</p>

# 💀 Toxic Comment Classifier

A Streamlit app that detects toxic, insulting, or abusive language in user-generated text.  
The app uses a fine-tuned [`bert-base-uncased`](https://huggingface.co/bert-base-uncased) model for **multilabel toxic comment classification** trained on the Jigsaw Toxic Comment dataset.

--- 

## 🛑 LIVE  Demo

Try the app online at:  
👉 [Hugging Face Space](https://huggingface.co/spaces/dipeshpandit/bert-toxic-comment)

---

## 💡Quick example on how it works
Enter any comment in the input box and the model predicts which of the following toxic labels apply:

| Label           | Description               |
|-----------------|---------------------------|
| `toxic`         | General toxicity          |
| `severe_toxic`  | Severe toxicity or abuse  |
| `obscene`       | Profanity or obscenity    |
| `threat`        | Threatening language      |
| `insult`        | Insult or hate speech     |
| `identity_hate` | Hate based on identity    |

### Input
<p align="left">
  <img src="streamlit_frontend\assets\input.png" alt="App Header" width="600"/>
</p>

### Output
<p align="left">
  <img src="streamlit_frontend\assets\output.png" alt="App Header" width="600"/>
</p>


## ℹ️ About the Model

- **Model:** [`dipeshpandit/bert-toxic`](https://huggingface.co/dipeshpandit/bert-toxic)  
- **Base model:** [`bert-base-uncased`](https://huggingface.co/bert-base-uncased)  
- Fine-tuned for multilabel classification with **6 toxic categories**  
- Label thresholds tuned on validation set to optimize F1 scores  
- Uses sigmoid outputs with label-specific thresholds for prediction

## How to run locally?
1. Clone the Repository
```bash
git clone https://github.com/dipesh1dp/toxic-comment-app.git
cd bert-toxic-comment-classifier
```
2. Create and Activate a Virtual Environment (Optional but Recommended)
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Set up and run FastAPI backend locally
```bash
# Install FastAPI requirements
pip install -r requirements.txt
```
```bash
# Run the FastAPI server (e.g., on port 8000)
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
Your backend will now be running at:
http://127.0.0.1:8000

You can also see the docs at:
http://127.0.0.1:8000/docs
4. Set up and run Streamlit frontend
```bash
# Install frontend dependencies
cd streamlit_frontend
pip install -r requirements.txt
```
Run the Streamlit app (by default runs on port 8501)
```bash
streamlit run streamlit_ui.py
```
The app will start on http://localhost:8501 in your default browser.

Communication between frontend & backend
Make sure the Streamlit app (in streamlit_ui.py) sends requests to:
```python
FASTAPI_URL = "http://127.0.0.1:8000"  # or your local backend URL
```
##  Optional: Run with Docker
1. Build the Docker Image
For GPU (CUDA 12.1) (NVIDIA RTX or similar):
```bash
# From project root
docker build -t toxic-comment-api  --build-arg BASE_IMAGE=pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime .
```
For CPU-only (e.g., HuggingFace Spaces, CPUs): 
```bash
# From project root
docker build -t toxic-comment-api \
  --build-arg BASE_IMAGE=pytorch/pytorch:2.2.2-cpu \
  .
```
2. Run the app
Once built, start the FastAPI server with
```bash
docker run -d -p 8000:8000 toxic-comment-api
```
Visit: http://localhost:8000/docs to try the API via Swagger UI.


## 📈 Performance Metrics 
### Validation Set Thresholds & F1 Scores

| Label           | Threshold | F1 Score |
|-----------------|-----------|----------|
| `toxic`         | 0.69      | 0.8264   |
| `severe_toxic`  | 0.44      | 0.5238   |
| `obscene`       | 0.60      | 0.8321   |
| `threat`        | 0.47      | 0.6316   |
| `insult`        | 0.32      | 0.7713   |
| `identity_hate` | 0.55      | 0.6280   |


### Test Set Performance Summary

| Metric              | Score  |
|---------------------|--------|
| F1 Score (Micro)    | 0.6740 |
| F1 Score (Macro)    | 0.6089 |
| Precision (Micro)   | 0.5857 |
| Recall (Micro)      | 0.7938 |
| Precision (Macro)   | 0.5426 |
| Recall (Macro)      | 0.7092 |

> For more details on training, see the [Fine-tuning Report](reports\fine-tune-report.md)

## 📁 Project Structure

```plaintext
toxic-comment-app/
├── app/
|    ├── __init__.py                       
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
|
├── finetune-notebook/
|   ├──bert-toxic-finetune.ipynb 
|
├── reports/
|   ├──fine-tune-report.md         
│
├── streamlit_frontend/
│   ├── streamlit_ui.py
│   ├── assets/
│   └── requirements.txt         ← For Streamlit only
│
├── requirements.txt             ← For FastAPI only
├── Dockerfile                   ← Builds FastAPI container
├── .gitignore
├── README.md

```

## 🛠️ Built With

- 🤗 [Transformers](https://github.com/huggingface/transformers)  
- ⚡ [PyTorch](https://pytorch.org/)  
- ⚙️ [FastAPI](https://fastapi.tiangolo.com/)
- 🌐 [Streamlit](https://streamlit.io/)  
- 💬 [Jigsaw Toxic Comment Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)  


## 👤 Author

Developed by Dipesh Pandit. 
- [LinekedIn](https://www.linkedin.com/in/dipesh1dp/)
- [HuggingFace](https://huggingface.co/dipeshpandit)


## 📄 License
This project is licensed under the **Apache License 2.0.**
