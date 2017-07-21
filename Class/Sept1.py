num_list = [1,1,1,2,2,2,2,2,4,3,3,3,3,3,3,3]
used_num = []
while len(num_list) != 0:
    for num in num_list:
        if num not in used_num:
            num_count = num_list.count(num)
            used_num.append(num)
            num_list.remove(num)
    
