import requests
import csv

with open('{Your csv file with lattitude and longitude goes here ie) coordinates.csv}', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    FOV_VAL = "fov=90"
    IMG_SIZE = "size=1000x800"
    URL1 = "https://maps.googleapis.com/maps/api/streetview?pano="
    URLheading = "&heading="
    URL2 = "&size=1000x800&fov=120&key={Your API KEY goes here}" 
    images =[]
    heading = ["0","120","240"]

    from base64 import b64encode, b64decode
    from IPython.display import Image
    from IPython.display import display
    for row in reader:
      for heading_val in heading:
        r = requests.get("https://maps.googleapis.com/maps/api/streetview/metadata?location="+(str(', '.join(row)))+"&heading="+heading_val+"&key={Your API KEY goes here}") 
        pano_id = (r.json()["pano_id"])
        location = (r.json()["location"])
        r = requests.get(URL1+pano_id+URLheading+heading_val+URL2)
        if r.status_code == 200:
          code = (b64encode(r.content))
          img = Image(data=b64decode(code)) #each image
          display(img)
          print(location, "heading", heading_val)
          #images.append(img)
          

#display(*images)
#display.download_links('drive/colab/street_view/')
