from fastapi import FastAPI
import json

# Importing Models
from src.movie_reviews.main import predict as movie_reviews
from src.cat_and_dog.main import predict as cat_and_dog

# Initializing App
app = FastAPI()

# Allowing Cross Origins
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints

@app.get("/")
def index():
	return "Welcome to the API of PyModelsAI"

@app.get("/movie_reviews")
def endpoint_movie_reviews(text: str):
	output = movie_reviews(text)
	return json.dumps(output)

@app.get("/cat_and_dog")
def endpoint_cat_and_dog(
        resized_img_base64:str = None,
        img_url:str = None
    ):
    output = cat_and_dog(resized_img_base64, img_url)
    return json.dumps(output)