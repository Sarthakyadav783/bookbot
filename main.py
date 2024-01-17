def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    text.lower()
    num_words=count_words(text)
    chars_dict=count_letters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    report=get_report(chars_dict)
    for item in report:
        print(item)
    print("--- End report ---")
    
    #print(chars_dict)

def get_book_text(path):
    file_object=open(path,"r")
    data=file_object.read()# return a string
    return data

def count_words(text):
    words=text.split()
    return len(words)

def count_letters(text):
    text.lower()
    char_dict={}
    count=0
    for i in text:
        if i in char_dict:
            char_dict[i]+=1
        else:
            char_dict[i]=1
    return char_dict

def get_report(dict1):
    list1=[]
    for i in dict1:
        if i.isalpha():
            list1.append(f"The {i} character was found {dict1[i]} times")
    list1.sort()
    return list1
    
    


main()
