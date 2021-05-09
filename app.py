import time
from utils import zoneTypeOfferSeparator, getPropertiesInPageData, writeToJson


# PARAMETROS
# #############################################
container_css_selector = '.inmuebles-item:not(.ads_LISTADO_INMUEBLESPos1)'
price_selector = '.inmuebles-item-precio h4'
title_selector = 'h2.text-ellipsis.line-height-30px'
zone_type_offer_selector = 'h3.text-ellipsis'
bed_wc_surface_selector = 'ul.list-inline li.icon-default-color'

output_file = 'output/casas_data.json'

max_pages = 3
# ##############################################

selectors = (
    container_css_selector,
    price_selector,
    title_selector,
    zone_type_offer_selector,
    bed_wc_surface_selector
)

page_number = 1
all_data = []

tic = time.perf_counter()
while True:
    if page_number == max_pages + 1:
        break
    try:
        page_data = getPropertiesInPageData(page_number, selectors)
    except:
        print('shit broke for no reason')
        break
    all_data.extend(page_data)
    page_number += 1
toc = time.perf_counter()


thic = time.perf_counter()
writeToJson(output_file, all_data)
thoc = time.perf_counter()


print(page_number)
print(f"Scraping lasted {toc - tic:0.4f} seconds")
print(f"Writing to json lasted {thoc - thic:0.4f} seconds")

