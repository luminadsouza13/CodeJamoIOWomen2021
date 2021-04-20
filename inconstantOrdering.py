if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N=int(input())
        list1=list(map(int,raw_input().strip().split()))[:N]
        list2=[1]
        for j in range(len(list1)): 
          list2.append(list1[j])
        stringval="A"
        string=""
        charvalstarts=65
        charvalends=91
        prev="A"
        
        for iby2 in range(1,N,2):
              charvalstarts=65
              for j in range(iby2,iby2+2):
                        if(j%2!=0):
                            for block in range(list2[j]):
                                string=string+chr(charvalstarts+1)
                                charvalstarts+=1
                        else:
                            charvalstarts=65
                            for block in range(list2[j]):
                                string=string+chr(charvalstarts)
                                charvalstarts+=1
                            string=string[::-1]
                            
                            if(ord(prev) <= ord(string[0])):
                                val=ord(string[0])+1
                                stringval=stringval[:prevind-1] + chr(val) 

                        stringval=stringval+string
                        prev=string[-1]
                        prevind=len(stringval)
                        string=""  
        if(N%2!=0):
                charvalstarts=65
                for block in range(list2[j+1]):
                    string=string+chr(charvalstarts+1)
                    charvalstarts+=1

        stringval=stringval+string
        print("Case #%s: %s"% ((i+1),str(stringval)))