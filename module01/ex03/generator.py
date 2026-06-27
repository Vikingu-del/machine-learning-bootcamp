import random
from typing import Optional


def ft_shuffle(series: list) -> list:
    for i in range(len(series) - 1, 0, -1):
        j = random.randint(0, i)
        series[i], series[j] = series[j], series[i]


def generator(text: str, sep: str = " ", option: Optional[str] = None):
    """Splits the text according to sep value and yields the substrings."""
    VALID_OPTIONS = ["shuffle", "unique", "ordered", None]

    if (
            isinstance(text, str)
            and isinstance(sep, str)
            and option in VALID_OPTIONS
        ):
        words = text.split(sep)

        if option == "shuffle":
            ft_shuffle(words)
        elif option == "ordered":
            words = sorted(words)
        elif option == "unique":
            words = list(dict.fromkeys(words))

        for word in words:
            yield word
        return

    yield "ERROR"


if __name__ == "__main__":
    dash = "-"
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print(dash * 40)

    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print(dash * 40)

    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print(dash * 40)

    not_unique_text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(not_unique_text, sep=" ", option="unique"):
        print(word)
    print(dash * 40)

    for word in generator([1, 2, 3 ,4], sep=" ", option="unique"):
        print(word)
