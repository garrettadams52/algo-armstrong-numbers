# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    
    ans = []

    for i in numbers:
        sum = 0
        dig1 = i % 10
        dig2 = (i % 100 - dig1) // 10
        dig3 = (i - dig1 - dig2) // 100
        #print(dig1, dig2, dig3)

        if dig2 == 0 and dig3 == 0:
            ans.append(i)
        elif dig3 == 0 and dig2 == 0:
            sum = dig1**2 + dig2**2
            if sum == i:
                ans.append(i)
        else: 
            sum = dig1**3 + dig2**3 + dig3**3
            if sum == i:
                ans.append(i)
            

    return ans

my_list = [x for x in range(1000)]
print(find_armstrong_numbers(my_list))