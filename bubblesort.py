def bubble_sort(list1):  
    has_swapped = True  
  
    total_iteration = 0  
  
    while(has_swapped):  
        has_swapped = False  
        for i in range(len(list1) - total_iteration - 1):  
            if list1[i] > list1[i+1]:  
                # Swap  
                list1[i], list1[i+1] = list1[i+1], list1[i]  
                has_swapped = True  
        total_iteration += 1  
    print("The number of iteraton: ",total_iteration)  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)    
print("The sorted list is: ", bubble_sort(list1))  
