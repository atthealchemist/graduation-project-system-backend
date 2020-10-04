import json
from pathlib import Path

from fastapi import APIRouter

from modules.publishers.manager import PublishManager
from modules.schemas.publisher import PublisherSchema

publisher = APIRouter()


@publisher.get('/publish/{publisher_name}/fields', tags=['publisher'])
def publisher_fields(publisher_name: str):
    schema_path = Path() / 'modules' / 'publishers' / 'schemas' / f"{publisher_name}.json"
    if not schema_path.exists():
        return dict(status="error", description=f"Schema path {schema_path} does not exists!")
    schema_dict = json.loads(schema_path.read_text())

    return dict(status="converted", fields=schema_dict.get('fields'))


@publisher.post('/publish/{publisher_name}', tags=['publisher'])
def publish(new_publisher: PublisherSchema):
    current_publisher_cls = PublishManager.get_publisher(new_publisher.publisher_name)
    current_publisher_instance = current_publisher_cls(params=new_publisher.params)
    status = current_publisher_instance.publish()
    return dict(status="published" if status else "error", url="loo")

