import requests
import json
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Product import Product
from Restaurant import Restaurant


class App():
    def __init__(self):
        self.Equipos= []
        self.Partidos = []
        self.Estadio = []
        self.Restaurants = []
        self.Productos = []
        self.Bebida = []
        self.Comida = []

    def run(self):
        self.api()

    def api(self):
        #equipo
        URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        response = requests.get(URL)
        response = response.json()
        
        for equipo in response:
           nuevo = Equipo(equipo["id"], equipo["code"], equipo["name"], equipo["group"])
           self.Equipos.append(nuevo)

        #estadio
        URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        response = requests.get(URL)
        response = response.json()

        for estadio in response:
            nuevo = Estadio(estadio["id"], estadio["name"], estadio["city"], estadio["capacity"])
            
            listado_restaurante = []
            for restaurante in estadio["restaurants"]:
                nuevo_restaurante = Restaurant(restaurante["name"])
                
                listado_productos = []
                for producto in restaurante["products"]:
                    nuevo_producto = Product(producto["name"], producto["quantity"], producto["price"], producto["stock"], producto["adicional"])
                    listado_productos.append(nuevo_producto)

                nuevo_restaurante = listado_productos

            self.Estadio.append(nuevo)

        #partido 
        URL = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        response = requests.get(URL)
        response = response.json()

        for partido in response:
            nuevo = Partido(partido["id"],partido ["number"], partido["home"], partido["away"], partido["date"], partido ["group"], partido["stadium_id"])
            for equipo in self.Equipos:
                if partido["home"]["id"] == equipo.id:
                    nuevo.home = equipo
            for equipo in self.Equipos:
                if partido["away"]["id"] == equipo.id:
                    nuevo.away = equipo
            for estadio in self.Estadio:
                if partido["stadium_id"] == estadio.id:
                    nuevo.stadium_id = estadio

             
            self.Partidos.append(nuevo)
        
        
        