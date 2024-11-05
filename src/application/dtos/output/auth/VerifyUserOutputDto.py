from src.domain.entities.auth.UserEntity import UserEntity


class VerifyUserOutputDto:
    def __init__(self, user_entity: UserEntity) -> None:
        self.user_entity = user_entity
