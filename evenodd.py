#Program to check even and odd numbers in a given range.
start=int(input("enter the starting number:"))
end=int(input("enter the end number:"))

print(f"even and odd numbers between {start}and {end}")

for num in range(start,end+1):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
