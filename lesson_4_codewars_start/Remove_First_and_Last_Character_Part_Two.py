task = """
https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python

Remove First and Last Character Part Two

This is a spin off of my first kata.

You are given a string containing a sequence of character sequences separated by commas.

Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

If the input string is empty or the removal of the first 
and last items would cause the resulting string to be empty, 
return an empty value (represented as a generic value NULL in the examples below).

"1,2,3"      =>  "2"
"1,2,3,4"    =>  "2 3"
"1,2,3,4,5"  =>  "2 3 4"

""     =>  None
"1"    =>  None
"1,2"  =>  None
"""

def array(string) -> str | None:

    if not string:
        return None

    spl = string.split(',')

    if len(spl) < 3: # <= 2
        return None

    del spl[0]
    del spl[-1]

    return ' '.join(spl)

res = array('1,2,3,4')
print(res)
res = array('0')
print(res)
res = array('1')
print(res)
res = array('1,2')
print(res)
