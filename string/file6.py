# with open("sample.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using python.\nI like programming in pyhton")

## changing python with linux

# with open("sample.txt","r") as f:
#     data = f.read()
# new_data = data.replace("python","linux")
# print(new_data)

# with open("sample.txt","w") as f:
#     f.write(new_data)

 ## Find the word: and check by line
def check_word():
    word = "learning"
    with open("sample.txt","r") as f:
        data = f.read()
        if(data.find(word) != 1):
        # if (word in data):
            print("found")
        else :
            print("not Found")


def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("sample.txt","r") as f:
        while data:
           data = f.readline()
           if (word in data):
               print(line_no)
               return
           line_no += 1
           
check_line()
        
  