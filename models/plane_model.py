import sys
default_path = "C:\\Users\\tev3ca\\Desktop\\FastAPI_Planes"
sys.path.append(default_path)

from core.configs import settings
from sqlalchemy import Column, Integer, String

class PlaneModel(settings.DBBaseModel):
    __tablename__ = 'planes'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50))
    pax: int = Column(Integer)
    engines: int = Column(Integer)