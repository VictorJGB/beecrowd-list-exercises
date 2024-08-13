N = int(input())

result_array = []

for i in range (N):
    number = int(input())
    result = ''
    
    if (number % 2 == 0): 
        result = 'EVEN'
    if (number % 2 != 0): 
        result = 'ODD'
    if (number > 0): 
        result = result + ' POSITIVE'
    if (number < 0): 
        result = result + ' NEGATIVE'
    if (number == 0):
        result = 'NULL'
        
    result_array.append(result)
    
for result in result_array:
    print(result)