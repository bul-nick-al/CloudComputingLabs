import vk
token = "e79eaf99ef71f54b7e954c4ee7df00b8bc0141c44e2ed826eded974ab1a6b20b95548c1c83d183c0bf9b7"
session = vk.Session(access_token=token)
api = vk.API(session)
user = api.users.getNearby(latitude=55.7519325, longitude=48.7453866, radius=2, v='5.85')
print(user)



