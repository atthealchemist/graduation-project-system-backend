from typing import List

from fastapi_utils.api_model import APIModel as APISchema


class MigratorSchema(APISchema):
    migrator_name: str
    params: List[dict]
