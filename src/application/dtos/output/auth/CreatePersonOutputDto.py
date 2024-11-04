from src.domain.entities.auth.PersonEntity import PersonEntity


class CreatePersonOutputDto:
    def __init__(self, person_entity: PersonEntity) -> None:
        self.person_entity = person_entity
