"""
Caesar Cipher Encoder
---------------------
This script encodes a message using a Caesar cipher with a fixed shift of 15.
It retains punctuation, digits, and spaces, and preserves the case of letters.
"""

def shift_character(char: str, shift_amount: int) -> str:
    """
    Shifts a single alphabetic character by the specified amount.
    Wraps around the alphabet cyclically.
    Non-alphabetic characters are returned unchanged.
    """
    if char.isupper():
        base = ord('A')
        shifted = chr((ord(char) - base + shift_amount) % 26 + base)
        return shifted
    elif char.islower():
        base = ord('a')
        shifted = chr((ord(char) - base + shift_amount) % 26 + base)
        return shifted
    return char  # Leave punctuation, spaces, and digits untouched


def encode_message(message: str, shift_amount: int = 15) -> str:
    """
    Encodes the entire message using a Caesar cipher.
    """
    encoded = ""
    for char in message:
        encoded += shift_character(char, shift_amount)
    return encoded


def display_encoded_message(original: str, encoded: str) -> None:
    """
    Displays the original and encoded messages with clear labelling.
    """
    print("\n Caesar Cipher Encoder")
    print("--------------------------------------------------")
    print(f"Original Message : {original}")
    print(f"Encoded Message  : {encoded}")
    print("--------------------------------------------------\n")
    print("Note: Non-letter characters have been left unchanged.")


def main() -> None:
    """
    Prompts the user for input and displays the encoded result.
    """
    print("Welcome to the Caesar Cipher Encoder!")
    user_message = input("Please enter your message below:\n> ")
    encoded_result = encode_message(user_message)
    display_encoded_message(user_message, encoded_result)


if __name__ == "__main__":
    main()