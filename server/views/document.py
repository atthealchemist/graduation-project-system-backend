from typing import List

from ..main import app
from ..schemas.document import Document


@app.get('/documents/', response_model=List[Document])
def get_documents():
    pass


@app.get('/document/{document_uuid}/', document_uuid=None)
def get_document():
    pass


@app.post('/document/create/')
def create_document():
    pass


@app.patch('/document/edit/{document_uuid}', document_uuid=None)
def edit_document():
    pass


@app.delete('/document/delete/{document_uuid}', document_uuid=None)
def delete_document():
    pass
