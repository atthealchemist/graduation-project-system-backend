from uuid import UUID

from fastapi import APIRouter

from modules.core.database import DatabaseManager
from modules.models.space import Space
from modules.utils import extract_entity

space = APIRouter()


@space.get('/{space_uuid}', tags=['space'])
def get_space(space_uuid: str):
    current_space = DatabaseManager.get(Space, lambda u: u.id == UUID(space_uuid))
    current_space_extracted = extract_entity(current_space)
    return dict(status='read_one', result=current_space_extracted)


@space.get('/', tags=['space'])
def list_spaces():
    spaces = DatabaseManager.all(Space)
    spaces = [extract_entity(current_space) for current_space in spaces]
    return dict(status='read_all', count=len(spaces), result=spaces)
