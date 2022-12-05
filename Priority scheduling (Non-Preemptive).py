                        #Priority Scheduling (Non-Preemptive) Algorithm
          
'''a is a list containing 5 lists. list a[0] denotes Arrival time(at) , a[1]
denotes Burst time(bt) ,a[2] denotes Priority , a[3] denotes Completion time(ct)
, a[4] denotes Turnaround time(tat) and a[5] denotes Waiting time(wt).'''

a=[[1,2,5,7,6],[8,5,7,9,2],[0,4,2,3,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
priority1=[0,4,2,3,1]                                                               
priority=[0,4,2,3,1]
g_c=0
if(a[0][0]==0):
    while(len(priority)>0):
        k=min(priority)
        i=priority1.index(k)
        g_c=g_c+a[1][i]
        a[3][i]=g_c
        a[4][i]=a[3][i]-a[0][i]
        a[5][i]=a[4][i]-a[1][i]
        priority.remove(k)    
 
else:
    g_c=a[0][0]
    while(len(priority)>0):
        k=min(priority)
        i=priority1.index(k)
        g_c=g_c+a[1][i]
        a[3][i]=g_c
        a[4][i]=a[3][i]-a[0][i]
        a[5][i]=a[4][i]-a[1][i]
        priority.remove(k)

#for printing at,bt,priority,ct,tat and wt in tabular format        
print('at\tbt\tpr\tct\ttat\twt')
for i in range(6):
    print(a[i][0],end='\t')
print(end='\n')
for i in range(6):
    print(a[i][1],end='\t')
print(end='\n')
for i in range(6):
    print(a[i][2],end='\t')
print(end='\n')
for i in range(6):
    print(a[i][3],end='\t')
print(end='\n')
for i in range(6):
    print(a[i][4],end='\t')
print(end='\n')

#Calculating average waiting time
avg_wt=0
for i in range(5):
    avg_wt=avg_wt+a[5][i]
print('the average waiting timeis: ' ,avg_wt/5)