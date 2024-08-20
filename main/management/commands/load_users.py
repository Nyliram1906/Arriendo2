import csv
from django.core.management.base import BaseCommand
from main.models import Comuna
from main.services import crear_user

# Se ejecuta usando python manage.py test_client

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('data/users.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  # Se salta la primera línea
            for fila in reader:
                try:
                    crear_user(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                except Exception as e:
                    self.stderr.write(f"Error al crear usuario {fila[0]}: {e}")
