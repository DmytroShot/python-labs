from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name:str, quantity:int, price:float):
        
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(quantity) is not int:
            raise TypeError("quantity must be an integer")
        if type(price) is not float:
            raise TypeError("price must be a float")

        self.name = name
        self.quantity = quantity
        self.price = price
    
    @abstractmethod
    def requires_prescription(self) -> bool:
        pass

    @abstractmethod
    def storage_requirements(self) -> str:
        pass

    def total_price(self) -> float:
        return self.quantity * self.price

    def info(self) -> str:
        return " name: " + self.name + ", quantity: " + str(self.quantity) + ", price: " + str(self.price)


class Antibiotic(Medicine):

    def requires_prescription(self) -> bool:
        return True
    
    def storage_requirements(self) -> str:
        return "8-15°С, темне місце"


class Vitamin(Medicine):

    def requires_prescription(self) -> bool:
        return False
    
    def storage_requirements(self) -> str:
        return "15-25°С, сухо"

  
class Vaccine(Medicine):

    def requires_prescription(self) -> bool:
        return True
    
    def storage_requirements(self) -> str:
        return "2-8°С, холодильник"
    
    def total_price(self) -> float:
        return self.quantity * self.price * 1.1


