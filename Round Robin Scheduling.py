                   #ROUND ROBIN SCHEDULING

'''a is a list containing 5 lists. list a[0] denotes Arrival time(at) , a[1]
denotes Burst time(bt) , a[2] denotes Completion time(ct) , a[3] denotes
Turnaround time(tat) and a[4] denotes Waiting time(wt).'''

a=[[1,2,5,7,6],[2,8,5,9,7],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

#at1 is list of arrival time
a_t1=a[0]    

#bt1 is list of burst time and rq is ready queue (sorted arrival time)
b_t1=[2,8,5,9,7]     
rq=[1,2,5,6,7]

#t is time quantum whose value set to 5
t=5
l=[]

#gc is a variable initialise to zero(0)
gc=0
gc=rq[0]

while(len(rq)>0):     
    if(b_t1[a_t1.index(rq[0])]<t):
        gc=gc+(b_t1[a_t1.index(rq[0])])
        a[2][a_t1.index(rq[0])]=gc
        rq.remove(rq[0])
    elif(b_t1[a_t1.index(rq[0])]==t):
        gc=gc+b_t1[a_t1.index(rq[0])]
        a[2][a_t1.index(rq[0])]=gc
        rq.remove(rq[0])
    elif(b_t1[a_t1.index(rq[0])]>t):
        gc=gc+t 
        b_t1[a_t1.index(rq[0])]=(b_t1[a_t1.index(rq[0])])-t
        rq.append(rq[0])
        rq.remove(rq[0])

for i in range(len(a[0])):
    a[3][i]=a[2][i]-a[0][i]
    a[4][i]=a[3][i]-a[1][i]

#for printing at,bt,ct,tat and wt in tabular format    
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
    
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
            
        
