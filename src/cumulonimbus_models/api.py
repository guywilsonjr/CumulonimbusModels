from typing import ClassVar

from pydantic import BaseModel


class APIRequest(BaseModel):
    path: ClassVar[str]
    format: ClassVar[str]

    @classmethod
    def get_url(cls, base_url: str, **kwargs) -> str:
        return f'{base_url}{cls.format.format(**kwargs)}'

