introString=input("enter your introduction: ")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
        characterCount=characterCount-1
        wordCount=wordCount+1
print("number Words in the string: ")
print(wordCount)

print("number Characters in the string: ")
print(characterCount)