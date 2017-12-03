# using 'as' in import to give a function an alias
from pizza import make_pizza_three as mp3, make_pizza_two as mp2

mp3(16, "pepperoni", "cheese")
mp2("green peppers", "olive", "pineapple")
