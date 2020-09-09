import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Binary
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
    slug = Column(String)
    url = Column(String)
    short_url = Column(String)
    contents = Column(Binary)

    references = relationship("Reference", back_populates="document")
    links = relationship("Link", back_populates="document")
    assets = relationship("Asset", back_populates="document")

    changes = relationship("Change", back_populates="document")
    comments = relationship("Comment", back_populates="document")
