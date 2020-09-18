from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter

from modules.database import DatabaseManager
from modules.models.document import Document

document = APIRouter()


@document.post('/create', tags=['document'])
def create_document():

    params = ''
    DatabaseManager.create(
        Document,
    )

    return dict(document_uuid=str(uuid4()), created=True, created_at=str(datetime.now()))


@document.delete('/{document_uuid}/delete', tags=['document'])
def delete_document(document_uuid: str):
    return dict(deleted_document_uuid=document_uuid)


@document.patch('/{document_uuid}/update', tags=['document'])
def update_document(document_uuid: str):
    return dict(document=document_uuid, updated=True)


@document.get('/{document_uuid}', tags=['document'])
def get_document(document_uuid: str):
    return dict(document=document_uuid)


@document.get('/', tags=['document'])
def list_documents():
    docs = [dict(test='document')]
    return dict(documents=docs)


@document.post('/import', tags=['document'])
def import_documents():
    pass