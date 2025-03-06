def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def sort_char_count(char_count_dict):
    chars_list = []
    for char, count in char_count_dict.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list