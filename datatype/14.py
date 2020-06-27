# 14. Write a Python function to create the HTML string with tags around the
# word(s).

def AddHtmlTags(tag,strn):
    
    return f"<{tag}> {strn} </{tag}>"




print(AddHtmlTags(input("enter a tag"),input("Enter a string")))
