def get_fibonacci_number(position):
    if position == 1 or position == 2:
        return 1
    elif position <= 0:
        print("Done with recursion")
        pass
    else:
        return ((get_fibonacci_number(position-1))+(get_fibonacci_number(position -2)))
    
def get_fibonacci_number_sequence(number):
    list = []
    for i in range(0,number):
        list.append(get_fibonacci_number(i+1))
    return list

if __name__ == "__main__":
    pass