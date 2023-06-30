string='588432347423122345'
numbers = [int(char) for char in string]
consecutive_numbers = []
current_number = None
b=[]
for num in numbers:
    if current_number is None:
        consecutive_numbers.append(str(num))
    elif num == current_number + 1:
        consecutive_numbers.append(str(num))
    else:
        if len(consecutive_numbers) > 1:
            
            b.append(''.join(consecutive_numbers))
        
        consecutive_numbers = [str(num)]
    
    current_number = num

if len(consecutive_numbers) > 1:
    b.append(''.join(consecutive_numbers))
print(b)  



 