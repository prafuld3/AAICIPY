# multiprocessing can achieve through two ways. 1. through multiprocessing.process 1. through multiprocessing.Pool

# multiprocessing.process

""" Here we have worker1 function which takes n and m as argument and multiply them. this do this 100000000 times. 
we created 6 processes which do this work in seperate 6 cores. args takes multiple arguments. .start() start the process and .join() waits till process ends """

import multiprocessing

def worker1(n,m):
    count=0
    while count<100000000:
        n*m
        count+=1
    print(n*m+count)

p1= multiprocessing.Process(target=worker1, args=(10,100))
p2= multiprocessing.Process(target=worker1, args=(100,100))
p3= multiprocessing.Process(target=worker1, args=(10,100))
p4= multiprocessing.Process(target=worker1, args=(100,100))
p5= multiprocessing.Process(target=worker1, args=(10,100))
p6= multiprocessing.Process(target=worker1, args=(100,100))

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
p6.join()


###########################################################################################################################

# multiprocessing.processing dynamically.
# this code randomly generate numbers in 8 tuples and multiprocess it into 8 cores.

start= time.time()

def worker1(n,m):
    count=0
    while count<100000000:
        n*m
        count+=1
        
    print(n*m+count)
    
    # return df_final
    
lst=[]
arguments = [(random.randint(1,100),random.randint(1,100)) for x in range(8) ]
    
for i,j in zip([f'p{x}' for x in range(8)], arguments):
    i= multiprocessing.Process(target=worker1, args=j)
    lst.append(i)

for i in lst:
    i.start()

for i in lst:
    i.join()
    
end= time.time()
print(end-start)


#####################################################################################################################################

# using pool:

start= time.time()

def worker1(n,m):
    count=0
    while count<100000000:
        n*m
        count+=1
        
    print(n*m+count)
    
arguments = [(random.randint(1,100),random.randint(1,100)) for x in range(8) ]

p=multiprocessing.Pool(processes=8)
result= p.starmap(worker1, arguments)

end= time.time()

print(end-start)
