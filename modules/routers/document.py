from fastapi import APIRouter

from modules.database import DatabaseManager
from modules.models.document import Document
from modules.schemas.document import Document as DocumentSchema

document = APIRouter()


@document.post('/create', tags=['document'])
def create_document(doc: DocumentSchema):

    doc = DatabaseManager.create(
        Document,
        title=doc.title,
        contents=doc.contents
    )

    return dict(created=True, document_id=doc.id, created_at=str(doc.created_at))


@document.delete('/{document_uuid}/delete', tags=['document'])
def delete_document(document_uuid: str):
    DatabaseManager.delete(
        Document,
        document_uuid
    )
    return dict(deleted=True, deleted_document_uuid=document_uuid)


@document.patch('/{document_uuid}/update', tags=['document'])
def update_document(document_uuid: str, doc: DocumentSchema):
    updated = DatabaseManager.update(
        Document,
        document_uuid,
        title=doc.title,
        contents=doc.contents
    )
    return dict(updated=True, document_id=updated.id)


@document.get('/{document_uuid}', tags=['document'])
def get_document(document_uuid: str):
    doc = DatabaseManager.get(Document, lambda d: d.id == document_uuid)
    return dict(document=doc.id)


@document.get('/', tags=['document'])
def list_documents():
    docs = DatabaseManager.all(Document)
    return dict(documents=docs)


@document.post('/import', tags=['document'])
def import_documents():
    pass