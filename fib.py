#just doing basic fib
fibarr = [] #just doing an array for giggles

def fibonacci(x , y):
    #gonna do first 20 numbers cause... why not..
    sum = x + y
    x = y
    y = sum
    return x, y

def fibonacci_alt(x , y): #alternate way to do it
    return y, x + y

def run(a, b, conf):
    fibarr.append(a)
    fibarr.append(b)
    if (conf == -1):
        for i in range(18):
            a, b = fibonacci(a,b)
            fibarr.append(b)
    else: 
        for i in range(18):
            a, b = fibonacci_alt(a,b)
            fibarr.append(b)

print("Lets start the sequence! (20 numbers) (original func)")
run(0,1,-1)


for i in range(len(fibarr)):
    print(f"{i} : {fibarr[i]}")

#just checking to see if the other works as well
print(f"FIB ARRAY SIZE: {len(fibarr)}")
fibarr.clear()
print(f"FIB ARRAY SIZE: {len(fibarr)}")

print("RUNNING ALT VERSION")
run(0,1,0)
for i in range(len(fibarr)):
    print(f"{i} : {fibarr[i]}")

