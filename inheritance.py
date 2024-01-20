#1. Class defination is one time process
class A():
    #1. property/variable
    name=""
    #2. constructor/esp.function
    def __init__(self,n):
        self.name=n
        pass
    #3. function/method
    pass
#1. Class defination is one time process
#class Child(Parent)
class B(A):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method
    pass
#1. class defination is one time process
#class Child(Parent)
class C(A):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    #3. function/method
    pass
#1. class defination is one time process
#class Child(Parent)
class D(B):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method
    pass
#1. class defination is one time process
# class Child(Parent)
class E(B):
    #1. property/variable/states
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method/behaviour
    pass
#1. class defination is one time process
class F(C):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/behaviour
    pass
class G(C):
    #1. property/states/variable
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)
        pass
    #3. function/behaviour
    pass
class H(C):
    #1. property/variable/states
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method/behaviour
    pass
class I(G):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self):
        pass
    #3. function/method
    pass
class J(G):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self,n):
        super().__init__(n)

        pass
    #3. function/method
    pass

#2. create class external object is many time process
j1=J("Vishal")
print(f'My name is {j1.name}')