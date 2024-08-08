def process_packages():
    times = []
    print("Enter time to reach destination (type 'done' to finish):")
    
    while True:
        time = input()
        if time.lower() == 'done':
            break
        try:
            times.append(int(time))
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

    order = input("Enter sorting order (asc/desc): ").strip().lower()
    
    if order == 'asc':
        times.sort()
    elif order == 'desc':
        times.sort(reverse=True)
    else:
        print("Invalid order. Sorting in ascending order by default.")
        times.sort()

    for time in times:
        print(time)

process_packages()
