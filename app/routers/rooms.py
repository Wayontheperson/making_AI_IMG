from fastapi import APIRouter

router = APIRouter()


@router.get("/rooms/")
async def get_rooms():
    return
