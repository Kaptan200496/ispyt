from models.salg import Salg
from storage.storage import Storage

class SalgService:
    @staticmethod
    def get_salgs():
        data = Storage.get_all(Salg.get_file_name())
        return data

    @staticmethod
    def add_salg(ansatt,car,salg_date,price):
        new_salg = Salg(False,ansatt=ansatt, car=car, salg_date=salg_date, price=price)
        Storage.add_to_file(Salg.get_file_name(), new_salg)
        return new_salg

    @staticmethod
    def delete_by_id(id):
        Storage.delete_from_file(Salg.get_file_name(), id)

    @staticmethod
    def find_by_id(id):
        return Storage.find_in_file(Salg.get_file_name(), id)