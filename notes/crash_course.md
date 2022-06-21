- can use quotes in strings interchangeably
like "quote 'name'" and 'quote "name"'

- old way is to use format
"his name is {a} {b}".format(a, b)

- can use fstrings for assignment
a = f"{b} called {c}"

- can use underscores for numbers
n = 3.14_15_926

- multiple assignments
x_old, y_old = x, y

- constants
CONSTANT_X = 3.14

- [comments](https://hn.algolia.com/?dateRange=all&page=0&prefix=true&query=code%20comments&sort=byPopularity&type=story)
is this comment adding something meaningdul?
docstrings

- python lists are *powerful*
different types of objects
support *slices* and flexible indexing
a[-1]
a[1:9:5]
etc

insert(pos, value)
pop()
pop(indx)
del a[ind]
use pop if want to use and remove
otherwise del
remove() for remove by value

- range(1,100)
a = [i for i in range(1,100)
a = list(range(1,100))

- can loop through slice
for i in a[-3:]

- copy list (b = a is ref assign)
a2 = a[:]
a3 = a.copy()


- tuples are *immutable*
(1, 2)
one element tuple defined (1,)
can loop through

- style guide
pep8 is the style guide
easier to read > easier to write
use 4 spaces for indentation
tab should be set to insert spaces

- if el in x or el not in x


- dictionary use get('val', 'No val')
best way to loop through dict

- can nest dicts/lists inside dicts
for user, user_info in d.items()
for username, user_info in users.items():
thats how we loop through nested


- remove multiple values from list
while 'cat' in pets:
 pets.remove('cat')
BAD


- function arguments types
positional order matters
keyword order doesnt matter
default values (do after pos in defenition)
what is THE right way to design function api/interface???


- can make str arg "optional" just defined string = ''
otherwise None?


- preventing a function changing a list
pass list[:] to function

- random number of args
use *args
*args - make an empty tuple
than pack all the argumenets into that tuple
it would be a tuple even with 1 value
\* unpacks tuple??

**kwargs - any number of key=pair
def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
u user_info['first_name'] = first
 user_info['last_name'] = last
 return user_info
user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
 You’ll often see the parameter name **kwargs used to collect non-specific keyword
arguments.


- function allow to decompose
we can put functions into modules
those are just files into some folder
we import file e.g pizza and use pizza.make_pizza()
module_name.function_name()
that makes every function from module avaliable in program


- import specific functions
from module import function


dont use from module import *

- give alias to a function
from numpy import dot as dotka


- give alias to a module
import numpy as np
import scipy as sp
import skickit.learn as sk
if alias used no longer availabel old names?
if all stuff needed -> import module
if specific -> import specific
all import should be on the top (exceptions are comments)

- def too_big(ppositional1positional1positional,
	      1ositional1, positional1, positional1):

- object oriented programming
class as user defined type
object as particular instance of class

- function that is a part of class is *method*
__init__() is default Python's method that is used when instance of class is created
magic methods (__ asd __ )
double underscore used to avoid name clashes
each method takes self
self is a reference to an instance of class
variables that are accessible through instances are *attributes*
instance = Dog(name, age) --> calls __init__ with name, age and returns new object ref
class.attribute
class.method()
[magic](https://rszalski.github.io/magicmethods/)


- inheritance
*parent* class -> *child* class
*superclass* -> *subclass*
class Child(Parent):
    super.__init__(a,b)

*override* methods in child class by same name
attributes can be class instances

When you wrestle with questions like these, you’re thinking at a higher
logical level rather than a syntax-focused level. You’re thinking not about
Python, but about how to represent the real world in code. When you reach
this point, you’ll realize there are often no right or wrong approaches to
modeling real-world situations. Some approaches are more efficient than
others, but it takes practice to find the most efficient representations.

- as well as functions we can split classes into modules
you should add docstrings on top of each module
can import single class
all module
all classes
also can use aliases


- python standard library
random not good enough for security related stuff
classes should be CamelCase
they should contain doctstring briefly describing
also its good to write docstring for functions


- files and exceptions
look in this dir by default
windows uses \ but you can still use /
need use \\ insted of just \ cause \ is used for escape
with open path as file:
     content = file.read()
such code will automatically close file
we can manually close but that is more bug prone (close too fast or never close)??
for line in file:
    print(line)
when python reads data i interprets it as string
you can convert it to int


- readline() all lines
- open() as whole
- open() and for line in file
file modes are r, w, a and r+ (read, write, append, rw)

try
except Exception
else
