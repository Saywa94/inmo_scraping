import time
from utils import getPageData, writeToJson
from parametros import selectors, output_file, start_page

page_number = start_page
all_data = []
last_page = False

tic = time.perf_counter()

while not last_page:
    try:
        page_data, stop_parsing = getPageData(page_number, selectors)
        last_page = stop_parsing
    except:
        print(f'shit broke for no reason in {page_number}')
        break
    all_data.extend(page_data)
    print(f'pages scraped: {page_number}')
    page_number += 1

toc = time.perf_counter()


thic = time.perf_counter()
writeToJson(output_file, all_data)
thoc = time.perf_counter()


print(f'{page_number} total pages scraped')
print(f"Scraping lasted {toc - tic:0.4f} seconds")
print(f"Writing to json lasted {thoc - thic:0.4f} seconds")

