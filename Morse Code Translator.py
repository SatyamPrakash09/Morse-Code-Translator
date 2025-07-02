#morse code dictionary
morse_code_dict = {
    # Letters
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',

    # Digits
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',

    # Punctuation
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.',

    # Space (optional - some use '/' for word separation)
    ' ': ' '
}

#creating reverse morse code dictionary to convert morse code into text
reversed_morse_dict = {v: k for k, v in morse_code_dict.items()}

#converts text into marse code
def text_to_morse(text):
    text = text.upper()
    morse_code=[]

    for i in text:
        if i in morse_code_dict:
            morse_code.append(morse_code_dict[i])
        else:
            morse_code.append(i) # if there is an unfamiliar char then it will just add exactly the same in morse_code[].

    return ' '.join(morse_code)

#convert user morse code into readable text
def morse_to_text(morse):
    # In morse code there is 1 space b/w letters and 3 spacing b/w words
    words = morse.strip().split("   ")# 3 spacing
    decoded_morse=[]
    for word in words:
        letters = word.split()
        decoded_word = ''
        for i in letters:
            if i in reversed_morse_dict:
                decoded_word += reversed_morse_dict[i]
            else:
                decoded_word += "?" #for unknown script
        decoded_morse.append(decoded_word)
    return " ".join(decoded_morse)
    

#get user choice if it want to convert morse to text or text to morse
while True:
    print('\n')
    choice = input("Choose options:\n1.Text to Morse code\n2.Morse code to Text\n3.Exit()\nEnter 1, 2 or 3: ")
    print("\n")
    if choice == "1":
        text_input = input("Enter the text you want to convert into morse code: ")
        result = text_to_morse(text_input)
        print("\nMorse code: \n",result)
        print("\n")

    elif choice == "2":
        morse_input = input("Enter the ,orse code you want to convert into text: ")
        result = morse_to_text(morse_input)
        print("\nText: \n",result)
        print("\n")
    elif choice == "3":
        print("Exiting..........")
        break
    else:
        print("Invalid option selected !!!\nPlease enter 1, 2 or 3")
    

