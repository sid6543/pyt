Dic = {
    'name' : 'Siddharth',
    'address' : 'Minnesota',
    'phone number' : [7047474710],
    'education' : 'Graduate',
    'university' : 'St Cloud State University',
    'country of residence' : 'America',
    'nationality' : 'India',
 }
# print(Dic.keys())
# print(Dic.values())
# print(Dic.items())
# print(Dic)
friends = {
    'Sasuke' : 'Friend',
    'Naruto' : 'Friend',
    'Sakura' : 'Friend',
    'Kakashi' : 'Friend',
}
# Dic.update(friends) # Updates the dictionary by adding key value pair from update function
# print(Dic)

print(Dic.get("name1")) # Returns none as name1 is not present in the dictionary.
print(Dic["name1"]) # Throws error as name1 is not present in the dictionary.


