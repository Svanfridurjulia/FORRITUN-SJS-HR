def find_longest(line_str):
    len_count = 0
    for word in line_str:
        len_word = len(word)
        if len_word > len_count:
            len_count = len_word
            longestword = word
    return longestword.strip()

def open_file(filename):
    try:
        opened_file = open(filename,"r")
        return opened_file
    except FileNotFoundError:
        return False


filename = input("Enter filename: ")
file_object = open_file(filename)
if file_object:
  longest_word = find_longest(file_object)
  print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
  file_object.close()
else:
  print("File not found")