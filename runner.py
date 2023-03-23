# import calculator # original syntax needs to have the calculator. ""
from maths.calculator import add, subtract # if using this then dont need to use "calculator" before add
# from calculator import * # adds all functions from the calculator module (dont use because too many functions?)


result = add(1,2)  #have to add refer to the calculator module in order to let it work in file
result2 = subtract(3,1)
print(result)
print(result2)


# import calculator as safe_calculator (gives calculator an alias) ONLY IN THIS FILE
# would use result1 = safe_calculator.add(1,2)


