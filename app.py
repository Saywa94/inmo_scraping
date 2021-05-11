import time
from utils import getPropertiesInPageData, writeToJson
from parametros import selectors, output_file

page_number = 1
all_data = []
last_page = False

tic = time.perf_counter()

while not last_page:
    try:
        page_data, stop_parsing = getPropertiesInPageData(page_number, selectors)
        last_page = stop_parsing
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

