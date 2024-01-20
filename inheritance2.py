#1. class defination is one time process
class A():
    #1. property/variable/state
    n1=20
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method
    pass
class B():
    #1. property/variable
    n2=20 
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method
    pass
class C(A,B):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self):
     pass
    #3. function/method
    pass

#2. create class external object is many time process
c1=C()
print(c1.n1 + c1.n2)