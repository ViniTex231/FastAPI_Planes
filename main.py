import sys
default_path = "C:\\Users\\tev3ca\\Desktop\\FastAPI_Planes"
sys.path.append(default_path)

from fastapi import FastAPI
from core.configs import settings
from api.v1._api import api_router

app = FastAPI(title='Planes API')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)