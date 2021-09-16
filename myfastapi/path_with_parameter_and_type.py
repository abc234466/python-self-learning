from fastapi import FastAPI

app = FastAPI()


@app.get('/items/{item_id}')
def get_item_id(item_id: int):
    return {'item_id': item_id}
