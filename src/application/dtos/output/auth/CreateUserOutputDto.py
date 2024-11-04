from src.domain.entities.auth.UserEntity import UserEntity


class CreateUserOutputDto:
    def __init__(self, user_entity: UserEntity):
        self.user_entity = user_entity
