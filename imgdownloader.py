import random                     #random generates a random number which we can use to save file with different n ames
import urllib.request               #to request for an image with url
def download(url):  
    name=random.randrange(1,1000)                         #creates random number 
    fullname=str(name) + ".jpg"                             #to save the file with extension 
    urllib.request.urlretrieve(url,fullname)                #funcyion to request an image

download("https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg")
