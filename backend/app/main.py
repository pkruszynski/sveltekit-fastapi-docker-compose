from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/fruit_prices")
def get_day_of_week():
    """
    Get fruit prices
    """
    fruit = ["banana", "apple", "orange"]
    price = [1.37, 0.99, 2.25]
    return dict(zip(fruit, price))
