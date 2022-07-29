class InvalidToken(Exception):
    def __init__(self, message: str = ""):
        msg = message.capitalize() if message else "Invalid Token"
        super().__init__(msg)
