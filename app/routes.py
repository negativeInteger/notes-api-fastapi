from fastapi import APIRouter

# create a router instance
router = APIRouter()

@router.get('/ping')
def test():
    return {"message": "HELLO EVERYTHHING WORKING"}