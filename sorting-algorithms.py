from random import randint
import threading
import time
def generateList(length:int,minMaxElementSize:tuple) -> list:
    return [randint(minMaxElementSize[0],minMaxElementSize[1]) for i in range(length)]
class Sort:
    @staticmethod
    def selectionSort(data:list) -> list:
        for i in range(0,len(data)):
            minIndex = i
            for o in range(i + 1,len(data)):
                if data[o] < data[minIndex]:
                    minIndex = o
            if minIndex != i:
                data[i],data[minIndex] = data[minIndex],data[i]
        return data
    @staticmethod
    def insertionSort(data:list) -> list:
        for i in range(1,len(data)):
            currentElement = data[i]
            minIndex = i
            while minIndex > 0 and currentElement < data[minIndex - 1]:
                data[minIndex] = data[minIndex - 1]
                minIndex -= 1
            data[minIndex] = currentElement
        return data
    @staticmethod
    def mergeSort(data:list) -> list:
        def merge(left:list,right:list) -> list:
            if not len(left):
                return left
            if not len(right):
                return right
            result = []
            leftIndex = 0
            rightIndex = 0
            while len(result) < (len(right) + len(left)):
                if left[leftIndex] < right[rightIndex]:
                    result.append(left[leftIndex])
                    leftIndex += 1
                else:
                    result.append(right[rightIndex])
                    rightIndex += 1
                if leftIndex == len(left) or rightIndex == len(right):
                    result.extend(left[leftIndex:] or right[rightIndex:]) # what does this do lmao
                    break
        if len(data) <= 1:
            return data
        return merge(Sort.mergeSort(list[:len(data)//2]),Sort.mergeSort(list[len(data)//2:]))
testerList = generateList(30,(0,100))