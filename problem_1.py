def let_partner_hold_hands(array):
    k = []
    for i in range(len(array)-1):
#check if the adjacent element is one below or after
        if abs(array[i]-array[i+1])!= 1:
            for j in range(i+2, len(array)-1):
                if abs(array[j]-array[i])==1:
                    array[i+1], array[j] = array[j], array[i+1]

            # add element in our switch array
            k.append(i+1)
        else:
            i = i + 1
    return k
# test case
test_arr = [0,2,1,3]
print(let_partner_hold_hands(test_arr))



