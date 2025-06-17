def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        print("----------- Word Count ----------")
        print(f"{num_words} words found in the document")
        return num_words


def get_num_characters(path_to_file):
    from collections import defaultdict
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        characters = {}
        for char in file_contents:
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1
        return characters


