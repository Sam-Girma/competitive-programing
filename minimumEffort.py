class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        energy = tasks[0][1]
        result = tasks[0][1]
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                sub_array1 = arr[:mid]
                sub_array2 = arr[mid:]

                mergeSort(sub_array1)
                mergeSort(sub_array2)
                i = j = k = 0
                while i < len(sub_array1) and j < len(sub_array2):
                    if sub_array1[i][1] - sub_array1[i][0] > sub_array2[j][1] - sub_array2[j][0]:
                        arr[k] = sub_array1[i]
                        i += 1
                    else:
                        arr[k] = sub_array2[j]
                        j += 1
                    k += 1
                while i < len(sub_array1):
                    arr[k] = sub_array1[i]
                    i += 1
                    k += 1
 
                while j < len(sub_array2):
                    arr[k] = sub_array2[j]
                    j += 1
                    k += 1

        mergeSort(tasks)

        for element in tasks:
            if element[1] > energy:
                result = result + element[1] - energy
                energy = energy + element[1] - energy
            energy = energy - element[0]
        return result
