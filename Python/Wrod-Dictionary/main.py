import json
from tkinter import *
import tkinter.messagebox
from difflib import get_close_matches

# Search for word
def Search(word, data):
    # Check word is in Dictionary or Not! 
    # if word is not in Dictionary definition variable will be Falsee
    definition = data.get(word.lower(),False)

    # if word is not in Dictionary
    if not definition:

        # Check for alpha Capital Letters (eg. Paris, Delhi)
        definition = data.get(word.title(),False)
        if definition:
           print_result(definition)
           return

        # Check for acronyms (eg. USA, UK)
        definition = data.get(word.upper(),False)
        if definition:
            print_result(definition)
            return

        # Find Close match of given word with cutoff of 0.8
        suggestion = get_close_matches(word, data.keys(), 1, cutoff=0.8)

        # If Close Match Found!
        if len(suggestion) > 0:
            tkinter.messagebox.showinfo(f'{word}',f"Did you Mean {suggestion[0]} ?")
            print_result(data[suggestion[0]])
            return

        # If Close Match Not Found! or User Don't want Our suggestion! 
        tkinter.messagebox.showinfo(f'{word}',f"This word {word} is not in Dictionary!")
        return
    
    # if exact word is in Dictionary
    print_result(definition)

# Get Input From User
def get_word():
    word = StringVar()
    text_entry = Entry(window, textvariable=word)
    text_entry.grid(row=0, column=0)
    return word

# Final Output In Clean way
def print_result(definitions):
    
    text_ouput.delete('1.0', END)
    
    if(type(definitions) == str):
        text_ouput.insert(END,definitions)
    else:
        print()
        for index ,definition in enumerate(definitions):
            text_ouput.insert(END,f"{index+1}: {definition}\n")

# Main Method
if __name__ == "__main__":
    
    # Data Load Fron Data.json File using json module
    data = json.load(open("data.json"))
    
    # Initialise tkinter window
    window = Tk()
    
    # Get Input From User and save it into word
    word = get_word()
    
    # Button Trigger Search Function that Find Word's defination from it
    find = Button(window, text="Find",width=20, command=lambda: Search(word.get(),data))
    find.grid(row=0, column=1)
    
    # Show Output in Text search thorugh Data.jsaon by using Search Functtion
    text_ouput =Text(window,height=10)
    text_ouput.grid(row=1, column=0, columnspan=2)
    
    

    # Keep Repeating Update tkinter window
    window.mainloop()
