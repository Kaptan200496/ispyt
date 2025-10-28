# ● ПІБ;
# ● Посада;
# ● Контактний телефон;
# ● Email.
import uuid
from typing import Dict
class Employee:
    staff = {}
    file_name = 'storage/staff.json'

    def __init__(self,id,fio,position,tlf,email):
        if id == False:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.fio = self.fio_validation(fio)
        self.position = self.position_validation(position)
        self.tlf = self.tlf_validation(tlf)
        self.email = self.email_validation(email)
    def __str__(self):
        return f"{self.fio} - {self.position}. Номер телефону: {self.tlf}. Email:{self.email}"

    @staticmethod
    def get_file_name():
        return Employee.file_name

    @staticmethod
    def fio_validation(raw_fio):
        fio = raw_fio
        return fio

    @staticmethod
    def position_validation(raw_position):
        position = raw_position
        return position

    @staticmethod
    def tlf_validation(raw_tlf):
        tlf = raw_tlf
        return tlf

    @staticmethod
    def email_validation(raw_email):
        email = raw_email
        return email

    def to_dict(self):
        return {
            self.id: {
                "fio": self.fio,
                "position": self.position,
                "tlf": self.tlf,
                "email": self.email
            }
        }

    @classmethod
    def to_obj(cls,data: Dict) -> "Employee":
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            fio=data.get("fio", ""),
            position=data.get("position", ""),
            tlf=data.get("tlf", ""),
            email=data.get("email", ""),
        )

