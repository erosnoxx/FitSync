import os
from uuid import uuid4
from dotenv import load_dotenv
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID
from src.application.extensions.Settings import db

load_dotenv()
schema = os.getenv('DATABASE_SCHEMA', 'fitsync')


class BaseEntity(db.Model):
    __abstract__ = True
    __table_args__ = {'schema': schema}
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))
