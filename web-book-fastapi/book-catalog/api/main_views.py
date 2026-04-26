from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_root(name: str = "World"):
    return {
        "message": f"Hello {name}",
        "docs": "/docs"
    }