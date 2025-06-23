numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

key = 77
start = 0
end = len(numbers) - 1
found = False

while start <= end:
    mid = (start + end) // 2
    if numbers[mid] == key:
        print("Found element at pos:", mid)
        found = True
        break  # Exit loop once found
    elif numbers[mid] > key:
        end = mid - 1
    else:
        start = mid + 1

if not found:
    print(f"{key} not found in the list!")
