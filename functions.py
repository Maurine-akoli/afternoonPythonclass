# User-defined functions
def greeting():
    print('Hello World')


greeting()  # Calling a function


def add():
    print(5 + 8)


add()


# Parameters and arguments
def student(firstname, course, age):
    print(firstname, course, age)


student("Job", "Datascience", "23")
student("Ann", "Cybersecurity", "30")
student("Jeff", "MIT", "12")

# Built-in function
y = max(89, 78, 23, 13, 70)
print(y)

x = min(67, 98, 54, 30)
print(x)

z = pow(2, 3)
print(z)
