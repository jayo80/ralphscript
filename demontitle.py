from namegen import full_name
from random import choice as rc
from time import sleep

prefix = ['shart','rectal','booger','turd','flop','fecal','plop','fart','poop','crack','dingle','shit','ass','dookie','jizz','wang','dong','weiner','piss',
'butt','diarrhea','anal','dick','toilet','filth','flop','cunt','gape','boner','fuck','stank','plop','dung','crap','snot','urine','doodoo','wang','dong']

title = [
    "Herald",
    "Emissary",
    "Lord",
    "Envoy",
    "Messenger",
    "Harbinger",
    "Prophet",
    "Revelator",
    "Servant",
    "Revenant",
    "Acolyte",
    "Knight",
]

adj = [
    "Endless",
    "Nameless",
    "Foul",
    "Stinking",
    "Reeking",
    "Infernal",
    "Eternal",
    "Rancid",
    "Unclean",
    "Noxious",
    "Fathomless",
    "Formless",
]

place = [
    "Void",
    "Depths",
    "Abyss",
    "Night",
    "Putrescence",
    "Gulf",
    "Pit",
    "Abode",
    "Realm",
    'Crapulence',
    'Flatulence',
    'Feculence',
    'Doodoo Hole',
]

def demon_name():
    return f"{full_name()}, {rc(prefix).capitalize()}{rc(title).lower()} Of The {rc(adj)} {rc(place)}"

if __name__ == "__main__":

    def demons():
        x = int(input("How Many Names: "))
        for i in range(x):
            print(demon_name())
            sleep(2)

    demons()

