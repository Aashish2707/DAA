def insertion_sort(arr, descending=False):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and ((key > arr[j]) if descending else (key < arr[j])):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sort_hotel_prices():

    input_prices = input("Enter Hotel Prices (one per line, type 'done' to finish): ")
    prices = []
    
    while input_prices.lower() != 'done':
        try:
            prices.append(int(input_prices))
        except ValueError:
            print("Please enter a valid number.")
        input_prices = input()

    order = input("Enter sorting order (asc/desc): ").strip().lower()
    descending = (order == 'desc')

    insertion_sort(prices, descending=descending)

    print("Sorted Hotel Prices:")
    for price in prices:
        print(price)

sort_hotel_prices()
