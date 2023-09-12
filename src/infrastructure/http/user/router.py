from fastapi import APIRouter
router = APIRouter(prefix='/user', tags=['User'], redirect_slashes=False)
