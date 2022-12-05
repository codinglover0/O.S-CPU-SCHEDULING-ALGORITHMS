                       #SJF ALGORITHM 

'''a is a list containing 5 lists. list a[0] denotes Arrival time(at) , a[1]
denotes Burst time(bt) , a[2] denotes Completion time(ct) , a[3] denotes
Turnaround time(tat) and a[4] denotes Waiting time(wt).'''
     
a=[[0,2,5,15,10],[5,9,7,6,3],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
at=a[0]
bt=a[1]

#at1 is sorted arrival time list and bt1 is list of corresponding burst time.
at1=[0,2,5,10,15]
bt1=[5,9,7,3,6]
k=[] 
l=[]

#gc is a variable initialising it to zero.
gc=0
gc=gc+a[1][0]
a[2][0]=gc
a[3][0]=a[2][0]-a[0][0]
a[4][0]=a[3][0]-a[1][0]
at1.remove(at1[0])
bt1.remove(bt1[0])

while(len(at1)>0):
    for i in range(len(at1)):
        if(at1[i]<=gc):
            l.append(at1[i])
            k.append(at.index(l[i]))
            c=[bt[i] for i in k]     #appending burst time in list c, of index k in list bt
    m=min(c)
    gc=gc+m
    n=bt.index(m)
    a[2][n]=gc
    a[3][n]=a[2][n]-a[0][n]
    a[4][n]=a[3][n]-a[1][n]
    at1.remove(at[n])
    bt1.remove(bt[n])
    k=[]
    l=[]                    

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

#Calculating average waiting time
avg_wt=0
for i in range(5):
    avg_wt=avg_wt+a[4][i]
print('the average waiting time is: ' ,avg_wt/5)
    



    













        
            
                 
 













