from dataclasses import dataclass


@dataclass
class ChatQuery:
    query: str

    @staticmethod
    def new(query) -> 'ChatQuery':
        return ChatQuery(query)
