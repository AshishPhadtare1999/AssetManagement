# from celery import app
from time import sleep
import pandas as pd
from .models import *
from AssetTracker.celery import app


#
# @shared_task
# def sleepy(duration):
#     print("File is in Que!...")
#     sleep(duration)
#     data = ManageAsset.objects.all().order_by('-created_at')
#     df = pd.DataFrame(data)
#     file_loc = f"assetManage.csv"
#     df.to_csv(file_loc, index=False)
#     print("File is created!....")


@app.task
def sample_task():
    file = open("hello.txt", "w")
    file.write(str("sadjadbjadbajdb"))
    file.close()
    print(">>>>>>>>>>>>>>>>> Hello <<<<<<<<<<<<<<<<<")
