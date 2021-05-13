class Propiedad:
    def __init__(self, titulo, precio, ciudad, zona, tipo_oferta, tipo_bien, superficie, n_habitaciones, n_wc):
        self.titulo = titulo
        self.precio = precio
        self.moneda = ''
        self.ciudad = ciudad
        self.zona = zona
        self.tipo_oferta = tipo_oferta
        self.tipo_bien = tipo_bien
        self.superficie = superficie
        self.medida = 'm2'
        self.n_habitaciones = n_habitaciones
        self.n_wc = n_wc


    def normalizeData(self):
        self.moneda = self.getMoneda()
        self.precio = self.getPrecio()
        self.superficie = self.getSuperficie()
        return

    def getMoneda(self) -> str:
        if self.precio == '':
            return ''
        moneda = self.precio.split('. ')[0]
        return moneda.replace('Desde ', '')

    def getPrecio(self):
        if self.precio == '':
            return 0
        precio =  self.precio.split('. ')[1]
        return int(precio.replace(',', ''))

    def getSuperficie(self):
        if self.superficie == '':
            return 0
        superficie = self.superficie.split('.')[0]
        if 'm2' in superficie:
            superficie = superficie.split(' ')[0]
        return int(superficie.replace(',', ''))
        