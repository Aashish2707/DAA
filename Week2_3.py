def insertion_sort(hotel_prices):
    for i in range(1, len(hotel_prices)):
        key = hotel_prices[i]
        j = i - 1
        while j >= 0 and key > hotel_prices[j]:
            hotel_prices[j + 1] = hotel_prices[j]
            j -= 1
        hotel_prices[j + 1] = key
    return hotel_prices

def main():
    hotel_prices = []
    while True:
        price = input("Enter Hotel Price (or 'done' to finish): ")
        if price.lower() == 'done':
            break
        hotel_prices.append(int(price))
    
    sorted_prices = insertion_sort(hotel_prices)
    print("Hotel Prices in Descending Order:")
    for price in sorted_prices:
        print(price)

if _name_ == "_main_":
    main()