from random import randint


class RoastedCornReal:
    def __init__(self):
        self.generateList = []

    def createList(self):
        for index in range(31, 41):
            self.generateList.append(index)
        print(self.generateList)

    def countElements(self):
        count = 0
        for element in self.generateList:
            count += 1
        return count

    def sumOfEvenPosition(self):
        count = 0
        for index in self.generateList:
            if index % 2 == 0:
                count += index
        return count

    def sumOfOddPosition(self):
        count = 0
        for sumOdd in self.generateList:
            if sumOdd % 2 != 0:
                count += sumOdd
        return count

    def multiply3rdPositionElements(self):
        counter = 1
        for element in self.generateList[0:10:3]:
            counter *= element
        print(counter)
        return counter

    def calculateAverage(self):
        average = 0
        for element in self.generateList:
            average += element / 100
        print(average)
        return average

    def largestElement(self):
        largest = 0
        for element in self.generateList:
            if element > largest:
                largest = element
        print(largest)
        return largest

    def smallestElement(self):
        smallest = self.generateList[0]
        for element in self.generateList:
            if element < smallest:
                smallest = element
        print(smallest)
        return smallest

    def createStringList(self, characters):
        stringList = []
        for element in characters:
            if len(element) >= 2:
                if element[0] == element[-1]:
                    stringList.append(element)
        print(stringList)
        return stringList

    def sequentialList(self, sequenceOfIntegers):
        listOfIntegers = []
        for element in range(1, 16):
            listOfIntegers.append(element)
            print(listOfIntegers)
            return sequenceOfIntegers



