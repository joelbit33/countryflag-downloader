import requests
from bs4 import BeautifulSoup


def download_flag(country_name, image_src):

    location_saved = f'downloaded_flags/{country_name}.jpg'
    with open(location_saved, 'wb') as handler:
        handler.write(image_src)


def find_flag(main_url):
    """Finds image source link from the main url
    """
    country_name = input("Country Name:").lower()

    flag_info_url = f'{main_url}/{country_name}'
    flag_response = requests.get(flag_info_url)
    flag_soup = BeautifulSoup(flag_response.content, 'html.parser')

    image = flag_soup.select('div img')
    image_path = image[0]['src']
    image_src = requests.get(
        f'{main_url}{image_path}').content
    return country_name, image_src


main_url = 'https://flagpedia.net'
country_name, image_src = find_flag(main_url)

download_flag(country_name, image_src)
