<<<<<<< HEAD
=======
#change made in subranch sub
>>>>>>> costupdate
import tiktoken
file_name=input("enter a file name: ")
try:
    with open(file_name,"r") as file:
        content=file.read()
        print("content is :",content)
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens =  encoding.encode(content)
    count = (len(tokens))
    print("Token count is :",count)
    cost = (count/1000) *0.003
    print("estimated cost is : $ ",round(cost,6))
except FileNotFoundError:
    print("\nerror:file not found")
