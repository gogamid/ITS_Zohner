
import threading
l = []
  
def div(start, end, N):
    for i in range(start, end+1):
        if N % i == 0:
            print(i)
    
  
  
if __name__ == "__main__":
    N = 1433234323232
    b = 43322323434
    
    
    threads = []
    for i in range(1, N, b):
        st = i
        end = i+b-1
        if end > N:
            end = N
        print (str(st) + "-" + str(end))
        t = threading.Thread(target=div, args=(st , end, N))
        threads.append(t)

    for i in threads:
        i.start()

    for i in threads:
        i.join()
  

  

    print("Done!")