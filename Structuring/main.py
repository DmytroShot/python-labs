# from abc import ABC, abstractmethod
from models import Antibiotic, Vitamin, Vaccine

list = {
    Antibiotic("Streptocid",10,144.0),
    Vitamin("Vitamin A",3,24.0),
    Vaccine("Gardacil",15,104.5),
}

for item in list:
    print(item.info())

