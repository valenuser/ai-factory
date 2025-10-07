from fastapi import APIRouter

router = APIRouter()


# Health Check Endpoint
@router.get("/")
def health_check():
    return {"status": "🚀 api_factory is running "}
