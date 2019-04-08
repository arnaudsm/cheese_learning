import pandas as pd 
from google_images_download import google_images_download
import urllib.request
import os

# Config
downloadPics = False
exportList = True


df = pd.read_csv("dataset/frenchcheese.csv", sep = ';', error_bad_lines=False) #CSV Importing
df = df.drop(columns=["Geo Shape", "geo_point_2d", "Department"], axis=1) #Drop useless columns

df.rename(columns={'Cheese':'Name'}, inplace=True) #Rename 'Name' column

# Sort by frequency and remove duplicates
df['freq'] = df.groupby('Name')['Name'].transform('count') 
df = df.sort_values(['freq'], ascending=False).drop_duplicates(['Name'], keep='first') 

# Indexing
df = df.reset_index() 
df['index'] = df.index

# Deleting less popular cheeses
df = df.drop(df[df.freq <= 1].index)


print(df.shape)
print(df[["Name", "freq"]])
df = df.drop(columns=["freq"], axis=1)

##Image Scraping
response = google_images_download.googleimagesdownload()  


for index, cheese in df.iterrows():
    search = "\""+cheese['Name']+"\" fromage"
    number = str(cheese['index'])
    print(search)


    if downloadPics:
        folder = "downloads/"+number+"/"
        try:  
            os.mkdir(folder)
        except OSError:  
            print("folder already exists")
        
        try:
            filename = os.path.join(folder, cheese['Name']+".jpg")

            urllib.request.urlretrieve(cheese['Image'], filename)
        except:
            print('Error')
        

        arguments = {"keywords":search,"limit":50, "image_directory":number, "type":"photo", "color_type": "full-color", "prefix":cheese['Name']}  
        paths = response.download(arguments)  
        print(paths)  

if exportList:
    df.to_csv("dataset/best_cheese.csv", index=False)


print("Task completed")