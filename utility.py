#!/usr/bin/python3 
import getopt, sys
import os
 
BASE_FILE_PATH = "C:\\Users\\HP\\Desktop\\"

def file_Operation(filename): 
  
    try: 
        file = open(os.path.join(BASE_FILE_PATH, filename), mode="r") 
    except FileExistsError: 
        print("File not found!!! Please provide the valid path of file") 
        sys.exit(1) 
    
    option = sys.argv[1]

    total_lines = 0 
    total_words = 0 
    total_charaters = 0 
    count = []
    count1 = [] 
    for line in file: 
        total_lines += 1 
        line = line.strip("\n") 
        words = line.split() 
        for i in words: 
            if i.isdigit(): 
                count.append(i) 
            if i.isalpha():
                word_list = list(i)
                for i in word_list:
                    count1.append(i.lower())
                #count1.append(list(i)) 

        total_words += len(words) 
        total_charaters += len(line) 

    if option == "-l":
        return f'The total lines are: {total_lines} {sys.argv[2]}' 
    elif option == "-w": 
        return f"The total worlds are: {total_words} {sys.argv[2]} " 
    elif option == "-c": 
        return f"The total charater are: {total_charaters} {sys.argv[2]} " 
    elif option == "-n": 
        numeric_number = set(count)
        return f"The total numeric number are: {numeric_number} {sys.argv[2]} " 
    elif option == "-a": 
        return f"The total alphabets are: {set(count1)} {sys.argv[2]} " 
    elif option == "-h": 
        s = """ Please provide the following Options with filename 
        Note: The options are case sensitive 
        -l: To display no. of lines present in a file 
        -c: To display no. of character present in a file 
        -w: To display no. of words in a file 
        -n: To display only numeric numbers in input file 
        -a: To display only alphabets in input file 
        -h: To disply help option""" 
        return s 
    else: 
        s = """Option is not valid!!,please provide the correct option 
want any help please provide the -h as options""" 
        return s 
 

if __name__ == "__main__":
    try: 
        a = file_Operation(sys.argv[2]) 
        print(a) 
    except: 
        print("please provide the correct argument") 
        print("python3 <script name> <Flag name> <Filename>") 
        print("python3 utility.py -l sample.txt")
