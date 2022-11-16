import requests
from bs4 import BeautifulSoup


main_url = 'https://flagpedia.net'
country_name = input("Country Name:").lower()


flag_info_url = f'{main_url}/{country_name}'
flag_response = requests.get(flag_info_url)
flag_soup = BeautifulSoup(flag_response.content, 'html.parser')


image = flag_soup.select('div img')
image_folder = image[0]['src']
print(image_folder)


###############################


img_data = requests.get(
    f'{main_url}{image_folder}').content

location_saved = f'downloaded_flags/{country_name}.jpg'
with open(location_saved, 'wb') as handler:
    handler.write(img_data)
