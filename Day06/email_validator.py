import re 
pattern = r'[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
def pattern(str):
    vaid_pattern = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]\.(edu|res\.in)$"

    if re.match(vaid_pattern, str) == None:
        return False
    else:
        return True

