from pydantic import EmailStr, BaseModel

# JSON payload containing access token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Contents of JWT Token
class TokenPayload(BaseModel):
    sub: str | None = None
