dict1 = {'1': [3,4,5], '2':[10,11,12]}

def check_bms_range_input(list1):
    if len(list1)== 0:
        return "Invalid Input"
    else :
        return check_bms_range_values(list1)

def check_bms_range_values(list, dict = dict1):
    dict3 = {}
    for range_id, range_value in dict.items():
        count = 0
        dict2 = {}
        for values in range_value:
            if values in sorted(list):
                count= count + list.count(values)
        dict2[range_id] = count
        dict3.update(dict2)
    return print_rangewithcount(dict3)

def print_rangewithcount( dict3, dict1 = dict1):
    for i , v in dict1.items():
        for j, vj in dict3.items():
            if i == j :
                #print("for range %d no of count are %s."%(v,vj))
                print( "The " + str(v) + " range has" +" " + str(vj) + " "+ "readings")
    return "Valid Input"

                

                
               
                
