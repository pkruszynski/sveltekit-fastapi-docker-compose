import json
import random

from faker import Faker
from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS is needed for static adapter only
# origins = [
#     "http://localhost",
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/get_scores")
def get_scores():
    """
    Get scores
    """

    fake = Faker()
    Faker.seed(0)

    result = []

    for id in range(100):
        result.append({"id": id, "name": fake.name(), "points": fake.pyint()})

    return json.dumps(result)


@app.get("/get_random_number")
def get_random_number():
    """
    Get random number
    """

    return {"random_number": random.randrange(1, 1000)}
