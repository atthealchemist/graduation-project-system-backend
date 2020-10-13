from modules.database import DatabaseManager
from modules.models.generated import Document


class DocumentManager:

    @staticmethod
    def get_document_by_id(doc_id):
        return DatabaseManager.get(Document, lambda d: d.id == doc_id, as_entity=True)

    @staticmethod
    def create_document_for_user(user):
        DatabaseManager.create(
            Document,
            user=user
        )

    @staticmethod
    def update_document_for_user(document, user):
        return DatabaseManager.update(
            Document,
            uuid=document.uuid,
            user=user
        )
