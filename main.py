#text = get_book_text(book_path)
#def get_book_text(path):
#    with open(path) as f:
#        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text_content = open_text(book_path)
    word_count = word_count_func(text_content)
    #print(f"| {word_count} words counted.")
    char_count = char_count_func(text_content)
    #print(char_count)
    fancy_print(book_path, word_count, char_count)

def word_count_func(text_data):
    return len(text_data.split())
    
def open_text(path):
    with open(path) as f:
        return f.read()
        #print(file_contents)

def char_count_func(text_data):
    text_data = text_data.lower()
    dict = {}
    for i in text_data:
        if i.isalpha() == True:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
    return dict

def fancy_print(bookpath, wordcount, dictx):
    print(f"============================")
    print(f"-- result info of {bookpath} --")
    print()
    print(f"| {wordcount} words counted.")
    print()

    #preping for sort by adding names to dict
    listdict = []
    for i in dictx:
        tempdict = {"char": i, "num": dictx[i]}
        listdict.append(tempdict)
    #actual sort
    listdict.sort(reverse=True, key=lambda idk : idk["num"])
    #result is something like []'u': 10407, 'n': 24367]
    #now how to print it pretty?
    #ex: The 'z' character was found 243 times
    for i in listdict:
        a = i["char"]
        b = i["num"]
        print(f"the char {a} was found {b} times")
    print ("---------end-------------")

    


main()