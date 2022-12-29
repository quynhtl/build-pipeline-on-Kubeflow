from pathlib import Path
from google.cloud import storage
from google.oauth2.credentials import Credentials
gcs_client = storage.Client()
bucket = gcs_client.bucket('mles-class-storage')

import os 

# export GOOGLE_APPLICATION_CREDENTIALS=./dummy-mles.json
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']='./dummy-mles.json'
#echo: xem có biến môi trường hay chưa
import schedule #setup time chạy tự động
import time

import os

from google.cloud import storage
gcs_client = storage.Client()
bucket = gcs_client.bucket('mles-class-storage')

from pathlib import Path
blobs = bucket.list_blobs()

# def download_data():
#   for blob in blobs:
#       if blob.exists():
#           filename = blob.name
#           if filename.endswith("/"):
#             continue
#           file_split = filename.split("/")
#           directory = "/".join(file_split[0:-1])
#           Path(directory).mkdir(parents=True, exist_ok=True)
#           print('Downloading {} from GCS'.format(filename))
#           blob.download_to_filename(filename) 
#           print('Downloaded {} from GCS'.format(filename))

def download_data():

  gg_credential = {
    "type": "service_account",
    "project_id": "vertical-set-272909",
    "private_key_id": "0dcb64c16224be9bdec1a844bad9960a0755c905",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCs1024z3+fjUd5\nkj8YKU79IIOSFpwyb9BvLXxfqqttTKjxISBeWrNflLrBWS50BeMz1BIq+vkCn76x\nbXNNHlmAjiloqzuLYFsBcTg7Hc+vNKkzxBzOumLlA6HYkBJyeIsfFpzhP+05jIls\nMGaPIBfPyDNCvF9XYt8BW+0MlNCXY6JgHAED4+rw2jG17+EKIi9SHWPJ1xjBnvYi\ne6SgdOk9GUfL/EVOix2rp3DIngtUsm3ah0x5zUpZPtRfp144SWVDB85whX2nT62D\nD+Es0msMBe2lz20PMACsTPnRo4mV/FYD3owyXoXAk3Vh8QehgKeaF/zvx6X2e4MU\nvdrIWkMjAgMBAAECggEAIWZv0gVjE7mQ9NjCkZA1/+tfEYWGBKcf38Qp8zC/dN0q\nDoLIxwL/A7rxhfiOZgRXPgY+xoh+QzgMeSv96oqxYArYzK2+UXY6z+IJrD7cCe8C\nvYqpyHczMi9MANYCgpVxyP2tLkgUtxjF257Uyta4U0JMSZquT+w+zPvvKI2/a2mX\nvJ5E2oCqPnq1YUSdDX+N2cPTocerVf9kwgEuq4cuGdFdOa+/ylGV4sGEqEOTiMIQ\n1RjkVrQph+DOYcckwqVVXA8JiBzqiM91XhSjo8f7Uh15PjhbKmXkaVpxIYzrhcrj\nkVvn0ppmsMmbiziLnX3zizfKl+Rvm0DCHmO69DgcoQKBgQDYK0m+Y6ieXkedfI+B\nRuBsQ3kSUu3s4YcXNrFrx3FL3UFDnzv8wLFk7U+0M0A7gAkvmSXxjCQNTs+qT6xo\nohlpdTx6Uy/PQVbxIVCHhDH4BUTwIILAUkW64s++JRI5LuTycb1hCm20PoFQVdus\nTApDYsQ4GGKr4PcujKyCP8ZioQKBgQDMsDpDA7wOpOMszLyNr8dPBcEVtbWnWV9c\ny6vOfNI4IfgyM3ZxM/tK/rIlPFRI92L/bVIqabGu4pXt8b/xnm7O/d19L7XTee7e\nKzCVopxS2ADJ3CWaesYX6qShZq/V8SzEn41cOayHlOyr4MDBJAxMMtAO88Y3XnjP\nkjAaxUyTQwKBgQC5LHvDSAONhh263pTfnSNqGnKAK+H8ZUUfsY5SUUrQPfxGPQVa\nAobzegYoyy5eydMUnxBN1kqby8NAlXePOiyilfb0ooX1+HbNoEgnjipv17OyL2dR\n8Cgja1+h9oehzHX66Uvc8N4A5PpJIwNGmOzBxL1pgBomOlQD4CV2fcMngQKBgE2w\n2fxTr45zYVLAxxSUUncY/Qerd650SrDjEWwHjpcFtboANIWVMF1vvNhLRMaJN4cx\nzE0S3wE9OaEd8DfaZb6lNutsL3x8PIERLZiuJt1+5RW5PICc9xFe22vzmOwAZXig\nArytm2G+0fIPFbp5Xz2Qz83NE0Ay2HIYz69pkb4XAoGAE9QOS880lNqBhkEmoGxe\nzvtGZy8wZ0qlwzg0/GbuZDkFmY30Dyle7q+O2VRGAsmePIOuG2Qy2qmdMELYRN15\nN1YAI5GkgzxlrbSMSTutPtMD4YPvaXh7uESdPOXaYX88kU79t8DBlL3TVRPYUUco\nxorwJoqs4JHRyroxLGScwFg=\n-----END PRIVATE KEY-----\n",
    "client_email": "mles-dummy-user@vertical-set-272909.iam.gserviceaccount.com",
    "client_id": "106495373658812956228",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mles-dummy-user%40vertical-set-272909.iam.gserviceaccount.com"
  }

  creds = Credentials.from_authorized_user_info(info=gg_credential)
  gcs_client = storage.Client(credentials=creds)

  bucket = gcs_client.bucket('mles-class-storage')
  blobs = bucket.list_blobs()
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

schedule.every(1).minutes.do(download_data)

while True:
  schedule.run_pending()
  time.sleep(1)
  
# download_data()