from typing import ClassVar

from pydantic import BaseModel, Field


class APIRequest(BaseModel):
    path: ClassVar[str] = Field(exclude=True)
    format: ClassVar[str] = Field(exclude=True, const=True)

    def get_url(self, base_url: str) -> str:
        return f'{base_url}/{self.path}'

