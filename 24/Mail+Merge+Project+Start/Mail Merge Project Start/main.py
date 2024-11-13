#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as sample_letter:
    lines = sample_letter.readlines()

with open("./Input/Names/invited_names.txt") as guests_names:
    names = guests_names.readlines()


for name in names:
    dear_name = lines[0].replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt") as letter:
        letter.write()


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp