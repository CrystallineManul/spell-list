class UserModel:
    user_id: int
    nickname: str

    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname
