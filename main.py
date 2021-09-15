# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def my_function():
    #get user's name
    name = input("Tell me your name:")
    #print user's name
    print(f'Hello{name}')

def second_function():
    #ask the user for a number
    number = int(input("input a number:"))
    #multiply number by itself
    your_Number = number * number
    #print number
    print (your_Number)

def third_function():
    #ask user for a word
    word = input("input a word:")
    #count how many letters in the word
    letters = len(word)
    #print letters in word
    print(letters)


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    my_function()
    second_function()
    third_function()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

