import requests
from pprint import pprint


class Super_hero:
    name = ''
    intelligence = ''

    def find_the_hero(self):
        url = f'https://superheroapi.com/api/2619421814940190/search/{self.name}'
        r = requests.get(url)
        return r.json()

    def find_intelligence(self):
        data = self.find_the_hero()
        for param in data['results']:
            for k, v in param.items():
                if k == 'powerstats':
                    for stat, measure in v.items():
                        if stat == 'intelligence':
                            intelligence = int(measure)
        self.intelligence = intelligence
        return intelligence

    def find_the_most_intelligent(self, *heroes):
        dict = {}
        dict[self.name] = self.find_intelligence()
        for hero in heroes:
            if isinstance(hero, Super_hero):
                intelligence = hero.find_intelligence()
                dict[hero.name] = intelligence
        best_intelligence = max(dict.values())
        for k, v in dict.items():
            if v == best_intelligence:
                return f'The most intelligent Superhero - {k}'
