import re

some_data = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
# pattern = r"(?P<user>\b[a-zA-Z0-9-._]+)@(?P<host>([a-z-]{2,}).([a-z.]{2,})+)"

valid_emails = [el.group() for el in re.finditer(pattern, some_data)]
print('\n'.join(valid_emails))