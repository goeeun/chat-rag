from pydantic import BaseModel, Field
from src.domain import ChatQuery


class ChatQueryDTO(BaseModel):
    """
    사용자 메세지를 포함하는 데이터 전송 객체
    """
    query: str = Field(description="사용자 메세지", examples=['안녕하세요'])

    def to_domain(self) -> ChatQuery:
        return ChatQuery.new(
            query=self.query
        )

class OkDTO(BaseModel):
    """
    API 정상 수행시 반환되는 DTO
    """
    ok: bool