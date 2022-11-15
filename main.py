#  pip install instaloader

from datetime import datetime
import instaloader

#  Carrrega a lib e faz login com a conta desejada
L = instaloader.Instaloader()
L.login('***SEU USUARIO***', '***SUA SENHA***')

#  Carrega os dados de seguidores e seguindo do perfil escolhido
followers = instaloader.Profile.from_username(L.context, "herald.fortunato").get_followers()
followees = instaloader.Profile.from_username(L.context, "herald.fortunato").get_followees()

#  Mostra resultados
print('\n')
print('Seguidores: ' + str(followers._data['count']))
print('Seguindo: ' + str(followees._data['count']))
print('\n\n')
print('Lista e informações de seguidores:')
print('\n')
print(followers._data['edges'])