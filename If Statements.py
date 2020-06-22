
is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You are either not male or not or not both")
elif not(is_male) and (is_tall):
    print("You are tall but not a male")