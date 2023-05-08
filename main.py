from langdetect import detect
text = input("Enter any text in any language : ")
print("Language Detected : ",detect(text))