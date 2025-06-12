from pydantic import BaseModel, Field
from typing import List, Any

class Iris(BaseModel):
    data: List[List[float]] = Field(..., min_length=1)

class IrisPredictionResponse(BaseModel):
    prediction: List[int]
    probability: List[Any]
    log_probability: List[Any]