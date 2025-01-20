# webapp/app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from webapp.routers import executor


def create_app() -> FastAPI:
    """FastAPI 인스턴스를 생성

    router를 생성하여 FastAPI 인스턴스에 등록

    Returns:
        FastAPI 인스턴스
    """
    app = FastAPI(
        title="Chat RAG",
        description="Chat RAG"
    )

    app.include_router(
        executor.router,
        tags=['executor']
    )

    return app

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()
