#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    text = str(letter.readlines())
    print(text)
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
with open("./Input/Names/invited_names.txt", mode="r") as names:
    for name in names:
       stripped_name = name.strip()
       new = text.replace("[name]",stripped_name)
       with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letters:
           completed_letters.write(new)
# Save the letters in the folder "ReadyToSend".
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp