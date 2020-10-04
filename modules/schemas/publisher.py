from typing import List

from fastapi_utils.api_model import APIModel as APISchema


class PublisherSchema(APISchema):
    publisher_name: str
    params: List[dict]
