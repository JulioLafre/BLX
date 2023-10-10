from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import product_routers, auth_routers, order_routers

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

#Security Routes: authentication and authorization
app.include_router(auth_routers.router, prefix="/auth")

#Orders Routers
app.include_router(order_routers.router)
