def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(get_num_characters(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_dict = {}
    full_text = text.lower()
    for c in "abcdefghijklmnopqrstuvyxyz":
        count = full_text.count(c)
        char_dict[c] = count
    return char_dict

main()