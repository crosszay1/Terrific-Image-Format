import gzip
import os

choice = input("Choose C to compress and D to decompress: ").lower()
inputData = input("Input: ")
os.system("clear")

if choice == "c":
    bytes = inputData.encode('utf-8')
    outputData = gzip.compress(bytes)
elif choice == "d":
    outputData = gzip.decompress(eval(inputData)).decode('utf-8')
else:
    outputData = "Choice var error, please choose C or D."

print(outputData)