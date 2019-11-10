x=1000000
sum=0
bulan=0
laba = [int(0), int (0), int (x) * .1 ,int (x) * .1, int (x) * .5, int (x) * .5, int (x) * .5, int (x)* .2 ]
print ("modal awal : ",x )
for i in laba :
    sum = sum+i
    bulan+=1
    print ("laba bulan", bulan ,"sebesar",i)
print ("laba adalah",sum )
