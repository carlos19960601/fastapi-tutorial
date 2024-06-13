from fastapi import APIRouter

router = APIRouter(
    prefix="/add",
    tags=["addition"]
)


@router.get('/numbers')
def add_numbers():
    return { "message": "we are adding numbers"}

@router.get('/strings')
def add_strings():
    return { "message": "we are adding strings"}
