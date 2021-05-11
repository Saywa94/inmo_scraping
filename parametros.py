
# PARAMETROS

# #############################################
container_css_selector = '.inmuebles-item:not(.ads_LISTADO_INMUEBLESPos1)'
price_selector = '.inmuebles-item-precio h4'
title_selector = 'h2.text-ellipsis.line-height-30px'
zone_type_offer_selector = 'h3.text-ellipsis'
bed_wc_surface_selector = 'ul.list-inline li.icon-default-color'
next_page_selector = '#linkNext'
# ##############################################

output_file = 'output/casas_deptos_terrenos_data.json'

url = 'https://www.ultracasas.com/buscar/casa-o-departamento-o-oficina-o-local-comercial-o-galpon-o-terreno-o-habitacion-o-edificio-o-quinta-propiedad-agricola-en-venta-o-alquiler-o-anticretico--en--la-paz---la-paz?page='


selectors = (
    url,
    container_css_selector,
    price_selector,
    title_selector,
    zone_type_offer_selector,
    bed_wc_surface_selector,
    next_page_selector,
)



# casa = 1
# departamento = 1
# local = 1
# terreno = 1

# oficina = 1
# habitacion = 1
# galpon = 1
# edificio = 1

# venta = 1
# alquiler = 1
# anticretico = 1

# region = 'la-paz'
# ciudad = 'la-paz'

# search = 'casa-o-departamento-o-oficina-o-local-comercial-o-galpon-o-terreno-o-habitacion-o-edificio-en-venta-o-alquiler-o-anticretico--en--la-paz---la-paz?page='

# def get_search():

#     url = f'{casa}{departamento}{oficina}{local}{galpon}{terreno}{habitacion}{edificio}en{venta}{alquiler}{anticretico}-en--{region}---{ciudad}'
#     return url