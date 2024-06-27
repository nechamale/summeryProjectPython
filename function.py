import urllib.request as req, requests, re
from PIL import Image

x = requests.get('https://api.github.com/emojis').json()
links = list(x.items())
name = list(x.keys())


def print_all_icons():
    for i, n in zip(range(len(name)), name):
        print(i, ':', n)
    return name
    # number = int(input("Select the Index icon: "))
    # return links[number][1]

def search_icons_by_keyword():
    result = []
    while len(result)==0:
        search = input("insert name to search").lower()
        result = [n for n in name if re.search(search, n)]
        if len(result)==0:
            print('No results!!')
    for i, n in zip(range(len(result)), result):
        print(i, ':', n)
    return result
    # number = int(input("Select the index of icon: "))
    # return x[result[number]]


def display_icon(link):
    req.urlretrieve(link, "image.png")
    img = Image.open("image.png")
    img.show()
