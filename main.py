with open('./books/frankenstein.txt') as f:
    file_contents = f.read()

def count_words_in_book(string):
    return len(string.split())

def count_letters_in_book(string):
    dict_count = {}
    for char in ''.join(string.split()):
        if char.lower() in dict_count and char.isalpha():
            dict_count[char.lower()] += 1
        elif char.isalpha():
            dict_count[char.lower()] = 1
    return dict_count

def sort_list_from_dict(unsorted_dict):
    list_to_be_sorted = list(unsorted_dict.values())
    list_to_be_sorted.sort(reverse=True)
    return list_to_be_sorted

def print_letters_in_order_from_most_used(letters_dict):
    sorted_list_of_values = sort_list_from_dict(letters_dict)
    for count in sorted_list_of_values:
        print(f"The '{list(letters_dict.keys())[list(letters_dict.values()).index(count)]}' character was found {count} times")
    return
    
def print_book_report(string):
    print('--- Begin report of books.frankenstein.txt ---')
    print(f'{count_words_in_book(string)} words found in document\n')
    print_letters_in_order_from_most_used(count_letters_in_book(string))
    print('--- End report ---')
        

print_book_report(file_contents)