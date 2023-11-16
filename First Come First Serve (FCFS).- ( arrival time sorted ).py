                           #FCFS ALGORITHM   ( Arrival Time already Sorted)

#If arrival time either starts with zero(0) or not.


'''a is a list containing 5 lists. list a[0] denotes Arrival time(at) , a[1]
denotes Burst time(bt) , a[2] denotes Completion time(ct) , a[3] denotes
Turnaround time(tat) and a[4] denotes Waiting time(wt).'''


a=[]
lst=[]

n = int(input("Enter number of processes : "))

for i in range(2):
    print("enter elements in list: ",i+1)                        ''' while taking input , list 1 denotes Arrival time and list 2 denotes Burst time '''     
    for j in range(0, n):
        ele = int(input())
        # adding the element
        lst.append(ele)
    a.append(lst)
    lst=[]     

for i in range(3):
    for i in range(n):
        lst.append(0)
    a.append(lst)   
    lst=[] 
        
print(a)

#gc is a variable initialising it to zero
gc=0
if(a[0][0]==0):
    for i in range(n):
        gc=gc+a[1][i]
        a[2][i]=gc
        a[3][i]=a[2][i]-a[0][i]
        a[4][i]=a[3][i]-a[1][i]

#condition for arrival time not starting with zero(0)    
else:
    gc=a[0][0]
    for i in range(n):
        gc=gc+a[1][i]
        a[2][i]=gc
        a[3][i]=a[2][i]-a[0][i]
        a[4][i]=a[3][i]-a[1][i]
    
#for printing at,tb,ct,tat and wt in tabular format    
print('at\tbt\tct\ttat\twt')
for i in range(n):
    for j in range(5):    
        print(a[j][i],end='\t')
    print(end='\n')
       

#calculating average Turn Around time and Waiting time
avg_wt=0
avg_tat=0
for i in range(n):    
    avg_tat=avg_tat+a[3][i]
print('The average turn around time is: ',avg_tat/n)    
for i in range(n):    
    avg_wt=avg_wt+a[4][i]
print('The average waiting time is: ',avg_wt/n)    


























