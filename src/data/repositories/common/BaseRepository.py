from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, TypeVar, Generic, List, Optional
from src.domain.entities.common.BaseEntity import BaseEntity

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, entity: Type[T]):
        self.session = session
        self.entity = entity

    def add(self, obj: T) -> T:
        try:
            self.session.add(obj)
            self.session.commit()
            self.session.refresh(obj)
            return obj
        except SQLAlchemyError as e:
            self.session.rollback()  # Reverte a transação em caso de erro
            raise e  # Opcional: levanta a exceção novamente para tratamento externo
        finally:
            self.session.close()  # Fecha a sessão

    def get(self, obj_id: int) -> Optional[T]:
        try:
            return self.session.query(self.entity).filter(self.entity.id == obj_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()  # Reverte a transação em caso de erro
            raise e
        finally:
            self.session.close()

    def get_all(self) -> List[T]:
        try:
            return self.session.query(self.entity).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def update(self, obj: T) -> T:
        try:
            self.session.merge(obj)
            self.session.commit()
            return obj
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def delete(self, obj_id: int) -> None:
        try:
            obj = self.get(obj_id)
            if obj:
                self.session.delete(obj)
                self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def delete_all(self) -> None:
        try:
            self.session.query(self.entity).delete()
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def add_bulk(self, objs: List[T]) -> List[T]:
        try:
            self.session.bulk_save_objects(objs)
            self.session.commit()
            return objs
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
