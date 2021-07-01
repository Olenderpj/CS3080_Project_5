""" PJ OLENDER
CS 3080 - Summer 2021
Project 5 - Decorators
Completed on 7/1/2021
Description: Use decorators to calculate the efficiency of different functions and test this by running the code
through 10,000 iterations. Tests different styles of functions based on the user's input/ selection.
"""


from functools import wraps
from Iterator import Iterator
from time import time

ITERATIONS_TO_COMPLETE = 10000


###############################################################################
# Timing Decorator
###############################################################################

# Decorator method used to calculate the efficiency of a function - tested by running the function 10,000 times
# Prints a formatted version of the results with the functions name and the time it took for 10k iterations
# Returns the elapsed time it took to run the function, and the function itself.
def timeIt(method):

    @wraps(method)
    def inner(*args, **kwargs):
        start = time()
        for i in range(ITERATIONS_TO_COMPLETE + 1):
            method(*args, **kwargs)

        end = time()
        elapsedTime = (end - start) * 1000

        print("{0:<20}{1}{2:>10.3f}{3:}".format(method.__name__, ": ", elapsedTime, " ms"))
        return elapsedTime * 1000

    return inner


###############################################################################
# Method Time Comparison
###############################################################################

# Accepts an array of functions and calls each function using the timeit decorator
# Stores the functions and their times in a dictionary and then sorts the dictionary based on the times
# Prints the fastest function's name
def timeCompare(methodsList, data):
    timeDict = {}
    for method in methodsList:
        time = method(data)
        timeDict[method.__name__] = time

    sortedDict = sorted(timeDict.items(), key=lambda x: x[1])

    fastestName, fastestTime = sortedDict[0]

    print("{} is the best".format(fastestName))


###############################################################################
# Test String Concatenation versus Join
###############################################################################
@timeIt
def stringConcatenator(words):
    phrase = ''
    for word in words:
        phrase += word + " "
    return phrase

@timeIt
def stringJoiner(words):
    return " ".join(words)


def testStringConcatenation():
    words = []
    for i in range(100, 200):
        words.append(str(i))
    timeCompare([stringConcatenator, stringJoiner], words)
    print()


###############################################################################
# Test String Formatting
###############################################################################
@timeIt
def stringPercent(phrase):
    longPhrase = "%s %s %s %s %s" % (phrase, phrase, phrase, phrase, phrase)

    return longPhrase

@timeIt
def stringF(phrase):
    return f"{phrase} {phrase} {phrase} {phrase} {phrase}"

@timeIt
def stringFormat(phrase):
    return "{} {} {} {} {}".format(phrase, phrase, phrase, phrase, phrase)


def testStringFormatting():
    phrase = " ".join([str(x) for x in range(10000)])

    timeCompare([stringPercent, stringF, stringFormat], phrase)
    print()


###############################################################################
# Test List Building
###############################################################################

# Generates a value that is incremented by 1 every time the function is called
def valueGenerator(maxValue):
    for i in range(maxValue):
        yield i + 1

@timeIt
def listRange(maxValue):
    rangeList = [*range(0, maxValue + 1)]
    return sum(rangeList)

@timeIt
def listComprehension(max):
    list = [value for value in range(max + 1)]
    return sum(list)

# Creates an iterator object that will iterate by 1 value until it reaches the maximum specified value
@timeIt
def listIterator(max):
    total = 0
    iterator = Iterator(max)
    for value in iterator:
        total += value
    return total

# Uses the generator function to get the sum of numbers to a maximum specified value
@timeIt
def listGenerator(max):
    total = 0
    numbers = valueGenerator(max)

    for value in numbers:
        total += value

    return value

@timeIt
def listExpression(max):
    total = sum(x + 1 for x in range(max))
    return total


def testListBuilding():
    max = 50
    timeCompare([listRange, listComprehension, listIterator, listGenerator, listExpression], max)
    print()


###############################################################################
# Menu processing
###############################################################################

def menu():
    menuItem = 1
    print("*" * 60)
    print("%d - Test String Concatenations" % menuItem)
    menuItem += 1
    print("%d - Test String Formatters" % menuItem)
    menuItem += 1
    print("%d - Test List Building" % menuItem)
    menuItem += 1
    print("%d - Quit" % menuItem)
    print("*" * 60)
    return promptForInteger(1, menuItem,
                            "Please make a selection between 1 and %d:" % menuItem,
                            "Your response must be number between 1 and %d, try again." % menuItem)


def promptForInteger(minimum, maximum, message, errorMessage):
    try:
        response = int(input(message + "\n"))
    except:
        response = -1

    while (response < minimum or response > maximum):
        try:
            response = int(input(errorMessage + "\n"))
        except:
            response = -1
    return response


###############################################################################
# Main
###############################################################################
response = 0
while response != 4:
    response = menu()

    # Test String Concatenations
    if response == 1:
        testStringConcatenation()
    # Test String Formatters
    elif response == 2:
        testStringFormatting()
    # Test List Building
    elif response == 3:
        testListBuilding()
    # Quit
    elif response == 4:
        print("Quitting!")