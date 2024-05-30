def transform_into_numbers(list_numbers):
    # Define an empty String to storage number
    temp_string_number = ""
    # Determine whether the collection is empty. If it is empty, return -1 and do not execute subsequent code.
    if len(list_numbers) == 0:
        return -1
    # Loop the elements in the collection and convert the data types
    # of the elements and add them to the empty string one after another
    for i in list_numbers:
        temp_string_number += str(i)
    # Return integer
    return int(temp_string_number)


if __name__ == '__main__':
    print(transform_into_numbers([8, 3, 5, 1]))