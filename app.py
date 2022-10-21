from preprocessing import cleaning_data
from predict import prediction

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import Optional
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {'Alive'}
class property_type(str, Enum):
        HOUSE = "HOUSE"
        APARTMENT = "APARTMENT"
class building_state(str, Enum):
        NEW = "NEW" 
        GOOD = "GOOD" 
        TO_RENOVATE = "TO RENOVATE"
        JUST_RENOVATED = "JUST RENOVATED" 
        TO_REBUILD = "TO REBUILD"
class Property(BaseModel):
    area: int
    property_type: property_type
    rooms_number: int
    zip_code: int
    land_area: Optional[int] | None = None
    garden: Optional[bool] | None = None
    garden_area: Optional[int] | None = None
    equipped_kitchen: bool | None = None 
    full_address: Optional[str] | None = None
    swimming_pool: bool
    furnished: Optional[bool] | None = None
    open_fire: bool
    terrace: bool
    terrace_area: int
    facades_number: int
    building_state: building_state

@app.get("/predict")
async def expecting_format():
    expected_format = {
    "area": int,
    "property_type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms_number": int,
    "zip_code": int,
    "land_area": int | None,
    "garden": bool | None,
    "garden_area": int | None,
    "equipped_kitchen": bool | None,
    "full_address": str | None,
    "swimming_pool": bool | None,
    "furnished": bool | None,
    "open_fire": bool | None,
    "terrace": bool | None,
    "terrace_area": int | None,
    "facades_number": int | None,
    "building_state": "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD" | None
     }
    return {"Please see the schema example to fill the fields.", expected_format}

@app.post("/predict", status_code=201)
async def getting_data(data: Property):
    df = pd.DataFrame.from_dict(data)  
    cleaned_df = cleaning_data.preprocess(df)
    price_predict = prediction.predict(cleaned_df)
    res = dict.fromkeys(['Price prediction'], price_predict)

    return res


