from models.car import Car
from storage.storage import Storage

class CarService:
    @staticmethod
    def get_cars():
        data = Storage.get_all(Car.get_file_name())
        return data

    @staticmethod
    def add_car(car_name, year_of_manufacture, cars_type, self_price, selg_price):
        new_car = Car(False,car_name=car_name, year_of_manufacture=year_of_manufacture, cars_type=cars_type, self_price=self_price, selg_price=selg_price)
        Storage.add_to_file(Car.get_file_name(), new_car)
        return new_car

    @staticmethod
    def delete_by_id(id):
        Storage.delete_from_file(Car.get_file_name(), id)

    @staticmethod
    def find_by_id(id):
        return Storage.find_in_file(Car.get_file_name(), id)