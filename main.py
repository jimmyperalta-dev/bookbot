import sys
from stats import count_words, count_characters, sort_char_count, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
       
    with open(path) as f:
        contents = f.read()
    
   
    word_count = count_words(contents)
    
   
    char_counts = count_characters(contents)
    
 
    sorted_chars = sort_char_count(char_counts)
    
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    
if __name__ == "__main__":
    main()