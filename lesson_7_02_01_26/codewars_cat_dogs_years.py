task = '''
https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
'''


def human_years_cat_years_dog_years(human_years):
    if human_years < 1:
        return None

    a = []

    while human_years >= 1 and type(human_years) == int:

        if human_years == 1:
            cat_years = 15
            dog_years = 15

        elif human_years == 2:
            cat_years = 9 + 15
            dog_years = 9 + 15
        else:
            cat_years = 24 + (human_years - 2) * 4
            dog_years = 24 + (human_years - 2) * 5

        a.append(human_years)
        a.append(cat_years)
        a.append(dog_years)

        break

    return a


def human_years_cat_years_dog_years_2(human_years: int) -> list:
    if type(human_years) != int:
        return []

    if human_years < 1:
        return []

    a = []

    if human_years == 1:
        cat_years = 15
        dog_years = 15

    elif human_years == 2:
        cat_years = 9 + 15
        dog_years = 9 + 15
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5

    a.append(human_years)
    a.append(cat_years)
    a.append(dog_years)

    return a


if __name__ == '__main__':
    res = human_years_cat_years_dog_years(3)
    print(res)
