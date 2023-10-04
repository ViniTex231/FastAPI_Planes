from typing import Optional
from pydantic import BaseModel

class Plane(BaseModel):
    id: Optional[int] = None
    nome: str
    pax: int
    engines: int
