"""

Version : 1.0

"""

import os, json

class Item :
    
    def __init__(self, name:str, price:float, code:int, amount:int=1) -> None:
        
        assert isinstance (name,str) and name 
        assert isinstance (price, float) and price 
        assert isinstance (code, int) and code 
        assert isinstance (amount, int)
        
        self.__name = name
        self.__price = price
        self.__code = code 
        self.__amount = amount 

    # Getter
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_code(self):
        return self.__code
    
    def get_amount(self):
        return self.__amount
    
    # Setter
    
    def set_name(self, n_name:str):
        assert isinstance(n_name, str) and n_name
        self.__name = n_name
        
    def set_price(self, n_price:float): 
        assert isinstance(n_price, float) and n_price
        self.__price = n_price
        
    def set_code(self, n_code:int):
        assert isinstance(n_code, int) and n_code
        self.__code = n_code
        
    def set_amount(self, n_amount:int):
        assert isinstance (n_amount, int) and n_amount
        self.__amount = n_amount
        
        
        
    # Methodes produits :
    
    def calcul_promotion (self, pourcentage:int):
        assert isinstance (pourcentage, int)
        return self.__price * (pourcentage / 100)

    
    
    
        
test = Item('Tomate Ronde', 1.0,10,50)
print(test.calcul_promotion(50))
print (test.get_price())

test.set_price(test.calcul_promotion(50))
print (test.get_price())

        
                
        