#Write a Python function to find out those label numbers that 
#are divisible by another label number and display how many such label numbers are there totally.

#lex_auth_0127136209566679041189

def check_numbers(num1,num2):
    #start writing your code here
    num_list = []
    count = 0 
    for i in range(num1, (num2//2)+1):
        num_list.extend([x for x in range(i+1, num2+1) if x%i==0])
        
    num_list=set(num_list)
    count=len(num_list)
    
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))
