from typing import List

from fastapi import APIRouter

from modules.database import DatabaseManager
from modules.models.generated import Document
from modules.schemas.document import DocumentSchema
from modules.utils import generate_slug

document = APIRouter()


@document.post('/create', tags=['document'])
def create_document(new_document: DocumentSchema):
    created_document = DatabaseManager.create(
        Document,
        title=new_document.title,
        name=generate_slug(new_document.title),
        slug=generate_slug(new_document.title),
        contents=new_document.contents
    )
    return dict(status='created', document_id=created_document.id)


@document.delete('/{document_uuid}', tags=['document'])
def delete_document(document_uuid: str):
    DatabaseManager.delete(
        Document,
        document_uuid
    )
    return dict(status='deleted', document_id=document_uuid)


@document.patch('/{document_uuid}', tags=['document'])
def update_document(document_uuid: str, doc: DocumentSchema):
    updated_document = DatabaseManager.update(
        Document,
        document_uuid,
        title=doc.title,
        contents=doc.contents
    )
    return dict(status='updated', document_id=updated_document.id)


@document.get('/{document_uuid}', tags=['document'])
def get_document(document_uuid: str):
    current_document = DatabaseManager.get(Document, lambda d: d.id == document_uuid, extract=True)
    return dict(status='read_one', result=current_document)


@document.get('/', tags=['document'])
def list_documents():
    all_documents = DatabaseManager.all(Document)
    return dict(status='read_all', count=len(all_documents), result=all_documents)


@document.post('/import', tags=['document'])
def import_documents(documents: List[DocumentSchema]):
    for doc in documents:
        create_document(doc)
