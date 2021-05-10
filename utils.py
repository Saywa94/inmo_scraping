from typing import Dict, List, Tuple
from bs4 import BeautifulSoup
from constructors import Propiedad
import requests
import json


def getPropertiesInPageData(n_page: int = 1, selectors: Tuple = ()) -> Tuple[List[Dict], bool]:

    container_css_selector, price_selector, title_selector, zone_type_offer_selector, bed_wc_surface_selector, next_page_selector = selectors

    url = f'https://www.ultracasas.com/buscar/casa-o-departamento-o-terreno-en-venta--en--la-paz---la-paz?page={str(n_page)}'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    page_data = []
    all_card_containers = soup.select(container_css_selector)
    
    for card in all_card_containers:
        price = card.select(price_selector)[0].string
        title = card.select(title_selector)[0].string

        zone_type_offer_string = card.select(zone_type_offer_selector)[0].string
        city, zone, type, offer = zoneTypeOfferSeparator(zone_type_offer_string)
        n_bedrooms, n_wc, surface = getBedWcSurface(card, bed_wc_surface_selector)

        propiedad = Propiedad(title, price, city, zone, offer, type, surface, n_bedrooms, n_wc)
        page_data.append(propiedad.__dict__)
    
    stop_parsing = lasPage(soup, next_page_selector)

    return page_data, stop_parsing
    

def zoneTypeOfferSeparator(city_zone_type_offer: str) -> Tuple:
    city = city_zone_type_offer.split(' - ')[0].split(', ')[1]
    zone = city_zone_type_offer.split(' - ')[0].split(', ')[0]
    type = city_zone_type_offer.split(' - ')[1].split(' en ')[0]
    offer = city_zone_type_offer.split(' - ')[1].split(' en ')[1]

    return city, zone, type, offer


def getBedWcSurface(card: str, selector: str) -> Tuple:
    try:
        n_bedrooms = card.select(selector)[0].text
        n_bedrooms = int(n_bedrooms) if n_bedrooms != '' else ''
        n_wc = card.select(selector)[1].text
        n_wc = int(n_wc) if n_wc != '' else ''
        surface = card.select(selector)[2].text
        
    except:
        try:
            n_bedrooms = int(card.select(selector)[0].text)
            n_wc = int(card.select(selector)[1].text)
            surface = ''
        except:
            try:
                n_bedrooms = int(card.select(selector)[0].text)
                n_wc = ''
                surface = card.select(selector)[1].text
            except:
                try:
                    n_bedrooms = ''
                    n_wc = ''
                    surface = card.select(selector)[0].text
                except:
                    n_bedrooms = ''
                    n_wc = ''
                    surface = ''

    return n_bedrooms, n_wc, surface


def lasPage(soup, page_selector: str) -> bool:
    next_page = soup.select(page_selector)
    return next_page == []


def writeToJson(pathToFile: str, all_data: List[Dict]):
    out_file = open(pathToFile, "w", encoding='utf8')
    json.dump(all_data, out_file, indent = 4, ensure_ascii = False)
    out_file.close()