import math

s = "chillout"

def encryption(s: str) -> str:
   
    # remove spaces in string
    s_no_space = s.replace(" ", "")
    
    # compute bottom and ceiling
    rows = math.floor(len(s_no_space)**0.5)
    columns = math.ceil(len(s_no_space)**0.5)
 
    # prepare finishing vars
    str_length = len(s_no_space)
    if rows * columns < str_length: rows += 1

    final_string = ""
    for i in range(columns):
        final_string += "".join([
            s_no_space[i+x*columns] for x in range(rows)
            if i+x*columns < str_length 
        ])
        final_string += " "
    print(final_string.rstrip())

encryption(s)
