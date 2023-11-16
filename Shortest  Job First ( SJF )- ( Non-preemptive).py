                                                                    #SJF ( NON-PREEMPTIVE)

#If arrival time either starts with zero(0) or not.


'''a is a list containing 5 lists. list a[0] denotes Arrival time(at) , a[1]
denotes Burst time(bt) , a[2] denotes Completion time(ct) , a[3] denotes
Turnaround time(tat) and a[4] denotes Waiting time(wt).'''


a=[]
lst=[]

n = int(input("Enter number of processes : "))

for i in range(2):
    print("enter elements in list: ",i+1)                           
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

#bt1 is unsorted list of burst time ,bt is sorted list of burst time and at is sorted list of arrival time.
bt1=a[1]
#gc is a variable initialising it to zero
at=sorted(a[0])
i=0
bt=sorted(a[1])
g_c=at[0]
i=a[0].index(g_c)
g_c=g_c+bt1[i]
b=bt1[i]
a[2][i]=g_c
a[3][i]=a[2][i]-a[0][i]
a[4][i]=a[3][i]-a[1][i]

i=0
while(i!=n):
    m=bt[i]
    j=bt1.index(m)
    if(m!=b):
        g_c=g_c+m
        a[2][j]=g_c
        a[3][j]=a[2][j]-a[0][j]
        a[4][j]=a[3][j]-a[1][j]
    i+=1


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


        




















        
            
                 
 













