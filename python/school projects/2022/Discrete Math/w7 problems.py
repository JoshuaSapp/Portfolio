# Problem 9


a = [4,8,3,10,7,2,6,9,5,1]
b = [10,5,3,12,2,9,7,1,6,11,8,5]
c = [8,3,14,5,4,11,9,2,7,6,12,13,1,10]


def do_insertion_sort(in_list):
    count = 0
    for i in range(0,len(in_list)):
        check = i-1
        value1 = in_list[i]
        while (in_list[check]>value1) and (check >= 0):
            in_list[check+1] = in_list[check]
            check -= 1
            count += 1
        in_list[check+1] = value1
    return(count)

a_out = do_insertion_sort(a)
b_out = do_insertion_sort(b)
c_out = do_insertion_sort(c)

print()
print("insertion sort")
print()
print(f"a sorted:{a}, operaions:{a_out}")
print(f"b sorted:{b}, operaions:{b_out}")
print(f"c sorted:{c}, operaions:{c_out}")


a = [4,8,3,10,7,2,6,9,5,1]
b = [10,5,3,12,2,9,7,1,6,11,8,5]
c = [8,3,14,5,4,11,9,2,7,6,12,13,1,10]

def do_bubble_sort(in_list):
    out_list = in_list
    operations = 0
    list_len = len(in_list)
    for i in range(0,list_len):
        for x in range(0,list_len-i-1):
            if out_list[x] > out_list[x+1]:
                operations += 1
                temp = out_list[x]
                out_list[x] = out_list[x+1]
                out_list[x+1] = temp

    return([out_list,operations])

a_out = do_bubble_sort(a)
b_out = do_bubble_sort(b)
c_out = do_bubble_sort(c)

print()
print("bubble sort")
print()
print(f"a sorted:{a_out[0]}, operaions:{a_out[1]}")
print(f"b sorted:{b_out[0]}, operaions:{b_out[1]}")
print(f"c sorted:{c_out[0]}, operaions:{c_out[1]}")

# Problem 10

a = [6,31,46,49,49,55,56,59,65,82]
b =	[9,14,16,25,26,33,44,45,52,55,57,68,72,72,84,94]
c =	[11,14,23,29,31,36,41,41,44,47,47,50,65,70,82,85,88,89,92,96]

def do_linear_search(list,value):
    count = 0
    for number in list:
        count+= 1
        if number == value:
            return(count)
    return("NA")

print()
print("linear search")
print()
print(f"a took {do_linear_search(a,65)} operations to find 65")
print(f"b took {do_linear_search(b,65)} operations to find 65 (could not find value in given list)")
print(f"c took {do_linear_search(c,65)} operations to find 65")