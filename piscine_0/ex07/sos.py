from sys import argv


def main():
    """
    this program takes in a string and converts it to morse code
    """
    try:
        assert len(argv) == 2, "the arguments are bad"
        morse_code_dictionary = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            " ": "/",
        }
        morse_code = []
        for c in argv[1].upper():
            assert c in morse_code_dictionary.keys(), "the arguments are bad"
            morse_code.append(morse_code_dictionary[c])
        print(" ".join(morse_code))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
