# """Demonstrating the capabilities of a dictionary."""


# # declaring the type of a dictionary
# schools: dict[str, int]

# # intialize to an empty dictionary
# schools = dict()

# # set a key-value pairing
# schools["UNC"] = 19400
# schools["Duke"] = 6717
# schools["NCSU"] = 26150

# # print a dictionary literal
# print(schools)

# # access a value bu its key (perform a look-up)
# print(f"UNC has {schools['UNC']} students")

# # remove a key-value pairing by its key
# schools.pop("Duke")

# # test for the existence of a key
# is_Duke_present: bool = "Duke" in schools
# print(f"Duke is present: {is_Duke_present}")

# # to reassign a key-value pairing
# schools["UNC"] = 20000
# schools["NCSU"] += 100

schools: dict[str, int]
schools = {
    "UNC": 19400,
    "Duke": 6717,
    "NCSU": 26150
}

for key in schools:
    print(f"Key: {key}, Value: {schools[key]}")