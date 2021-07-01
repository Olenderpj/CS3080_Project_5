from functools import wraps
from Iterator import Iterator
from time import time


###############################################################################
# Timing Decorator
###############################################################################
def timeIt(method):
    @wraps(method)
    def inner(*args, **kwargs):
        start = time()
        method(*args, **kwargs)
        end = time()
        elapsedTime = (end - start) * 1000

        print("{0:<20}{1}{2:>10.3f}{3:}".format(method.__name__, ":", elapsedTime, " ms"))
        return elapsedTime * 1000

    return inner


###############################################################################
# Method Time Comparison
###############################################################################
def timeCompare(methodsList, data):
    timeDict = {}
    for method in methodsList:
        time = method(data)
        timeDict[method.__name__] = time

    sortedDict = sorted(timeDict.items(), key=lambda x: x[1])

    #print(sortedDict)
    fastestName, fastestTime = sortedDict[0]

    print("{} is the fastest".format(fastestName))





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

    # TODO: COMPLETE- Run timeCompare on the two string methods
    timeCompare([stringConcatenator, stringJoiner], words)
    print()


###############################################################################
# Test String Formatting
###############################################################################
@timeIt
def stringConv(phrase):
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

    # TODO: COMPLETE- Run timeCompare on the three formatting methods

    timeCompare([stringConv, stringF, stringFormat], phrase)

    print()


###############################################################################
# Test List Building
###############################################################################
def valueGenerator(maxValue):
    for i in range(maxValue):
        yield i + 1

@timeIt
def listRange(maxValue):
    rangeList = [*range(0, maxValue + 1)]
    return sum(rangeList)

@timeIt
def listComprehension(max):
    #TODO: double check if this is correct
    list = [value for value in range(max + 1)]
    return sum(list)

@timeIt
def listIterator(max):
    total = 0
    iterator = Iterator(max)
    for value in iterator:
        total += value
    return total

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

    # TODO: Run timeCompare on the five list building methods
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
