from pydantic import BaseModel 
from typing import List

class InferenceRequest(BaseModel): 
    text: str 

class LabelScore(BaseModel):
    label: str
    score: float

class InferenceResponse(BaseModel): 
    predictions: List[LabelScore]

