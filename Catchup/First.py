'''
Check missing values in a list of consecutive numbers:

list_2 = [1, 4, 5, 6, 8, 12]

for (position, data) in enumerate(list_2):
    if(position+1 == len(list_2)):
        break
    if((list_2[position+1] - list_2[position]) > 1):
        print(f"Number {list_2[position] + 1} missing.")
        temp = list_2[position]
        while(temp != list_2[position+1]):
            temp += 1
            if((list_2[position+1] - temp) > 1):
                print(f"Number {temp+1} missing.")
'''

'''
Dictionaries
my_dict = {
    "Animal": "Elephant",
    "Car": "Porsche",
    "List": {
        "Inner List 1": [1, 2, 3, 4, 5],
        "Inner List 2": [6, 7, 8, 9, 10]
    }
}
merged_list = my_dict["List"]["Inner List 1"] + my_dict["List"]["Inner List 2"]
print(merged_list)
'''

'''
Functions
def summer(a = 0, b = 0, *numbers, **keyNumbers):
    print(a+b)
    for i in numbers:
        print(i)
    print(keyNumbers)
    
summer(10, 5, 12, 12, number_1=13, number_2 = 14)
'''

