import sys
default_path = "C:\\Users\\tev3ca\\Desktop\\FastAPI_Planes"
sys.path.append(default_path)

from fastapi import APIRouter
from api.v1.endpoints import plane

api_router = APIRouter()
api_router.include_router(plane.router, prefix='/planes', tags=['planes'])