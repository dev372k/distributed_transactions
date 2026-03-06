from pydantic import BaseModel
from typing import List, Optional

class Operation(BaseModel):
    type: str
    key: str
    value: Optional[int] = None


class Transaction(BaseModel):
    id: str
    timestamp: int
    operations: List[Operation]