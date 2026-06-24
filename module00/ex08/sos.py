MORSE_ALPHABET = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/',
}


def morse_encode(text: str) -> str:
    """Encodes a given text into Morse code."""
    encoded = []
    for char in text.upper():
        if char in MORSE_ALPHABET:
            encoded.append(MORSE_ALPHABET[char])
        else:
            raise ValueError(
                f"Character '{char}' cannot be encoded in Morse code."
            )
    return ' '.join(encoded)


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sos.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    try:
        morse_code = morse_encode(text)
        print(morse_code)
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
