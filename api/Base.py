from fastapi import APIRouter
router = APIRouter()


@router.get('/')
async def home(num: int):

    return num
