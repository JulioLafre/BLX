from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import product_routers, user_routers

app = FastAPI()

#Cors
origins = [
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
     allow_methods=["*"],
    allow_headers=["*"]
)

# Products Routers
app.include_router(product_routers.router)

#Users Rotes
app.include_router(user_routers.router)

