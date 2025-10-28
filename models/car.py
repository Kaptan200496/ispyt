# Автомобіль:
# ● Назва виробника;
# ● Рік випуску;
# ● Модель;
# ● Собівартість;
# ● Потенційна ціна продажу.
import uuid
from typing import Dict

class Car:
    cars = {}
    file_name = 'storage/cars.json'
    def __init__(self, id, car_name, year_of_manufacture, cars_type, self_price, selg_price):
        if id == False:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.car_name = self.year_validation(car_name)
        self.year_of_manufacture = self.car_name_validation(year_of_manufacture)
        self.cars_type = self.cars_type_validation(cars_type)
        self.self_price = self.self_price_validation(self_price)
        self.selg_price = self.selg_price_validation(selg_price)

    def __str__(self):
        return f"{self.car_name} - {self.year_of_manufacture}. Тип: {self.cars_type}. Собівартість:{self.self_price}. Потенційна ціна продажу:{self.selg_price}"

    @staticmethod
    def get_file_name():
        return Car.file_name

    @staticmethod
    def car_name_validation(raw_car_name):
        car_name = raw_car_name
        return car_name

    @staticmethod
    def year_validation(raw_year_of_manufacture):
        year_of_manufacture = raw_year_of_manufacture
        return year_of_manufacture

    @staticmethod
    def cars_type_validation(raw_cars_type):
        cars_type = raw_cars_type
        return cars_type

    @staticmethod
    def self_price_validation(raw_self_price):
        self_price = raw_self_price
        return self_price

    @staticmethod
    def selg_price_validation(raw_selg_price):
        selg_price = raw_selg_price
        return selg_price


    def to_dict(self):
        return {
            self.id: {
                "car_name": self.car_name,
                "year_of_manufacture":self.year_of_manufacture,
                "cars_type":self.cars_type,
                "self_price": self.self_price,
                "selg_price":self.selg_price
            }
        }

    @classmethod
    def to_obj(cls, data: Dict) -> "Car":
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            car_name=data.get("car_name", ""),
            year_of_manufacture=data.get("year_of_manufacture", ""),
            cars_type=data.get("cars_type", ""),
            self_price=data.get("self_price", ""),
            selg_price=data.get("selg_price", "")
        )


