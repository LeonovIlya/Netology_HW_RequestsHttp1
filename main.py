import requests


class Super_Hero:
    url = ' https://superheroapi.com/api/'
    access_token = '2619421814940190'

    def __init__(self, name):
        self.name = name
        self.id = ''
        self.intelligence = ''

    def get_id(self):
        self.id = requests.get(self.url + self.access_token + '/search/' + self.name).json()['results'][0]['id']
        return self.id

    def get_intelligence(self):
        if not self.id:
            self.get_id()
        self.intelligence = requests.get(self.url + self.access_token + '/' + self.id + '/powerstats').json()[
            'intelligence']
        return self.intelligence


def most_intelligence(heroes):
    for hero in heroes:
        if not hero.intelligence:
            hero.get_intelligence()
    sorted_list_of_intelligence = sorted(heroes, key=lambda hero: hero.intelligence)
    return sorted_list_of_intelligence[0]


if __name__ == "__main__":
    Super_Heroes = [Super_Hero('Hulk'),
                    Super_Hero('Captain America'),
                    Super_Hero('Thanos')]
    winner = most_intelligence(Super_Heroes)
    print(f"Самый умный - {winner.name}, его интеллект равен {winner.intelligence}")
