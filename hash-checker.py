hashValue = input("Enter the hash value to check: ")
hashToCheck = input("Enter the hash value to compare against: ")
def hash_checker(hashValue, hashToCheck):
    if hashValue == hashToCheck:
        print("The hash values match.")
    else:
        print("The hash values do not match.")
hash_checker(hashValue, hashToCheck)