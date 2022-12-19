"""WAP to read a file and
m. Print the total number of characters, words and lines in the file.
n. Calculate the frequency of each character in the file. Use a variable of dictionary
type to maintain the count.
o. Print the words in reverse order.
p. Copy even lines of the file to a file named ‘File1’ and odd lines to another
file named ‘File2’."""
def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1
                    word = 'Y'
                for i in letter:
                    if(i !=" " and i !="\n"):
                        num_charc += 1
                        
print("Number of words in text file: ",
          num_words)               
            
print("Number of lines in text file: ",
          num_lines)
print('Number of characters in text file: ',
          num_charc)
print('Number of spaces in text file: ',
          num_spaces)
if _name_ == '_main_':
    fname = 'File1.txt'
    try:
        counter(fname)
    except:
        print('File not found')
