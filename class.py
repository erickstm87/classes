#!/usr/bin/python
#Author Tommy Erickson
#Class writing practice taken from https://github.com/karan/Projects#classes

class Product:
    def __init__(self,price,p_id,quantity):
        self.price = price
        self.p_id = p_id
        self.quantity = quantity
   
#class Inventory:

gramophone = Product(20,'instrument',13)     
print gramophone.price



