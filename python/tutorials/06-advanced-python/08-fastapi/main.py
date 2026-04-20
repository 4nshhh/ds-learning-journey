from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
def hello():
    return "Hello"


food_items ={
    'indian' : ["Samosa","Vadapav"],
    'american' : ["Hotdog","Pie cake"],
    'italian' : ["Pizza","Pasta"]
}

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

@app.get("/get_items/{cuisine}")
def get_items(cuisine : AvailableCuisines):
    return food_items.get(cuisine)

coupon_code = {
    1 : "10%",
    2 : "20%",
    3 : "30%"
}

@app.get("/get_coupon/{code}")
async def coupon_code(code: int):
    return {"discount_Amount" : coupon_code.get(code)}
