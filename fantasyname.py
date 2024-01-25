import random
from namegen import last_name


prefix = ['fart','poop','crack','dingle','shit','ass','dookie','jizz','wang','dong','weiner','piss',
'butt','diarrhea','anal','dick','toilet','filth','flop','cunt','gape','boner','fuck','stank','plop','dung','crap','snot']

ruler_title = ['lord','king','master','prince','duke','baron','knight','fuhrer','monger','wizard']

race_suffix = ['kin', ' Elves', 'folk', ' Lords', 'lings', 'whackers', 'breed', 'wipers', 'sniffers', ' Midgets', ' Fathers', ' Serpents', ' Kings', 'blood', 'stains', 'gardeners']

def ruler():
    title = f'{random.choice(ruler_title).title()}'
    return title

def race():
    race_name = f'{random.choice(prefix).title()}{random.choice(race_suffix)}'
    return race_name

def full_ruler():
    return f"{last_name()}, {ruler()} of the {race()}"

if __name__ == '__main__':
    print(f'Hail {last_name()} {last_name()}, {ruler()} of the {race()}')
