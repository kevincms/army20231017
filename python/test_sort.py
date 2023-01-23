test_arr=[i for i in range(10,0,-1)]
bubble_arr=test_arr.copy()

print(bubble_arr)

def sort_bubble(list):
    list_count=len(list)
    for i in range(list_count):
        for j in range(list_count-i-1):
            if list[j]>list[j+1]: list[j], list[j+1] = list[j+1], list[j]
    return list

def sort_select(list):
    list_count=len(list)
    for i in range(list_count):
        for j in range(i,list_count):
            if list[i]>list[j]: list[i], list[j] = list[j], list[i]
    return list

def sort_insert(list):
    pass
    # list_count=len(list)
    # for i in range(list_count):
    #     for j in range(i,list_count):
    #         if list[i]>list[j]: list[i], list[j] = list[j], list[i]
    # return list

# print(sort_bubble(bubble_arr))
print(sort_select(bubble_arr))