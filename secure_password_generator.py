import random
from fastapi import FastAPI, HTTPException

app = FastAPI()

MAX_ALLOWED_PASSWORD_LENGTH = 256
ALLOWED_STRING_LETTERS: list[str] = [character for character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*"]

async def get_random_string(length: int) -> str:
    """Generates a securely random string with the length provided"""
    return "".join(map(str, [ALLOWED_STRING_LETTERS[await get_random_string_index()] for _ in range(length)]))

async def get_random_string_index() -> int:
    """Generates a securely random integer ranging from 0 (the beginning of the ALLOWED_STRING_LETTERS list) to the end of the ALLOWED_STRING_LETTERS list"""
    return random.SystemRandom().randint(0, len(ALLOWED_STRING_LETTERS) - 1)

@app.get("/generate_password/{password_length}")
async def generate_password(password_length: int):
    if (password_length > MAX_ALLOWED_PASSWORD_LENGTH or password_length < 1):
        raise HTTPException(status_code=422, detail=f"Input should be an integer ranging from 1 - {MAX_ALLOWED_PASSWORD_LENGTH}, got {password_length} instead.")
    return {"secure_password": await get_random_string(password_length)}