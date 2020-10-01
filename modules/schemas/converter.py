
from fastapi_utils.api_model import APIModel as APISchema


class ConverterSchema(APISchema):
    source_format: str
    target_format: str
    content: str
