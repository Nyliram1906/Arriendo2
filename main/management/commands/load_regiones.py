import csv
from django.core.management.base import BaseCommand
from main.models import Region

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Especifica la codificación adecuada para leer el archivo
        with open('data/comunas.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Salta la primera fila (cabecera)
            nombre_regiones = set()
            regiones_a_crear = []
            for fila in reader:
                nombre_region = fila[2]
                cod_region = fila[3]
                if nombre_region not in nombre_regiones:
                    regiones_a_crear.append(Region(nombre=nombre_region, cod=cod_region))
                    nombre_regiones.add(nombre_region)
            Region.objects.bulk_create(regiones_a_crear)
            print(f"Se crearon {len(regiones_a_crear)} regiones.")




""" import csv
from django.core.management.base import BaseCommand
from main.models import Region

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open('data/comunas.csv', 'r', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader) # Se salta la primera 
        nombre_regiones = []
        for fila in reader:
            if fila[2] not in nombre_regiones:
                Region.objects.create(nombre=fila[2], cod=fila[3])
                nombre_regiones.append(fila[2])
        print(nombre_regiones) """