url = 

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')

print(type(card_list), type(card_list[0]))

games = []

for i in card_list:
    cards = i.select('div.card')
    print(">>>", len(cards))
    for c in cards:
        games.append