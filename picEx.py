from bs4 import BeautifulSoup as bs
import requests
from PIL import Image
import os

os.chdir('C:\\Users\\arenk\\Documents\\VSAI\\enemies')
directory = os.getcwd()

html = requests.get('https://vampire-survivors.fandom.com/wiki/Enemies')
soup = bs(html.text, 'html.parser')
images = soup.find_all('img')
sprites = []
for i in range(562):
    j = i + 7
    sprites.append(images[j])

for index, sprite in enumerate(sprites):
    url = sprite['data-src']
    response = requests.get(url, stream=True)
    filename = f'sprite_{index}.png'
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)
        print(f'Sprite {index} downloaded and saved as {filename}')

img = Image.open(requests.get(sprites[29]['data-src'], stream=True).raw)
