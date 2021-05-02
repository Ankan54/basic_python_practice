"""
Binary search algorithm implementation
@Author: Ankan Bera
"""

def binary_search(search_list, target,low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high=len(search_list)-1

    if high < low:
        return -1

    mid_point= (low+high) // 2

    if search_list[mid_point]== target: # consider the list to be sorted
        return mid_point
    elif search_list[mid_point]> target:
        return binary_search(search_list,target,low,mid_point-1)
    else:
        return binary_search(search_list,target,mid_point+1,high)


if __name__ == "__main__":
    search_list= [1,5,6,8,10,15,17,19,22,23,26,33,37,41,50]
    print(binary_search(search_list,17))
