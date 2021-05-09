import time

from utils import zoneTypeOfferSeparator, getPropertiesInPageData, writeToJson


selectors = {
    'container_css_selector':   '.inmuebles-item:not(.ads_LISTADO_INMUEBLESPos1)',
    'price_selector':           '.inmuebles-item-precio h4',
    'title_selector':           'h2.text-ellipsis.line-height-30px',
    'zone_type_offer_selector': 'h3.text-ellipsis',
    'bed_wc_surface_selector':  'ul.list-inline li.icon-default-color',
}

output_file = 'output/casas_data.json'
all_data = []

page_number = 1
# Para casas en venta en La Paz, solo hay 41 paginas
max_pages = 3

    
tic = time.perf_counter()
while True:
    if page_number == max_pages + 1:
        print('Max number of pages attained')
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

