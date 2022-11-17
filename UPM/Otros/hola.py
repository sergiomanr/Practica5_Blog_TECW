'''def city_country(city_name,country_name):
    city_location = f'{city_name}, {country_name}'
    return city_location.title()
while True:
    print("\nTell me where are you from")
    city_name = input("Name your city: ")
    if city_name == 'q':
        break
        print("\n---Poll results---")
        print("Hello")
    country_name = input("Name the country: ")
    if country_name == 'q':
        break
    place_of_residenece = city_country(city_name,country_name)
    print(place_of_residenece)'''


# def make_album(artits_name,album_name,number_of_songs=None):
#     artits_name = input("\nWrite the artists name: ")
#     album_name = input("\nWrite the album's name: ")
# whirue:
#     if number_of_songs
#         album_info = f"{artits_name},{album_name},{number_of_songs}"
#     else:
#         album_info = f"{artits_name},{album_name}"
#     album_info = make_album(artits_name,album_name)
    
'''
albums ={}
def make_album(artits_name,album_name,number_of_songs=None):
    if number_of_songs:
        album_info = {'artist':artits_name, 'album': album_name,'number':number_of_songs}
    else:
        album_info = {'artist':artits_name, 'album': album_name}
    return album_info

while True:
   print("\n(enter 'q' at any time to quit)")
   artists_name = input("Write the artists name: ")
   if artists_name == 'q':
    break
   album_name = input("Write the album's name: ")
   if album_name == 'q':
    break
   albums.append(album_name)
   make_album(artists_name,album_name)
'''
matriz = [1,2,3,5,7,2]
for numeros in matriz:
    print(numeros)
print(len(matriz))