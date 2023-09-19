# question-01
# answer:
#     (a) text, x, y, color
#     (b) line 11
#     (c) "Tuesday", 0, 200, blue
#     (d) 2 (lines 8 and 9)
#     (e) Answers vary. Sample: the function body is intended because it's locally scoped to the function definition.
#     (f) The program draws a box starting at (0,200), filled blue, with "Tuesday" inside the box.


# question-02
# answer:
#     (a) Answers vary. Sample: Event handlers capture, log, and execute functions when an event occurs. They usually listen continually while a program is running.
#     (b) Answers vary. Please ensure that students correctly define two different Python variables. Sample:
number = 2
message = "Testing...1...2...3...testing"
#     (c) Again, answers vary. Ensure that students correctly reassign their first variable to a new value. Sample:
number = 1400
#     (d) Once again, answers vary. Ensure that students correctly reassign their second variable to a new value. Sample:
message = "Test complete."

# question-03
def printSquareAndCube(n):
    print("Square: ", n * n)
    print("Cube: ", n ** 3)
# answer: Responses will vary. Students must write a single function that calls printSquareAndCube three times, testing a different value each time. Sample:
def testFunction():
    printSquareAndCube(3)
    printSquareAndCube(2.4)
    printSquareAndCube(-5)

# question-04
firstNumber, secondNumber = 12, 7
# answer:
#     (a) True and False
#     (b) True
#     (c) False
#     (d) In any order:
firstNumber + secondNumber
firstNumber - secondNumber
firstNumber * secondNumber
firstNumber / secondNumber

# question-05
username = input("Please enter your username: ")
# answer:
#     (a)
if username == "GraysonGryphons":
    print("Yay, you're allowed to log in!")
else:
    print("Access denied.")
#     (b)
if username == "GraysonGryphons":
    print("Yay, you're allowed to log in!")
if username != "GraysonGryphons":
    print("Access denied")

# question-06
# answer:
#     (a) "large"
#     (b) "tall and narrow"

# question-07
extremeLow = 2.7
extremeHigh = 101.3
currentTemp = float(input("What is the current temperate? "))
# answer:
if currentTemp > 2.7 and currentTemp < 101.3:
    print("Current temperature is within the extremes")


# question-08
# answer:
#     (a) "You're in Upper School."
#         "You can get your license if you want!"
#     (b) "You're in Middle School."
#         "You're probably not telling the truth."


# question-09
# answer:
for i in range(1,16):
    print(2 * i)


# question-10
# answer:
from random import randrange
random1 = randrange(1,100)
random2 = randrange(1,100)

print(random1 // random2)
print(random1 % random2)



