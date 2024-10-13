def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return

    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num) if num < 1 else n - 1
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def get_array_from_user():
    user_input = input("Enter numbers separated by spaces: ")
    return list(map(int, user_input.split()))

def print_menu():
    print("\nMenu:")
    print("1. Bucket Sort")
    print("2. Radix Sort")
    print("3. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice in ['1', '2']:
            arr = get_array_from_user()
            
            if choice == '1':
                bucket_sort(arr)
            elif choice == '2':
                radix_sort(arr)
                
            print("Sorted array:", arr)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
