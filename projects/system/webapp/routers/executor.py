from fastapi import APIRouter, Request, Response
from src.dto import ChatQueryDTO, OkDTO

router = APIRouter()


@router.get("/chat-rag")
async def get_response(
        request: ChatQueryDTO,
)-> OkDTO:
    aa = request
    return OkDTO(ok=True)


@router.get("/chat-rag-llamaindex")
async def get_llama_index_response(
        request: ChatQueryDTO,
)-> OkDTO:
    aa = request
    return OkDTO(ok=True)


@router.get("/langchain-chat")
async def get_langchain_chat_response(
        request: ChatQueryDTO,
) -> OkDTO:
    aa = request
    return OkDTO(ok=True)

