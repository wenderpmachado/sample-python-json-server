import requests

class Util:
    def obterUrlAPI(self):
        return 'http://localhost:3000/'

    def obterEndpointUsuario(self):
        return self.obterUrlAPI() + 'usuario/'

    def obterEndpointUsuarioComID(self, id):
        return self.obterEndpointUsuario() + str(id)

    def enviarUsuario(self, usuario):
        return requests.post(url=self.obterEndpointUsuario(), json=usuario.toJson())

    def obterUsuario(self, id):
        return requests.get(url=self.obterEndpointUsuarioComID(id))
