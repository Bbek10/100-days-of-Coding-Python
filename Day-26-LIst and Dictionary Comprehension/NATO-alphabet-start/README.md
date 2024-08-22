#DAY 26 List Comprehension
new_list = [`new_item` for `item` in `list`]

https://leetcode.com/problems/sort-array-by-parity/description/

`numbers = [1,2,3]`

`new_list = []`

`for n in list:`

`add_1 = n+1`

`new_list.apped(add_1)`

this can be writtena as:

numbers = [1,2,3]

new_list = [n+1 `for` n `in` numbers]

## CONDITIONAL LIST COMPREHENSIOn

new_list = [new_item `for` item `in` list `if` test]

names = ["Alex","Beth","Eleanor","CAROLINE","Freddie"]

long_captial_names = [name.upper() for name in names if len(name) > 5]

`missing_states = []`

`for state in all_states:`    

`if state not in guessed_state:`        

`missing_states.append(state)`

This code from day 25 can be cut down to 1 line

`missing_states = [state for state in all_states if state not in guessed_state ]`

#HOW TO USE DICTIONARY COMPREHENSION

new_dict = {`new_key`:`new_value` for `item` in `list`}

or

 

new_dict = {`new_key`:`new_value` for `(key, value)`in dict.items()}

conditon

new_dict = {`new_key`:`new_value` for `(key, value)`in dict.items() if `test`}

**Dictionary Comprehension 1**

You are going to use Dictionary Comprehension to create a dictionary called `result` that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.  *

- Do NOT** Create a dictionary directly.

Try to use **Dictionary Comprehension** instead of a Loop.

To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.

`sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_list = sentence.split()
result = {word:len(word) for word in new_list}`

**Dictionary Comprehension 2**

You are going to use Dictionary Comprehension to create a dictionary called `weather_f` that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert `temp_c` into `temp_f` use this formula:

`(temp_c * 9/5) + 32 = temp_f`

`weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}`

`weather_f = {day:(temp_c *9/5)+32 for day,temp_c in weather_c.items()}`

`print(weather_f)`

import pandas
student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

#Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
#Access index and row
# print(index, row)
#Access row.student or row.score
# print(row.student)
pass

Keyword Method with iterrows()

{new_key:new_value for (index, row) in df.iterrows()}