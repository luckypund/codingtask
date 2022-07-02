#!/usr/bin/python3 
import sys 
 
def file_Operation(option,filename): 
 
        try: 
            file = open(filename, mode="r") 
        except: 
            print("File not found!!! Please provide the full path of file") 
            sys.exit(1) 
 
        total_lines = 0 
        total_words = 0 
        total_charaters = 0 
        count = 0 
        count1 = 0 
        for line in file: 
            total_lines += 1 
            line = line.strip("\n") 
            words = line.split() 
            for i in words: 
                if i.isdigit(): 
                    count += 1 
                if i.isalpha(): 
                    count1 += 1 
 
            total_words += len(words) 
            total_charaters += len(line) 
 
        if option.lower() == "-l": 
            return f'The total lines are: {total_lines} {sys.argv[2]}' 
        elif option == "-w": 
            return f"The total worlds are: {total_words} {sys.argv[2]} " 
        elif option == "-c": 
            return f"The total charater are: {total_charaters} {sys.argv[2]} " 
        elif option == "-n": 
            numeric_number = count 
            return f"The total numeric number are: {numeric_number} {sys.argv[2]} " 
        elif option == "-a": 
            return f"The total alphabets are: {count1} {sys.argv[2]} " 
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
 
try: 
        a = file_Operation(sys.argv[1],sys.argv[2]) 
        print(a) 
except: 
        print("please provide the correct argument") 
        print("python3 <script name> <Flag name> <Filename>") 
        print("python3 utility.py -l sample.txt")