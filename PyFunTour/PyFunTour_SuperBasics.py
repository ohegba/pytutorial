# This is a comment. Not on life or anything, but within the program data.

a_number = 3.14
a_nothernumber = a_number * 2

import math

pi = math.pi
almost_pi = round(pi, 2)

eq_approx_pi = (a_number == almost_pi)
falsity = not(eq_approx_pi)
truthiness = not(falsity)

_7mod3 = 7 % 3
_7floor3 = 7 // 3
_7pow3 = 7 ** 3
_7div3 = 7 / 3
_7add3 = 7 + 3
_7mul3 = 7 * 3
_7sub3 = 7 - 3

a_string = 'I am a String, aren\'t I?'
a_string_2 = "I am a String, aren't I?"
a_long_string = """The line continuation character is \\, don't you \
know?"""

eq_string1_string2 = a_string == a_string_2

lava = 'Pa' + "hoe" * 2
lava += " is a type of lava, yeah?"

letter_P = lava[0]
letter_Q = lava[-1]

spirit = 'redrum'
spirit_reveal_thyself = spirit[::-1]
exorcised_spirit = spirit[-1:-4:-1] * 2

exotic_fruit = 'Pineapple'
common_tree = exotic_fruit[:4]
common_fruit = exotic_fruit[4:]

boastful_word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
boastful_word_contest = len(boastful_word)

shopping_list = ['Butter', 'Milk', 'Eggs']
shopping_list[1] = 'Margarine'
shopping_list.append('Digital Voice Recorder (as seen on TV!)')
shopping_list[:] = shopping_list[:-1]

list_containing_a_list = ['a','b', ['a','b','c']]
alphabet_start = list_containing_a_list[2][0:2]

def timestwo(a):
    value = a * 2
    return value

def timestwo_ntimes(a,n):
    while n > 0:
        a = timestwo(a)
        n -= 1
    return a

four = timestwo_ntimes(2,1)
string_two = "Two"

elementary_math = (string_two + " times " + string_two + " = " + str(four))
text_editor = "Atom"
