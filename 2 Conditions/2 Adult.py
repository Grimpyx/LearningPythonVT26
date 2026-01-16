# I wanted to see if there was a python equivilent to C# switches in python.
# Searched up how to do it in python
def legal_status(age):
    match age:
        case age if age < 18:
            return "minor"
        case age if age < 21:
            return "adult"
        case age if age < 30:
            return "alcohol"
        case age if age < 35:
            return "senator"
        case _: # default case, meaning if no other case existed
            return "president"
        
# I expect this is the more intended method
#def legal_status(age):
#    if age < 18:
#        return "minor"
#    elif age < 21:
#        return "adult"
#    elif age < 30:
#        return "alcohol"
#    elif age < 35:
#        return "senator"
#    else:
#        return "president"