#write a python program to detect whwther a comment is spam or not a comment should be trated a spam if it contains any of these keywords 
comment =input("enter comment")
comment=comment.lower()
if "make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
    print("the message is spam")
else:
    print("message is corrrect")