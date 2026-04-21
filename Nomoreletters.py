My_string = "rabbarrbarree"
New_string = ""
for letter in My_string:
    if letter not in New_string:
        New_string = New_string + letter
print(New_string)