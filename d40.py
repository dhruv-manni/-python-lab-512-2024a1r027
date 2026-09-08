# 3.Take an email address and print username,domain,and reversed domain.
email=input("Enter Email:")
username=email.split("@")[0]
domain=email.split("@")[-1]
reversed_domain=email[::-1]
print("Username=",username)
print("Domain=",domain)
print("Reversed Domain:",reversed_domain)