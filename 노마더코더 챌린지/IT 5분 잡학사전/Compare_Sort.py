# https://www.daleseo.com/sort-insertion/

import time

test_arr=[i for i in range(10,0,-1)]
bubble_arr=test_arr.copy()
select_arr=test_arr.copy()
insert_arr=test_arr.copy()

print("origin : "+str(bubble_arr))

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
    list_count=len(list)
    for i in range(1, list_count):
        for j in range(i-1,-1,-1):
            if list[j+1]<list[j]: list[j+1], list[j] = list[j], list[j+1]
            else: continue
    return list

bubble_start=time.time()
print("1. bubble : "+str(sort_bubble(bubble_arr)))
bubble_end=time.time()
print("bubble time : "+str(bubble_end-bubble_start))

select_start=time.time()
print("2. select : "+str(sort_select(select_arr)))
select_end=time.time()
print("select time : "+str(select_end-select_start))

insert_start=time.time()
print("3. insert : "+str(sort_insert(insert_arr)))
insert_end=time.time()
print("insert time : "+str(insert_end-insert_start))