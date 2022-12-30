import zipfile
import os


# Create the zip file
with zipfile.ZipFile("output.zip", "w") as zip_file:
    # Iterate through the files in the first folder
    for root, dirs, files in os.walk("./data/train"):
        for file in files:
            # Add the file to the zip file
            zip_file.write(os.path.join(root, file))
    # Iterate through the files in the second folder
    for root, dirs, files in os.walk("./data/validation"):
        for file in files:
            # Add the file to the zip file
            zip_file.write(os.path.join(root, file))




data_zip_path = "./data_zip.zip"
# Open the zip file
with zipfile.ZipFile(data_zip_path, "r") as zip_file:
    # Extract the contents of the zip file to the "extracted" directory
    zip_file.extractall()