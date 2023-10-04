from fastapi import FastAPI, HTTPException, status, Response
from models import Plane

planes = {
    1: {
        "nome": "Airbus A320",
        "pax": 186,
        "engines": 2
    },
    2: {
        "nome": "Boeing 737",
        "pax": 149,
        "engines": 2
    },
    3: {
        "nome": "Airbus A350",
        "pax": 366,
        "engines": 2
    },
    4: {
        "nome": "Cessna 152",
        "pax": 2,
        "engines": 1
    },
    5: {
        "nome": "Airbus A380",
        "pax": 516,
        "engines": 4
    },
    6: {
        "nome": "Boeing 747",
        "pax": 410,
        "engines": 4
    },
    7: {
        "nome": "Boeing 787",
        "pax": 335,
        "engines": 2
    },
    8: {
        "nome": "Embraer E195",
        "pax": 114,
        "engines": 2
    },
    8: {
        "nome": "ATR 72-600",
        "pax": 78,
        "engines": 2
    },
}

app = FastAPI()

@app.get('/planes')
async def get_planes():
    return planes

@app.get('/planes/{plane_id}')
async def get_plane(plane_id : int):
    try:
        plane = planes[plane_id]
        plane.update({"id" : plane_id})
        return plane
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Plane not found')
    
@app.post('/planes', status_code=status.HTTP_201_CREATED)
async def post_plane(plane: Plane):
    last_key = sorted(planes.keys())[-1]
    next_key = last_key + 1
    plane.id = next_key
    planes[next_key] = plane
    return plane

@app.put('/planes/{plane_id}')
async def put_plane(plane_id : int, plane : Plane):
    if plane_id in planes:
        planes[plane_id] = plane
        return plane
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This plane doesn't exist")
    
@app.delete('/planes/{plane_id}')
async def delete_plane(plane_id : int):
    if plane_id in planes:
        del planes[plane_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This plane doesn't exist")
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)