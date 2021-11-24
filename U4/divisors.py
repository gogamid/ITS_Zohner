
import multiprocessing as mp

  
def div(start, end, N):
    for i in range(start, end+1):
        if N % i == 0:
            print(i)
    
  
  
if __name__ == "__main__":
    N = 10000000000
    b = 625000000

    data = []
    
    
    
    for i in range(1, N, b):
        st = i
        end = i+b-1
        t = (st, end, N)
        data.append(t)
        print (str(st) + "-" + str(end))
    

    process_pool = mp.Pool(mp.cpu_count())
    output = process_pool.starmap(div, data)

  
    print(data)
    print("Done!")
