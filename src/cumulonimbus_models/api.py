from pydantic import BaseModel, Field


class APIRequest(BaseModel):
    path: str = Field(exclude=True)
    format: str = Field(exclude=True)

    def get_url(self, base_url: str) -> str:
        return f'{base_url}/{self.format}'

