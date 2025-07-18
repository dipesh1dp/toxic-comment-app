from fastapi import FastAPI 
from app.model import load_model, predict_labels 
from app.schemas import InferenceRequest, InferenceResponse

app = FastAPI()
tokenizer, model, device = load_model()

@app.get("/")
def root():
    return {"message": "BERT Toxic Comment Classifier is running!"} 
         
@app.post("/predict", 
          response_model=InferenceResponse)
def predict(text_input: InferenceRequest): 
    results, scores = predict_labels(text=text_input.text, 
                            tokenizer=tokenizer, 
                            model=model, 
                            device=device) 
    return InferenceResponse(predictions=results) 



