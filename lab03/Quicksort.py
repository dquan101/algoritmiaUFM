def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def quicksort(myList, start, end):
    if start < end:
        split = partition(myList, start, end)
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList



def main():
    myList = [5,10,15,32,55,21,40,2,3,76,89,28,9,7]
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)
main()