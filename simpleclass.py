# Basic program that creates a class and a method

# create a class called "Person"
class Person:
# Create method "hello"
# Note: must use 'self' in parameter list
def hello(self):
  print "Hello world!"
 
# create object "bob" of class "Person"
bob = Person()

# call method "hello" on object "bob"
bob.hello()
