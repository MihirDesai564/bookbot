
def count_chars(string):
    count = {}
    for i in string:
        l = i.lower()
        if l in count:
            count[l] += 1
        else:
            count[l] = 1
    return count

def file_count(string):
    count = len(string.split())
    return count

def main():
    with open("books\\frankenstein.txt") as f:
        file_contents = f.read()
        total_len = file_count(file_contents)
        char_len_dict = count_chars(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{total_len} words found in the document")
        print("\n")
        for char, length in char_len_dict.items():
            print(f"The '{char}' character was found {length} times")
        print("--- End report ---")


        

main()