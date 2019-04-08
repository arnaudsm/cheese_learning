# Retrieve empty images
from google_images_download import google_images_download

terms = ["plate", "empty plate", "dining table", "faces"]

##Image Scraping
response = google_images_download.googleimagesdownload()  
for each in terms:
    arguments = {"keywords":each,"limit":30, "image_directory":"empty", "type":"photo", "color_type": "full-color"}  
    paths = response.download(arguments)  
    print(paths)  


print("Task completed") 