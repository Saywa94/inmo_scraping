from typing import Dict, List
from bs4 import BeautifulSoup
from constructors import Propiedad
import requests
import json


def getPropertiesInPageData(n_page: int = 1, selectors: Dict[str, str] = {}) -> List[Dict]:

    container_css_selector = selectors['container_css_selector']
    price_selector = selectors['price_selector']
    title_selector = selectors['title_selector']
    zone_type_offer_selector = selectors['zone_type_offer_selector']
    bed_wc_surface_selector = selectors['bed_wc_surface_selector']

    url = f'https://www.ultracasas.com/buscar/casa-en-venta--en--la-paz---la-paz?page={str(n_page)}'

    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    page_data = []
    all_card_containers = soup.select(container_css_selector)
    

    for card in all_card_containers:
        price = card.select(price_selector)[0].string
        title = card.select(title_selector)[0].string
        

        zone_type_offer_string = card.select(zone_type_offer_selector)[0].string
        zone_type_offer = zoneTypeOfferSeparator(zone_type_offer_string)
        city = zone_type_offer['city']
        zone = zone_type_offer['zone']
        type = zone_type_offer['type']
        offer = zone_type_offer['offer']

        try:
            n_bedrooms = card.select(bed_wc_surface_selector)[0].text
            n_bedrooms = int(n_bedrooms) if n_bedrooms != '' else ''
            n_wc = card.select(bed_wc_surface_selector)[1].text
            n_wc = int(n_wc) if n_wc != '' else ''
            surface = card.select(bed_wc_surface_selector)[2].text
        except:
            try:
                n_bedrooms = int(card.select(bed_wc_surface_selector)[0].text)
                n_wc = int(card.select(bed_wc_surface_selector)[1].text)
                surface = ''
            except:
                try:
                    n_bedrooms = int(card.select(bed_wc_surface_selector)[0].text)
                    n_wc = ''
                    surface = card.select(bed_wc_surface_selector)[1].text
                except:
                    n_bedrooms = ''
                    n_wc = ''
                    surface = card.select(bed_wc_surface_selector)[0].text

        propiedad = Propiedad(title, price, city, zone, offer, type, surface, n_bedrooms, n_wc)

        page_data.append(propiedad.__dict__)

    return page_data


def zoneTypeOfferSeparator(city_zone_type_offer: str) -> Dict[str, str]:
    city = city_zone_type_offer.split(' - ')[0].split(', ')[1]
    zone = city_zone_type_offer.split(' - ')[0].split(', ')[0]
    type = city_zone_type_offer.split(' - ')[1].split(' en ')[0]
    offer = city_zone_type_offer.split(' - ')[1].split(' en ')[1]

    return { 'city': city, 'zone': zone, 'type': type, 'offer': offer }


def writeToJson(pathToFile: str, all_data: List[Dict]):
    out_file = open(pathToFile, "w", encoding='utf8')
    json.dump(all_data, out_file, indent = 4, ensure_ascii = False)
    out_file.close()