import json
from models.employee import Employee
from models.car import Car
# from models.salg import Salg
class JsonStorage:

    @staticmethod
    def data_transform(filename):
        with open (filename, "r+", encoding='utf-8') as file:
            data = json.load(file)
        obj_of_array = [data[d] for d in data]
        return obj_of_array
