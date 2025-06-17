from stats import get_num_words, get_num_characters


def main():
    path_to_book = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    get_num_words(path_to_book)
    print("--------- Character Count -------")
    character_count = get_num_characters(path_to_book)
    character_count_sorted = dict(sorted(character_count.items()))
    for key in character_count_sorted:
        print(f"{key}: {character_count_sorted[key]}")
    print("============= END ===============")


main()
