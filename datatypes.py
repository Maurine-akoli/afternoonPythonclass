from typing import Tuple

number = 200  #int
second = 5.78 #double
text = "hello there" #str
ispythoninteresting=True #bool
cars= ["toyota", "nissan", "vw"] # Lists
fruits: tuple[str, str, str] =("banana", "oranges", "apple")  # Tuple
countries ={"Kenya", "Uganda", "Ethiopia"} #set
details = {
    "firstname" : "Maurine",
    "age" : 24,
    "course": "MIT",
    "nationality": "Kenyan"

}  # Dictionary
print(cars)
print(fruits)
print(countries)
print(details["nationality"] )
print(second)
print(ispythoninteresting)
# defining datatype
print(type(number))
print(type(second))
print(type(ispythoninteresting))

# Typecasting-converting from one datatype to another
print(int(second))
print(float(number))
