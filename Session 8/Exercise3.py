import requests
nasa_image = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
print(nasa_image)

nasa_data=nasa_image.json()
print(nasa_data["url"])

base_url="https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
data_param="date=2021-06-16"
nasa_image=requests.get(base_url+'&'+data_param)
nasa_data=nasa_image.json()
print(nasa_data["url"])

import datetime
today=datetime.datetime.today().strftime('%Y-%m-%d')
print(today)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)