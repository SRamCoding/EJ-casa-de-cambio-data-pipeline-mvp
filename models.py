from pydantic import BaseModel, Field
from datetime import datetime

class Transaction(BaseModel):
    user_id: str = Field(..., example="U123")
    source_currency: str = Field(..., example="USD")
    target_currency: str = Field(..., example="PEN")
    amount: float = Field(..., gt=0)
    rate: float = Field(..., gt=0)
    operation_type: str = Field(..., example="buy")
    timestamp: datetime = Field(default_factory=datetime.utcnow)