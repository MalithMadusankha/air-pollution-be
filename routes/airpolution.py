from fastapi import APIRouter
from controller.airpolution import sourece_detect
from models.airpolution import Airpolution

source = APIRouter()

@source.post('/airpolution')
async def find_source(activity: Airpolution):
    res = sourece_detect(activity)
    print("res : ", res)
    return res
