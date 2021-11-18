##Sum of even number from 1 to 100 including 1 and 100
even_sum=0
odd_sum=0
for i in range(0,101):
    if i%2==0:
        even=i
        even_sum += even
    else:
        odd=i
        odd_sum +=odd

print(f"Sum of even numbers from 1 to 100 is {even_sum}")
print(f"Sum of odd numbers from 1 to 100 is {odd_sum}")