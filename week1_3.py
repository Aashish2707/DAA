def sort_order_priorities():
    
    input_priorities = input("Enter orders Priority Number (comma-separated): ")

    priority_numbers = [int(x.strip()) for x in input_priorities.split(',')]

    priority_numbers.sort()
    
    sorted_priorities = ','.join(map(str, priority_numbers))
    print("After Sorting Orders Priority:")
    print(sorted_priorities)

sort_order_priorities()
