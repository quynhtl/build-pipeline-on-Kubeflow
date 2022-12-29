from pathlib import Path
from google.cloud import storage
import schedule #setup time chạy tự động
import time
import os

# export GOOGLE_APPLICATION_CREDENTIALS=./dummy-mles.json
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./dummy-mles.json'
#echo: xem có biến môi trường hay chưa


gcs_client = storage.Client()
bucket = gcs_client.bucket('mles-class-storage')
blobs = bucket.list_blobs()

def download_data():
  for blob in blobs:
      if blob.exists():
          filename = blob.name
          if filename.endswith("/"):
            continue
          file_split = filename.split("/")
          directory = "/".join(file_split[0:-1])
          Path(directory).mkdir(parents=True, exist_ok=True)
          print('Downloading {} from GCS'.format(filename))
          blob.download_to_filename(filename) 
          print('Downloaded {} from GCS'.format(filename))

# schedule.every(1).minutes.do(download_data)

# while True:
#   schedule.run_pending()
#   time.sleep(1)
  
download_data()

# import shutil

# Create the new folder
# os.makedirs("data")

# #move
# shutil.move("train", "./data/train")
# shutil.move("validation", "./data/validation")



# Copy the folders into the parent folder
# shutil.copytree("train", "./data/train")
# shutil.copytree("validation", "./data/validation")

