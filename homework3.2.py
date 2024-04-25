from random import randint, sample
min = 1 
max = 36
quantity = 5



def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1. <= quantity <= (max - min +1)):
     return []
     
    result_array = set()
    while len(result_array) != quantity:
     result_array.add(randint(min, max))
     return sorted (result_array)
       


print(sorted(sample(range(min, max), quantity)))
    


    



