if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N=int(input())
        list1=list(map(int,raw_input().strip().split()))[:N]

        list1.sort()
        minval=0
        prev=0
        val=0
        for j in range(N):
           prev=val
           val=list1[j]
           if(j==0):
             treats=1
             minval=minval+1
           else:
             if(prev == val):
               
                minval=minval+treats
             else:
                treats=treats+1
                minval=minval+treats
              
        print("Case #%s: %s"% ((i+1),(minval)))
        
      