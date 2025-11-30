class User:
    def __init__(self, user_id: str, username: str, password_hash: str):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
