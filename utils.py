from typing import Any, Dict, List, Tuple
from bs4 import BeautifulSoup
from constructors import Propiedad
import requests
import json


def getPageData(n_page: int = 1, selectors: Tuple[str, ...] = ()) -> Tuple[List[Dict[str, Any]], bool]:

    url, container_css_selector, price_selector, title_selector, zone_type_offer_selector, bed_wc_surface_selector, next_page_selector = selectors

    url = f'{url}{str(n_page)}'

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
        propiedad.normalizeData()
        
        page_data.append(propiedad.__dict__)
    
    stop_parsing = lasPage(soup, next_page_selector)

    return page_data, stop_parsing
    

def zoneTypeOfferSeparator(city_zone_type_offer: str) -> Tuple[str, ...]:
    city = city_zone_type_offer.split(' - ')[0].split(', ')[1]
    zone = city_zone_type_offer.split(' - ')[0].split(', ')[0]
    type = city_zone_type_offer.split(' - ')[1].split(' en ')[0]
    offer = city_zone_type_offer.split(' - ')[1].split(' en ')[1]

    return city, zone, type, offer


def getBedWcSurface(card: Any, selector: str) -> Tuple[Any, ...]:
    svg_bed = '.fa-bed'
    svg_bath = '.fa-bath'

    n_bedrooms = 0
    n_wc = 0
    surface = ''

    container = card.select(selector)
    if len(container) == 3:
        n_bedrooms = int(container[0].text) if container[0].text != '' else 0
        n_wc = int(container[1].text) if container[1].text != '' else 0
        surface = container[2].text
        return n_bedrooms, n_wc, surface

    if len(container) == 2:
        try:
            n_bedrooms = int(container[0].text)
            n_wc = int(container[1].text)
        except:
            if container[0].select(svg_bath) != []:
                n_wc = int(container[0].text)
            n_bedrooms = int(container[0].text)
            surface = container[1].text
        return n_bedrooms, n_wc, surface

    if len(container) == 1:
        if container[0].select(svg_bath) != []:
            n_wc = int(container[0].text)
            return n_bedrooms, n_wc, surface
        if container[0].select(svg_bed) != []:
            n_bedrooms = int(container[0].text)
            return n_bedrooms, n_wc, surface

        surface = container[0].text
        return n_bedrooms, n_wc, surface
    
    return n_bedrooms, n_wc, surface


def lasPage(soup, page_selector: str) -> bool:
    next_page = soup.select(page_selector)
    return next_page == []


def writeToJson(pathToFile: str, all_data: List[Dict]):
    out_file = open(pathToFile, "w", encoding='utf8')
    json.dump(all_data, out_file, indent = 4, ensure_ascii = False)
    out_file.close()