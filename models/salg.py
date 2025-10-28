# Продажі:
# ● Співробітник;
# ● Автомобіль;
# ● Дата продажу;
# ● Реальна ціна продажу.
from storage.storage import Storage
import uuid
from typing import Dict
class Salg:
    file_name = 'storage/salgs.json'


    def __init__(self,id,ansatt,car,salg_date,price):
        if id == False:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.ansatt = self.ansatt_validation(ansatt)
        self.car = self.car_validation(car)
        self.salg_date = self.salg_date_validation(salg_date)
        self.price = self.price_validation(price)

    def __str__(self):
        return f"{self.ansatt} - {self.car}. Дата продажу:{self.salg_date}. Реальна ціна продажу:{self.price}"

    @staticmethod
    def get_file_name():
        return Salg.file_name

    @staticmethod
    def ansatt_validation(raw_ansatt):
        ansatt = raw_ansatt
        return ansatt

    @staticmethod
    def car_validation(raw_car):
        car = raw_car
        return car

    @staticmethod
    def salg_date_validation(raw_salg_date):
        salg_date = raw_salg_date
        return salg_date

    @staticmethod
    def price_validation(raw_price):
        price = raw_price
        return price

    def to_dict(self):
        return {
            self.id: {
                "ansatt": self.ansatt,
                "car": self.car,
                "salg_date": self.salg_date,
                "price": self.price
            }
        }

    @classmethod
    def to_obj(cls,data: Dict) -> "Salg":
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            ansatt=data.get("ansatt", ""),
            car=data.get("car", ""),
            salg_date=data.get("salg_date", ""),
            price=data.get("price", ""),
        )
