import time
from utils import getPageData, writeToJson


page_number = 1
all_data = []
last_page = False

tic = time.perf_counter()

while not last_page:
    try:
        page_data, stop_parsing = getPageData(page_number)
        last_page = stop_parsing
    except:
        print(f'shit broke for no reason in {page_number}')
        break
    all_data.extend(page_data)
    print(f'pages scraped: {page_number}')
    page_number += 1

toc = time.perf_counter()

writeToJson(all_data)


print(f'{page_number} total pages scraped')
print(f"Scraping lasted {toc - tic:0.4f} seconds")

