import math

primeNumbers = []

def checkPrime(number):
    for num in range(2, int(math.sqrt(number)+1)):
        if number % num == 0:
            return False
    return True

def generatePrimeNumbers(boundary):
    for num in range(2, boundary):
        if checkPrime(num):
            primeNumbers.append(num)

def countGoldbachCombinations(boundary):
    # answer[(num-4)/2] := GoldbachCount
    answer = []
    for num in range(4, boundary, 2):
        # Count for current even number
        count = 0
        # The primeNumbers[minorPrimeIdx] is prime number of the pair
        minorPrimeIdx = 0
        while primeNumbers[minorPrimeIdx] <= num/2:
            if (num - primeNumbers[minorPrimeIdx]) in primeNumbers:
                count += 1
            minorPrimeIdx += 1
        answer.append(count)
    return answer

boundary = 1000
generatePrimeNumbers(boundary)
answer = countGoldbachCombinations(boundary)
print(answer)