from fastapi import APIRouter, Request, Response
from src.dto import ChatQueryDTO, OkDTO

router = APIRouter()


@router.get("/chat-rag")
async def get_response(
        request: ChatQueryDTO,
)-> OkDTO:
    aa = request
    return OkDTO(ok=True)
