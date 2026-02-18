######## 1. Type Annotations #########

#-- Typed Dictionary
#values must and should be the same defined data type
from typing import TypedDict
class Actor(TypedDict):
    name : str
    age : int

actor = Actor(name = "Arjun", age = "43")

#--Union
#values must and should be one of the datatypes mentioned in Union.
from typing import Union
 
def square(x: Union[int,float]) ->float:
    return x*x


#--Optional
#values must and should be either str or None
from typing import Optional

def hi(name : Optional[str]) ->None:
    if name is None :
        print("hey there")
    else:
        print("hey there {name}")

#--Any
#values contain any datatype - simple right!

from typing import Any
def value(x:Any):
    print(x)


#--lambda function

n =[1,2,3,4]
s=list(map(lambda a: a*a, n))