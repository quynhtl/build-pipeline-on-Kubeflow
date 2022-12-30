from pathlib import Path
from google.cloud import storage
import schedule #setup time chạy tự động
import time
import os

# export GOOGLE_APPLICATION_CREDENTIALS=./my_pipeline/dummy-u.json
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./my_pipeline/dummy-u.json'
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

import shutil

# Create the new folder
# os.makedirs("data")add

#move
shutil.move("train", "./data/train")
shutil.move("validation", "./data/validation")


# Copy the folders into the parent folder
# shutil.copytree("train", "./data/train")
# shutil.copytree("validation", "./data/validation")

# import tarfile
# import os.path
# def make_tarfile(output_filename, source_dir):
#     with tarfile.open(output_filename, "w:gz") as tar:
#         tar.add(source_dir, arcname=os.path.basename(source_dir))
# make_tarfile('./output.tar', './data')



