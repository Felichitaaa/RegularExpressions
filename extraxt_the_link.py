import re
text = input()
valids = []
pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
while text:
    valid_sites = [el.group() for el in re.finditer(pattern, text)]
    valids.extend(valid_sites)
    text = input()
print(*valids, sep="\n")