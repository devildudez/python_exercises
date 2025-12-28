task = """
https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/python

Swap Values

I would like to be able to pass an array with two elements to my swapValues 
function to swap the values. However it appears that the values aren't changing.

Can you figure out what's wrong here?
"""

def swap_values(lst: list) -> list:
    lst[0], lst[1] = lst[1], lst[0]
    return lst
