with open("./Input/Letter/letter.txt") as file:
    letter_contents = file.read()
    print(letter_contents)

with open("./Input/Names/names.txt") as name_data:
    names_list = name_data.read()
    # names_list.split(" ") or str.strip()
    print((names_list.split("\n")))
    print(len(names_list.split("\n")))
    # or simply use
    # names_list = name_data.readlines()

req_names = (names_list.split("\n"))

for i in req_names:
    # letter_contents.replace("[name]", i)
    file_name = "letter_for_" + i + ".txt"
    with open(f"./Output/{file_name}", mode="w") as w_file:
        w_file.write(letter_contents.replace("[name]", i))
