from superhero import Super_hero
from pprint import pprint

thanos = Super_hero()
thanos.name = 'Thanos'
iron_man = Super_hero()
iron_man.name = 'Iron Man'
hulk = Super_hero()
hulk.name = 'Hulk'
cap = Super_hero()
cap.name = 'Captain America'

# pprint(thanos.find_the_hero())
# pprint(hulk.find_the_hero())
# pprint(cap.find_the_hero())

# pprint(thanos.find_intelligence())
# pprint(hulk.find_intelligence())
# pprint(cap.find_intelligence())
# pprint(iron_man.find_intelligence())

print(cap.find_the_most_intelligent(hulk, thanos))