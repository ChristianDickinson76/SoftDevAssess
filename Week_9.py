def greetUser():
    print("Welcome to the Python treasure hunt!")

greetUser()

def calculateSum(a, b):
    return a + b

sumResult = calculateSum(15, 25)
print(f"Sum of 15 and 25 is: {sumResult}")

def createUserProfile(userName, userAge=18, userCountry="UK"):
    return {
        "name": userName,
        "age": userAge,
        "country": userCountry
    }

profile = createUserProfile("Christian")
print("User Profile Created:", profile)

def calculateTotalSum(*numbers):
    return sum(numbers)

total = calculateTotalSum(1, 2, 3, 4, 5)
print("Total Sum of numbers:", total)

square = lambda x: x * x
print("Square of 4 is:", square(4))

def calculateFactorial(n):
    if n == 1:
        return 1
    return n * calculateFactorial(n - 1)

factorialResult = calculateFactorial(5)
print("Factorial of 5 is:", factorialResult)

def numberSequenceGenerator(limit):
    for i in range(limit):
        yield i

print("Generated Sequence up to 5:")
for num in numberSequenceGenerator(5):
    print(num)

greetUser()

finalProfile = createUserProfile("Christian", 18, "UK")

ageFactorial = calculateFactorial(finalProfile["age"])

numbersList = [1, 2, 3, 4, 5]
listSum = calculateTotalSum(*numbersList)

print("User Profile:", finalProfile)
print(f"Factorial of user age ({finalProfile['age']}): {ageFactorial}")
print(f"Sum of {numbersList}: {listSum}")