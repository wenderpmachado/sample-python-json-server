
from usuario import Usuario
from util import Util

util = Util()

usuarioWender = Usuario(1, 'Wender')
usuarioThales = Usuario(2, 'Thales')

# Envia usuario 1
r = util.enviarUsuario(usuarioWender)

# Envia usuario 2
r = util.enviarUsuario(usuarioThales)

# Obtem usuario 1
r = util.obterUsuario(usuarioWender.id)

print(r.json())

# Obtem usuario 2

r = util.obterUsuario(usuarioThales.id)

print(r.json())

# db.json output:
# {
#     "usuario": [
#         {
#             "id": 1,
#             "nome": "Wender"
#         },
#         {
#             "id": 2,
#             "nome": "Thales"
#         }
#     ]
# }
