def main():

    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    
        lowered_words = file_contents.lower()
        words = lowered_words.split()
        counter = len(words)
    
        
    letter_dic = {}
    
    for letter in lowered_words:
        if letter.isalpha():
            if letter not in letter_dic:
                letter_dic[letter] = 1
        
            else:
                letter_dic[letter] += 1

    
    new_list = []
    def sort_on(dict):
        return dict[1]


    for letter, count in letter_dic.items():
        new_letter = (letter, count)
        new_list.append(new_letter)
       

    new_list.sort(reverse=True, key=sort_on)
    

    print(f"""--- Begin report of books/frankenstein.txt ---
    {counter} words found in the document""")
        
    for l, count in new_list:
   
        print(f"The {[l]} character was found {[count]} times")

if __name__ == "__main__":
    main()
    
