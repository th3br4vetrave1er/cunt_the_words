from collections import Counter
import re


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    # here we can specify how many most commons we wenna return
    return word_counts.most_common()


def main() -> None:
    user_prompt: str = input('Enter your name of the text file: ').strip()
    placeholder = open(user_prompt, 'r')
    text = placeholder.read()
    word_frequencies: list[tuple[str, int]] = get_frequency(text=text)

    for word, count in word_frequencies:
        print(
            f'Word "{word}" with the count of {count}'
        )


if __name__ == '__main__':
    main()

# TODO fixed main func, added file name input. Seems legit