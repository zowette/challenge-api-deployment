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
    return ('''
    This model is takes the next information as an input:
    area: int
    property_type: str #"APARTMENT" | "HOUSE",
    rooms_number: int
    zip_code: int
    land_area: int | None #Optional[int]
    garden: bool | None [bool],
    garden_area: int | None [int],
    equipped_kitchen: bool | None [bool],
    full_address: str | None #Optional[str],
    swimming_pool: bool | None [bool],
    furnished: bool | None #Optional[bool],
    open_fire: bool | None [bool],
    terrace: bool | None [bool],
    terrace_area: int | None [int],
    facades_number: int | None [int],
    building_state: str | None ["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
    ''')

@app.post("/predict", status_code=201)
async def getting_data(data: Property):
    df = pd.DataFrame.from_dict(data)  
    cleaned_df = cleaning_data.preprocess(df)
    price_predict = prediction.predict(cleaned_df)
    res = dict.fromkeys(['Price prediction'], price_predict)

    return res


