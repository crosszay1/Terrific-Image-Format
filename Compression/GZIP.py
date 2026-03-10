import gzip
import os

choice = input("Choose C to compress and D to decompress: ").lower()
inputData = input("Input: ")
os.system("clear")
print("reached")
if choice == "c":
    bytes = inputData.encode('utf-8')
    outputData = gzip.compress(bytes)
elif choice == "d":
    outputData = gzip.decompress(eval(inputData)).decode('utf-8')
else:
    outputData = "Choice var error, please choose C or D."

print(outputData)



# import gzip
# def gzipEncode(input):
#     bytes = input.encode('utf-8')
#     return gzip.compress(bytes)
# def gzipDecode(input):
#     return gzip.decompress(eval(input)).decode('utf-8')

# print(gzipEncode("Hello World!"))