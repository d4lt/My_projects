def fibbonaci(n,f1,f2):

    f = f1 + f2

    if n == 0:
        print(f)
        return
    else:
        fibbonaci(n-1, f2, f)

n_fib = int(input("choose the n'th term in the fibonacci sequence: ")) 
f1 = 0
f2 = 1

fibbonaci(n_fib, f1, f2)