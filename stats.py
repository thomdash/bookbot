def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(text):
    words = len(text.split())
    return words

def each_character(text):
    letter_dict = {}
    for letter in text:
        lower_case = letter.lower()
        if lower_case in letter_dict:
            letter_dict[lower_case] += 1
        else: 
            letter_dict[lower_case] = 1
    return letter_dict

def sorted_list(char_dict):
    dict_list = []
    for key, count in char_dict.items():
        char_info = {"char": key, "count": count}
        dict_list.append(char_info)
    def sort_on(dict):
        return dict["count"]
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list