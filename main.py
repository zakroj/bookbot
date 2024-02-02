def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    give_report(num_words, get_num_characters(text))

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

def give_report(words, dict):
    print(f"{words} words found in the document")
    print("")
    new_list = []
    for item in dict:
        new_list.append(dict[item])
    
    new_list = sorted(new_list, reverse=True)
    
    for i in new_list:
        for item in dict:
            if dict[item] == i:
                print(f"The '{item}' character was found {i} times")

main()