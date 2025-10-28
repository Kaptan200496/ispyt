import json
from storage.json_storage import JsonStorage

class Storage:
    @staticmethod
    def add_to_file(filename,obj):
        inf = obj.to_dict()
        with open(filename, "r+", encoding='utf-8') as file:
            information = file.read()
            if information == "":
                cur_information = {}
            else:
                cur_information = json.loads(information)
                file.seek(0)
            cur_information.update(inf)
            file.write(json.dumps(cur_information))
        print("Запис успішно доданий.")

    @staticmethod
    def delete_from_file(filename, id):
        with open(filename, "r+", encoding='utf-8') as file:
            information = file.read()
            file.truncate(0)
            file.seek(0)
            if information == "":
                print(f"Записів у базі немає.")
            else:
                information = json.loads(information)
                del information[id]
                file.write(json.dumps(information))
                print(f"Запис успішно видалений.")

    @staticmethod
    def get_all(filename):
        objects_array = JsonStorage.data_transform(filename)
        return objects_array

    @staticmethod
    def find_in_file(filename, id):
        with open(filename, "r+", encoding='utf-8') as file:
            information = file.read()
            if information == "":
                print(f"Записів у базі немає.")
            else:
                information = json.loads(information)
                return information[id]
            print(f"Запис не знайдено.")
