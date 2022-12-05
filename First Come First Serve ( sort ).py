                     #FCFS ALGORITHM

#if arrival time is not sorted.

'''a is a list containing 5 lists. list a[0] denotes Arrival time(at) , a[1]
denotes Burst time(bt) , a[2] denotes Completion time(ct) , a[3] denotes
Turnaround time(tat) and a[4] denotes Waiting time(wt).'''

a=[[1,0,5,2,3],[4,2,6,9,5],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#at1 and at are lists of arrival time 
at1=a[0]
at=[1,0,5,2,3]

#gc is a variable initialising it to zero
g_c=0
while(len(at)>0):
    m=min(at)
    i=at1.index(m)               
    g_c=g_c+a[1][i]
    a[2][i]=g_c
    a[3][i]=a[2][i]-a[0][i]
    a[4][i]=a[3][i]-a[1][i]
    at.remove(m)
    
#for printing at,tb,ct.tat,and wt in tabular format
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


#calculating average waiting time
avg_wt=0
for i in range(5):
    avg_wt=avg_wt+a[4][i]
print('The averge waiting time is: ' ,avg_wt/5)
