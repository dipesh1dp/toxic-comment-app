import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np 

# define label names
LABELS = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
# define optimal thresholds per label
optimal_thresholds = np.array([0.69, 0.44, 0.60, 0.47, 0.32, 0.55]) 


def load_model():
    # load model
    model_name = "dipeshpandit/bert-toxic"
    print(f"Loading model: {model_name}...")  
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    print(f"{model_name} has been successfully loaded")  


    # device agnostic code
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    return tokenizer, model, device

# Prediction function
def predict_labels(text, tokenizer, model, device):
    model.eval()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)

    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.sigmoid(logits).squeeze().cpu().numpy()

    preds = (probs >= optimal_thresholds).astype(int)

    results = []
    predicted_labels = []

    for label, prob, pred in zip(LABELS, probs, preds):
        results.append({"label": label, "score": round(float(prob), 2)})
        if pred:
            predicted_labels.append(label)

    return results, predicted_labels
