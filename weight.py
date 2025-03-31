print("Welcome to weight converter")

unit_dict = {"1": "KG", "2": "LB", "3": "OZ"}

unit = input("Select a unit:\n1. KG\n2. LB\n3. OZ\nEnter choice (1-3): ")

unit = unit_dict[unit]

weight = float(input(f"Enter your weight({unit}): "))


converter = {
    "KG": {
        "Weight in LB": lambda w: w / 0.454,
        "Weight in OZ": lambda w: (w * 16) / 0.454
    },

    "LB": {
        "Weight in KG": lambda w: w * 0.454,
        "Weight in OZ": lambda w: w * 16
    },

    "OZ": {
        "Weight in KG": lambda w: (w * 0.454) / 16,
        "Weight in LB": lambda w: w / 16
    },
}

results = {key: round(func(weight), 2) for key, func in converter[unit].items()}

print(f"\nConverted Weights ({weight})({unit}):")

for key, value in results.items():
    print(f"{key}: {value}")


# def from_kg():
#     to_lb = weight / 0.454
#     to_oz = (weight * 16) / 0.454

# def from_lb():
#     to_kg = weight * 0.454
#     to_oz = weight * 16

# def from_oz():
#     to_kg = (weight * 0.454) / 16
#     to_lb = weight / 16
