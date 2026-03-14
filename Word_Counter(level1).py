def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"Total number of words: {word_count}")
    except FileNotFoundError:
        print("file doesn't exist")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
file_name = input("Enter the file name: ")
count_words_in_file(file_name)