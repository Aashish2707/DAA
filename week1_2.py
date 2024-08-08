def sort_product_ids():
    input_ids = input("Enter Product IDs (comma-separated): ")

    product_ids = [int(x.strip()) for x in input_ids.split(',')]
    
    product_ids.sort()

    sorted_ids = ','.join(map(str, product_ids))

    print("After Sorting Product IDs:")
    print(sorted_ids)

sort_product_ids()
