task = '''
In this kata you will have to write a function that takes 
litres and price_per_litre (in dollar) as arguments.

- Purchases of 2 or more litres get a discount of 5 cents per litre, 
- purchases of 4 or more litres get a discount of 10 cents per litre, 
- and so on every two litres, up to a maximum discount of 25 cents per litre.
- But total discount per litre cannot be more than 25 cents. 

Return the total cost rounded to 2 decimal places.
Also you can guess that there will not be negative or non-numeric inputs.

Good Luck!

Note
1 Dollar = 100 Cents
'''

def fuel_calc(litres: int, price_per_litre: int) -> float:

    if litres <= 0 and type(litres) != int:
        return 0.0

    if price_per_litre <= 0 and price_per_litre is not int:
        return 0.0

    discount = 0
    litres_copy = litres

    while litres_copy >= 2:

        if discount >= 25:
            break
        if litres_copy >= 2 and litres_copy < 4:
            discount += 5
        if litres_copy >= 4 and litres_copy < 6:
            discount += 10
        if litres_copy >= 6:
            discount += 5

        litres_copy -= 2
    #
    # if litres >= 8:
    #     price_per_litre -= 5
    # if litres >= 6 and litres <= 8:
    #     price_per_litre -= 5
    # if litres >= 4 and litres < 6:
    #     price_per_litre -= 10
    # if litres < 4 and litres >= 2:
    #     price_per_litre -= 5
    #
    # total_price = price_per_litre * litres

    price_per_litre = price_per_litre - discount
    total_price = price_per_litre * litres

    return round(total_price, 2)

print(fuel_calc(10, 30))
