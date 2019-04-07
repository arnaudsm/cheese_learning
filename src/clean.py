debug = False


import pandas as pd 
from google_images_download import google_images_download

##CSV Importing
df = pd.read_csv("dataset/frenchcheese.csv", sep = ';', error_bad_lines=False)  
df = df.drop(columns=["Geo Shape"], axis=1)
df['index'] = df.index


if debug:
    print(df.head())
    df = df.head()  # debug (comment me in production)


##Image Scraping
response = google_images_download.googleimagesdownload()  

if not debug:
    for index, cheese in df.iterrows():
        search = "\""+cheese['Cheese']+"\" fromage"
        number = str(cheese['index'])
        print(search)

        arguments = {"keywords":search,"limit":50, "image_directory":number, "type":"photo", "color_type": "full-color", "prefix":cheese['Cheese']}  
        paths = response.download(arguments)  
        print(paths)  

print("Task completed")