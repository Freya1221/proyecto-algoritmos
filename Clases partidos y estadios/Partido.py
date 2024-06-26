class Partido ():
    def __init__(self, id, number, home, away, date, group, stadium_id):
        self.id = id
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.stadium_id = stadium_id
     

    def show(self):
        print(f'''
ID: {self.id}
NUMBER: {self.number}
GROUP: {self.group}
STADIUM_ID: {self.stadium_id}
FECHA: {self.date}
EQUIPO_LOCAL: {self.home}
EQUIPO_VISITANTE: {self.away}
''')
