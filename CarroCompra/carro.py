class Carro:
    def __init__(self, request):
        self.request = request #almacenamos peticion
        self.session = request.session #almacenamos la sesion
        carro=self.session.get("carro")
        if not carro:
            #el carro lo hacemos como diccionario que tendra par {id:producto} 
            carro=self.session["carro"]={}
        self.carro = carro
    def agrega_prod(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio), #convertimos el precio a string para bbdd
                "cantidad":1, #inicialmente la cantidad es 1
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar_carro()
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified = True
    def eliminar_prod(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    def restar_prod(self, producto):
        for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-producto.precio
                    if value["cantidad"]<1:
                        self.eliminar_prod(producto)
                    break
        self.guardar_carro()
        
    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True