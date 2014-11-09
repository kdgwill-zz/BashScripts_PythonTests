#!/usr/bin/python

class mergeSort:
    def __sort(self,arr,t,low,high):
        if(low<high):
            mid = low + (high-low)/2
            self.__sort(arr,t,low,mid)
            self.__sort(arr,t,mid+1,high)
            #
            for i in range(low,high+1): t[i] = arr[i]
            left = low
            right = mid+1
            for i in range(low,high+1):
                if left > mid : arr[i] = t[right];right+=1 #if left side past limit empty right
                elif right > high : arr[i] = t[left];left+=1 #if right side past limit empty right
                elif t[left] <= t[right] : arr[i] = t[left];left+=1 
                else : arr[i] = t[right];right+=1 
    
    def sort(self,arr):
        if not isinstance(arr,list):
            raise "argument passed  is not of type list"
        length = len(arr);
        t = [0]*length
        self.__sort(arr,t,0,length-1)



