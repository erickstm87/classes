#!/usr/bin/python
#Author Tommy Erickson
#Class writing practice taken from https://github.com/karan/Projects#classes

class Product:
    #general note: init is called because it will call an instance of the object. An object can have ''class attributes'' which are outside of the init function and apply to all instances of the object and an object can have 'instance attributes' which are things that need to be assigned every time the instance is called
    def __init__(self,price,p_id,quantity):
        self.price = price
        self.p_id = p_id
        self.quantity = quantity

