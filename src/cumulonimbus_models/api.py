import re
from typing import ClassVar, Set

from pydantic import BaseModel

from cumulonimbus_models.settings import BASE_URL




class APIRequest(BaseModel):
    route_format: ClassVar[str] = '/'

    @classmethod
    def format_args(cls) -> Set[str]:
        arg_regex = r'{[a-z][a-z_]*[a-z]}'
        arg_pattern = re.compile(arg_regex)
        arg_matches = arg_pattern.findall(cls.route_format)
        return {arg[1:-1] for arg in arg_matches}

    @classmethod
    def route(cls) -> str:
        route = cls.route_format
        for arg in cls.format_args():
            route = route.replace(f'{{{arg}}}', f'<{arg}>')
        return route

    @classmethod
    def get_url(cls, base_url: str = BASE_URL, **kwargs) -> str:
        format_args = cls.format_args()
        for arg, val in kwargs.items():
            if arg not in format_args:
                raise ValueError(f'Invalid argument: {arg}')
        found_args = set(kwargs.keys())
        missing_args = format_args - found_args
        if missing_args:
            raise ValueError(f'Missing arguments: {missing_args}')
        return f'{base_url}{cls.route_format.format(**kwargs)}'

