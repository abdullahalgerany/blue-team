import re
failed_pattern = re.compile(r"failed password", re.IGNORECASE)
with open("SUSPICIOUS.txt", "r") as file:
    for line in file:
        line = line.strip()
        if failed_pattern.search(line):
            print(line)