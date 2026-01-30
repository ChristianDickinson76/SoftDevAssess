userNames = ["drSmith", "drHouse"]
userEmails = ["drSmith@gmail.com", "drHouse@hospital.com"]
userRoles = ["admin", "docter"]
userDept = ["management", "research"]

_userAttempts = 0
while (_userAttempts < 3):
    _userName = input("Please enter your username:\n")
    _userPassword = input("Please enter your password:\n")
    if (_userName in userNames and _userPassword == "123"):
        print("Login Correct, Access Granted")

        _patientName = input("Please enter the patients full name:\n")
        _patientDOB = input("Please enter the patients DOB (YYYY/MM/DD):\n")
        _patientAOB = input("Please enter the patients Address of Birth:\n")
        _patientCOB = input("Please enter the patients Country of Birth:\n")
        _patientAddress = input("Please enter the patients Current Address:\n")

        _patientDetails = [_patientName, _patientDOB, _patientAOB, _patientCOB, _patientAddress,]

        for _element in _patientDetails:
            _cypherElement = ""
            for _x in range(0, len(_element)):
                _cypherElement.join(chr(ord(_element[_x]) + 3))
            _element = _cypherElement

        print("Cyphered Details are:")
        for _element in _patientDetails:
            print(f"{_element}")

        if(userRoles[userNames.index(_userName)] == "admin"):
            for _element in _patientDetails:
                _cypherElement = ""
                for _x in range(0, len(_element)):
                    _cypherElement.join(chr(ord(_element[_x]) + 3))
                _element = _cypherElement
        
    else:
        print("Login Incorrect, Access Denied")
        _userAttempts+=1
print("Too many attempts, exiting.")