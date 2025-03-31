"""
dictionary  = {"key": value, "boolean": True}
"""

units = {"1": "KG", "2": "LB", "3": "OZ"}


dict_comp = {key: value for key, value in units.items()}



print(dict_comp)


"""
.keys()
.values()
.items()
"""

choice = "my name"

#print(units[choice])

def add(num1, num2):
    result = num1 + num2
    return result
add(1, 1)

lambda num1, num2: num1 + num2

def to_lb(w):
    result = w / 0.454
    return result

lambda w: w / 0.454
