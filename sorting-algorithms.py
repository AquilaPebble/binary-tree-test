def selectionSort(data:list) -> list:
    for i in range(0,len(data)):
        minIndex = i
        for o in range(i + 1,len(data)):
            if data[o] < data[minIndex]:
                minIndex = o
        if minIndex != i:
            data[i],data[minIndex] = data[minIndex],data[i]
    return data
def insertionSort(data:list) -> list:
    for i in range(1,len(data)):
        currentElement = data[i]
        minIndex = i
        while minIndex > 0 and currentElement < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1
        data[minIndex] = currentElement
    return data