                           #FCFS ALGORITHM

#If arrival time either starts with zero(0) or not.

'''a is a list containing 5 lists. list a[0] denotes Arrival time(at) , a[1]
denotes Burst time(bt) , a[2] denotes Completion time(ct) , a[3] denotes
Turnaround time(tat) and a[4] denotes Waiting time(wt).'''

a=[[1,2,3,4,5],[4,2,6,7,5],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#gc is a variable initialising it to zero
gc=0
if(a[0][0]==0):
    for i in range(5):
        gc=gc+a[1][i]
        a[2][i]=gc
        a[3][i]=a[2][i]-a[0][i]
        a[4][i]=a[3][i]-a[1][i]

#condition for arrival time not starting with zero(0)    
else:
    gc=a[0][0]
    for i in range(5):
        gc=gc+a[1][i]
        a[2][i]=gc
        a[3][i]=a[2][i]-a[0][i]
        a[4][i]=a[3][i]-a[1][i]
    
#for printing at,tb,ct,tat and wt in tabular format    
print('at\tbt\tct\ttat\twt')
for i in range(5):    
    print(a[i][0],end='\t')
print(end='\n')
for i in range(5):    
    print(a[i][1],end='\t')
print(end='\n')  
for i in range(5):  
    print(a[i][2],end='\t')        
print(end='\n')   
for i in range(5):
    print(a[i][3],end='\t')
print(end='\n') 
for i in range(5):
    print(a[i][4],end='\t') 
print(end='\n')

#calculating average Waiting time
avg_wt=0
for i in range(5):    
    avg_wt=avg_wt+a[4][i]
print('The average waiting time is: ',avg_wt/5)    


      