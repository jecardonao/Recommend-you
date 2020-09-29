def QuickSort(arr):.

 elements = len(arr)  

  if elements < 2: 

      return arr 

current_position = 0  


 for i in range(1, elements):  

     if arr[i] <= arr[0]: 

      current_position += 1 

       temp = arr[i] 

       arr[i] = arr[current_position] 

       arr[current_position] = temp 

 
 temp = arr[0] 

arr[0] = arr[current_position]  

arr[current_position] = temp  

left = QuickSort(arr[0:current_position])  

right = QuickSort(arr[current_position+1:elements])  

 

arr = left + [arr[current_position]] + right  

return arr 

 
 

A = [91,58,19,59,4,50,14,22,11,27,16,24,60,7,58,83,26,55,34,50,21,41,78,57,8,34,11,58,29,84,98,48,6,93,14,59,89,60,14,33,52,74,1,30,8,50,37,57,30,80,81,94,89,100,88,67,3,18,57,15,73,38,59,60,73,92,30,39,43,88,42,58,15,49,88,11,71,50,77,89,74,70,4,12,27,53,18,75,38,6,82,76,54,74,2,15,65,9,24] 

print("Lista A: ",A) 

print("Lista A ordenada: ",QuickSort(A)) 

B = [7,55,58,38,44,4,62,63,110,156,134,160,94,1,4,12,186,57,181,175,177,153,146,46,156,19,196,200,57,27,75,94,161,49,69,71,42,168,49,173,197,48,162,25,199,63,28,99,194,6,161,173,130,144,76,25,91,15,146,52] 

print("Lista B: ",B) 

print("Lista B ordenada: ",QuickSort(B)) 

print("Listas: A+B: ", A + B) 

print("Listas A + B ordenadas por el metodo quicksort: ",QuickSort(A)+QuickSort(B))