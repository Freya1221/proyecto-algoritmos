class Partido ():
    def __init__(self, id, number, home, code, name, group, stadium_id, fecha, hora, equipo_local, equipo_vistante):
        self.id = id
        self.number = number
        self.home = home
        self.code = code
        self.name = name
        self.group = group
        self.stadium_id = stadium_id
        self.fecha = fecha
        self.hora = hora
        self.equipo_local = equipo_local
        self.equipo_vistante = equipo_vistante

    def show(self):
        print(f'''
ID: {self.id}
NUMBER: {self.number}
HOME: {self.home}
CODE: {self.code}
NAME: {self.name}
GROUP: {self.group}
STADIUM_ID: {self.stadium_id}
FECHA: {self.fecha}
HORA: {self.hora}
EQUIPO_LOCAL: {self.equipo_local}
EQUIPO_VISITANTE: {self.equipo_vistante}
''')
