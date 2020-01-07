def rightStrip(input, remove):
    last_char = input[-1]

    while last_char in remove:
        input = input[:-1]
        last_char = input[-1]
    return input


test = "iapojjoisjo"
print(f"{test}.")

print(rightStrip("iapojjoisjo", "oisj"))
print(f"""{test.rstrip("oisj")}""")
