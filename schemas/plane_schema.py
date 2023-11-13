from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class PlaneSchema(SchemaBaseModel):
    id: Optional[int] = None
    name: str
    pax: int
    engines: int

    class Config:
        from_attributes =True