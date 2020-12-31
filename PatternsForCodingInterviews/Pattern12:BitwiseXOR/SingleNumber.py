# In a non-empty array of integers, every number appears twice except for one, find that single number.

def find_single_number(arr):
  xor = 0
  for num in arr:
      xor ^= num
  return xor

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()