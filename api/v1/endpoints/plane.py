import sys
default_path = "C:\\Users\\tev3ca\\Desktop\\FastAPI_Planes"
sys.path.append(default_path)

from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.plane_model import PlaneModel
from schemas.plane_schema import PlaneSchema
from core.deps import get_session

router = APIRouter()

#POST
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PlaneSchema)
async def post_plane(plane: PlaneSchema, db: AsyncSession = Depends(get_session)):
    new_plane = PlaneModel(id=0,
                           name=plane.name,
                           pax=plane.pax,
                           engines = plane.engines)
    db.add(new_plane)
    await db.commit()
    return new_plane


#GET PLANES
@router.get('/', response_model=List[PlaneSchema])
async def get_planes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlaneModel)
        result = await session.execute(query)
        planes = List[PlaneModel] = result.scalars().all()
        return planes
    

#GET PLANE
@router.get('/{plane_id}', response_model=PlaneSchema,
            status_code=status.HTTP_200_OK)
async def get_plane(plane_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlaneModel).filter(PlaneModel.id == plane_id)
        result = await session.execute(query)
        plane = result.scalar_one_or_none()
        if plane:
            return plane
        else: raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plane not found..."))    


#PUT
@router.put('/{plane_id}', response_model=PlaneSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_plane(plane_id: int, plane: PlaneSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlaneModel).filter(PlaneModel.id == plane_id)
        result = await session.execute(query)
        plane_up = result.scalar_one_or_none()
        if plane_up:
            plane_up.name = plane.name
            plane_up.pax = plane.pax
            plane_up.engines = plane.engines
            await session.commit()
            return plane_up
        else:
            raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plane not found..."))    

#DELETE PLANE
@router.delete('/{plane_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_plane(plane_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlaneModel).filter(PlaneModel.id == plane_id)
        result = await session.execute(query)
        plane_del = result.scalar_one_or_none()
        if plane_del:
            await session.delete(plane_del)
            await session.commit()
            return Response(status_code=status.HTTP_404_NOT_FOUND, detail="Plane not found...")