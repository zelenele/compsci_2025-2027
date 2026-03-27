with open("text.txt", "w") as f:
    f.write("abbaac\n")
    f.write("hello world")
TEXT_PATH = "text.txt"
#We need to read data form text file and store in a variable
with open (TEXT_PATH, "r") as f:
    file_text = f.read()
alphabet_dict = {
    "a":0,
    "b":0
}
letter = "c"
if letter in alphabet_dict.keys():
    if letter in alphabet_dict:
        alphabet_dict[letter] += 1
    else:
        alphabet_dict[letter] = 1
print(alphabet_dict)