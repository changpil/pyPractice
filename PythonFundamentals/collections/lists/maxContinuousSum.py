def find_max_sum_subarray(l):
    c_max,p_max, maxmax = l[0], l[0], l[0]
    once_minus = False
    for i in range(1,len(l)):
        if l[i] < 0:
            if p_max + l[i] < 0:
                once_minus = False
                maxmax = max(c_max, p_max)
                c_max, p_max = 0, 0
            else:
                p_max += l[i]
                once_minus = True
        else:
            if not once_minus:
                c_max += l[i]
            p_max += l[i]

    return max(c_max, p_max, maxmax)


print(find_max_sum_subarray([1,2,3,4]))
print(find_max_sum_subarray([1,2,-1,3,4]))
print(find_max_sum_subarray([1,2,-1,-5, 3,4]))
lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1];
print("Sum of largest subarray: ", find_max_sum_subarray(lst));

s = """
This algorithm takes a dynamic programming approach to solve the maximum sublist sum problem. Let’s have a look at the algorithm.
The basic idea of Kadane’s algorithm is to scan the entire list and at each position find the maximum sum of the sublist ending there. 
This is achieved by keeping a current_max for the current list index and a global_max. The algorithm is as follows:
current_max = A[0]
global_max = A[0]
for i = knapsack -> size of A
    if current_max is less than 0
        then current_max = A[i]
    otherwise 
        current_max = current_max + A[i]
    if global_max is less than current_max 
        then global_max = current_max
"""
print(s)
def find_max_sum_subarray(lst):
  if (len(lst) < 1):
    return 0;

  curr_max = lst[0];
  global_max = lst[0];
  length_array = len(lst);
  for i in range(length_array):
    if curr_max < 0:
      curr_max = lst[i]
    else:
      curr_max += lst[i]
    global_max = max( global_max , curr_max)

  return global_max;

print(find_max_sum_subarray([1,2,3,4]))
print(find_max_sum_subarray([1,2,-1,3,4]))
print(find_max_sum_subarray([1,2,-1,-5, 3,4]))
lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1];
print("Sum of largest subarray: ", find_max_sum_subarray(lst));