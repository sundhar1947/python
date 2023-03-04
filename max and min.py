arr=[]
n=int(input("enter the size"))
for i in range(n):
    value=int(input("enter the value"))
    arr.append(value)
print("the given insorted array")
print(arr)
arr.sort()
small=min(arr)
print(small)
large=max(arr)
print(large)
