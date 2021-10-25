
# PARAMETROS

import datetime

# #############################################
container_css_selector = '.inmuebles-item:not(.ads_LISTADO_INMUEBLESPos1)'
price_selector = '.inmuebles-item-precio h4'
title_selector = 'h2.text-ellipsis.line-height-30px'
zone_type_offer_selector = 'h3.text-ellipsis'
bed_wc_surface_selector = 'ul.list-inline li.icon-default-color'
next_page_selector = '#linkNext'
# ##############################################
url = 'https://www.ultracasas.com/buscar/casa-o-departamento-o-oficina-o-local-comercial-o-galpon-o-terreno-o-habitacion-o-edificio-o-quinta-propiedad-agricola-en-venta-o-alquiler-o-anticretico--en--selecciona-una-ciudad---selecciona-una-ciudad?page='


now = datetime.datetime.now().strftime("%Y-%m-%d")
# VARIABLES TO EXPORT
output_file = f'output/all_data_bolivia_{now}.json'
selectors = (
    url,
    container_css_selector,
    price_selector,
    title_selector,
    zone_type_offer_selector,
    bed_wc_surface_selector,
    next_page_selector,
)

