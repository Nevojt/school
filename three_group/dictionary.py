
# random_list = [1, 2, 3, 4, [12, 13, 4, "hello", ["coffee", "cheese"]]]

# print(random_list[0])
# print(random_list[1])
# print(random_list[2])
# print(random_list[3])
# print(random_list[4][-1][0])

dict_list = {
    "1": "ice",
    "drink": "coffee",
    "hot": "tea",
    "list": [1, 2, 3, 4]
}

print(dict_list["list"])
dict_list["list"] = "hello"
print(dict_list["list"])

# print(dict_list["list"][2])