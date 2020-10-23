def isValid(value):
    
    # for checking the string character length
    if len(value) == 30:
        return True
    
    # for special character
    if True:
        count = 0
        # checking special characters
        arr = ["()", "(())", "(", ")", "(( ))", "=", "&&"]
        for i in value:
            if i in arr:
                count = count + 1
                break
        if count == 0:
            return False

    if True:
        count = 0
        # checking capital letters
        for i in range(65, 91):

            if chr(i) in value:
                count = count + 1

        if count == 0:
            return False

    if True:
        count = 0
        # checking small letters
        for i in range(90, 123):

            if chr(i) in value:
                count = count + 1

        if count == 0:
            return False

    # if all conditions fails
    return False


val = input("Enter your string character :")

if isValid([i for i in val]):
    print({i.split("=")[0]: (i.split("=")[1]) for i in val.split("&&")})

else:
    print("Syntax invalid")
