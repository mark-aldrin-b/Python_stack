
def countdown(num):
    new_list = []
    for x in range(num, -1, -1):
        new_list.append(x)
        print(new_list)
    return new_list

z_countdown = countdown(5)
print(z_countdown) 


def p_and_r(lists):
    print(lists[0])
    return lists[1]

print(p_and_r([1,2]))


def firstplus_length(lists):
    sum = lists[0] + len(lists)
    return sum

print(firstplus_length([1,2,3,4,5]))
print(firstplus_length([5,6,7,4,3,4,11,45]))


def greatertahn_second(lists):
    if len(lists) < 2:
            return False
    else:
        new_lists = []
        for x in range(0,len(lists)):
            if lists[x] > lists[1]:
                new_lists.append(lists[x])
        print("length is",len(new_lists))
        return ("num > second are",new_lists)

print(greatertahn_second([5,2,3,2,1,4]))
print(greatertahn_second([3]))


def length_and_value(num1, num2):
    lists = []
    for x in range(num1):
        lists.append(num2)
        # print(lists)
    return lists

print(length_and_value(4,7))
print(length_and_value(6,2))


"""
Example: length_and_value(4,7) should return [7,7,7,7]
Example: length_and_value(6,2) should return [2,2,2,2,2,2]"""

