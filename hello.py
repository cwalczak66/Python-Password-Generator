import random

def generatePassword(len):
    password = ""
    for i in range(len):
        ascii_val = random.randint(32, 126)
        character = chr(ascii_val)
        password+=character
    return password 

def main():
    len = 16

    newPassword = generatePassword(len)
    print(f"Generated Pasword: {newPassword}")

    
if __name__ == "__main__":
    # Call the main function when the script is executed
    main()



