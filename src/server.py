from fastapi import FastAPI

app = FastAPI()

@app.post("/profile")
def create_user():
    return {"Msg": "User Create"}

@app.post("/products")
def create_product():
    return {"Msg": "Product Create"}

@app.get("/products")
def list_products():
    return {"Msg": "Products List"}



