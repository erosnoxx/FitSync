from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List, Optional
from src.domain.entities.common.BaseEntity import BaseEntity

T = TypeVar('T', bound=BaseEntity)


class BaseRepository(Generic[T]):
    def __init__(self, session: Session, entity: Type[T]):
        self.session = session
        self.entity = entity

    def add(self, obj: T) -> T:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj
            
    def get(self, obj_id: int) -> Optional[T]:
        return self.session.query(self.entity).filter(self.entity.id == obj_id).first()
    
    def get_all(self) -> List[T]:
        return self.session.query(self.entity).all()

    def update(self, obj: T) -> T:
        self.session.merge(obj)
        self.session.commit()
        return obj

    def delete(self, obj_id: int) -> None:
        obj = self.get(obj_id)
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def delete_all(self) -> None:
        self.session.query(self.entity).delete()
        self.session.commit()

    def add_bulk(self, objs: List[T]) -> List[T]:
        self.session.bulk_save_objects(objs)
        self.session.commit()
        return objs
