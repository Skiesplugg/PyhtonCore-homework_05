def generator_numbers(text: str):
    words = text.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            continue

        try:
            yield float(word)
        except ValueError:
            pass


def sum_profit(text: str, func: callable):
    total = 0

    for number in func(text):
        total += number

    return total

            
