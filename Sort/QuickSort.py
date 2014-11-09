#!/usr/bin/python

class quickSort:
    def __sort(self,arr,low,high):
        if(high<=low) : return
        left = low
        right = high
        i = left + 1
        while i <= right :
            if arr[i] < arr[left] : 
                arr[i],arr[left] = arr[left],arr[i] 
                left+=1; i+=1
            elif arr[i] > arr[left] :
                arr[i],arr[right]=arr[right],arr[i]
                right-=1
            else : i+=1
        self.__sort(arr,low,left-1)
        self.__sort(arr,right+1,high)

    def sort(self,arr):
        if not isinstance(arr,list):
            raise "argument passed  is not of type list"
        length = len(arr);
        self.__sort(arr,0,length-1)
