import uuid
from flask import Flask, request
from db import items, stores
from flask_smorest import abort

app = Flask(__name__)

@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return abort(404, message= "Store not found")
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item, 201
    
@app.get("/store/<string:name>/item")
def get_item_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return abort(404, message= "Store not found")

@app.get("/item")
def get_all_items():
    return "Hello, world!"