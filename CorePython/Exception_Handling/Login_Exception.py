class LoginException(Exception):
    def __init__(self,message):       # making custom Exception class (khud ki exception class)
        super().__init__(message)

loginId = "Keshav"
password = "kes123"

try:
    if loginId == "Keshav" and password == "ke23":
        print("Valid User ")
    else:
        raise LoginException("Your information is not correct")

except LoginException as e:  # or LoginException ki jagah parent class (Exception) bhi likh skte hai 
    print("InCorrect --> ",e)