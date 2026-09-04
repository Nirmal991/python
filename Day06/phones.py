import re

def dictonary(dict_text):

    pattern = re.compile(
        r"(\d{3})-(\d{3})-(\d{4})"
        r"|\((\d{3})\) (\d{3})-(\d{4})"
        r"|(\d{3})(\d{3})(\d{4})"
    )

    result = []

    for match in pattern.finditer(dict_text):
        print(f'{match}\n')

        groups = match.groups()
        print(f'{groups}\n')

        if groups[0] is not None:
            area_code = groups[0]
            prefix = groups[1]
            line_number = groups[2]
        elif groups[3] is not None:
            area_code = groups[3]
            prefix = groups[4]
            line_number = groups[5]

        else:
            area_code = groups[6]
            prefix = groups[7]
            line_number = groups[8]

        phone = {
            "area_code": area_code,
            "prefix": prefix,
            "line_number": line_number,
            "formatted": f"({area_code}) {prefix}-{line_number}"
        }

        result.append(phone)

    return result

def main():
    directory = (
    "Contact HR at 123-456-7890 "
    "or the helpdesk at (987) 654-3210. "
    "Direct line is 5558881234."
)

    res = dictonary(directory)

    print(res)

main()