# Dictionary
# Sözlük objesi list, tuple gibi verileri depolayabildiğimiz başka bir yapıdır
# Sözlükler 'key' & 'value' mantığında çalışırlar
#Anahtarlar bir değere ulkaşmak için kullanılırlar

my_dict = {
    'Full Name':"Barış Sever",
    "Age": 19,
    "Sports": ["Boxing", "Football", "MMA", "NBA"],
    "Usernames" : ("PeaceLover", "PeaceLoverHD", "PeaceLover62"),
    "Books" : {
        "Dostoyevski" : ["Kumarbaz", "Suç ve Ceza", "Beyaz Geceler"]
    }
}

"""
a = my_dict["Books"]
for i in my_dict.values():
    print(i)
"""

from pprint import pprint
products = [
    {"name": "Everlast Pro Boxing Gloves", "price": 245},
    {"name": "Everlast Heavy Bag", "price": 200},
    {"name": "Everlast Pro Boxing Pads", "price": 155},
    {"name": "Everlast Pro Boxing Handwraps", "price": 200},
    {"name": "Everlast Pro Boxing Mouthpiece", "price": 95}
]
for i in products:
    if i.get("price") >= 200:
        print(f'{i.get("name")} fiyatı 200den büyüktür')
"""
print([i for i in my_dict.get("Books").get("Dostoyevski")])
"""
