def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)

    print(f"The book contains {word_count} words")

    for key in character_count:
        print(f"The {key} character was found: {character_count[key]} times")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_character_count(text):
    character_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_count:
            character_count[lowered] += 1
        else:
            character_count[lowered] = 1
    return character_count

main()