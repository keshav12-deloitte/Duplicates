import json
import inspect

from pages.HomeScreen import HomeScreen
from pages.LoginScreen import LoginScreen
from pages.PaymentScreen import paymentScreen


def generate_jsonl(classes):
    data = []

    for class_name, class_obj in classes.items():
        methods = []
        for name, method in inspect.getmembers(class_obj, inspect.isfunction):
            method_code = inspect.getsource(method)
            methods.append({
                "name": name,
                "code": method_code
            })

        data.append({
            "class_name": class_name,
            "methods": methods
        })

    with open("resources/data.jsonl", "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")


classes = {
    'HomeScreen': HomeScreen,
    'LoginScreen': LoginScreen,
    'PaymentScreen': paymentScreen
}

generate_jsonl(classes)


"""    
1 - addMethod : Method is present in HelloJi and Raja
        def addMethod(self,a, b):
            return a + b
        
        
    addMethod is exact same in both the classes.
    Method Description =  Method will return the sum of two numbers.

2 - subMethod  and subMethodaad : Similar Method is present in HelloJi and Raja
        def subMethod(self,d, e):
            return d - e
        
        def subMethodaad(self, d, e):
            a = d -e
            return a   
    subMethod and subMethodaad is similar as they both have same implementation
    Method Description =  Method will return the subtraction of two numbers.
    
"""



"""
class HelloJi:
    def addMethod(self,a, b):
        return a + b

    def subMethod(self,d, e):
        return d - e

    def is_prime(self, n):
        #Returns True if n is a prime number, False otherwise.
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
        
class Raja:
    def addMethod(self, a, b):
        return a + b

    def subMethodaad(self, d, e):
        a = d -e
        return a

    def multipyMethod(self, f, g):
        return f*g
        
Find the duplicate and similar code
"""





