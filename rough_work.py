list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,5,7,9]

def check_lists(list1,list2):
    for list in list2:
        if list not in list1:
            return False
    else:
        return True

check_lists(list1,list2)