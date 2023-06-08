#..............................Pascal's Triangle..............................




#function to print pascal’s triangle
def pascalTriangle(row):
    #outer loop for each row
    for i in range(0,row):
        #coeff variable
        c=1
        #inner loop to print space in the row
        for j in range(1,row-i):
            #print blank space
            print("  ",end=" ")
        #inner loop to print number elemts in a particular row
        for k in range(0,i+1):
            #print space seperated elements in  each row
            print("  ",c,end=" ")
            #calculate c
            c=c*(i-k)//(k+1)
        #prints new line for new row
        print()

#input
n=int(input("Enter the number of rows:  "))
#function call
pascalTriangle(n)






#...................................OR..................CODING NINJA SOLUTION ....FUNCTION ONLY.............
def printPascal(row):
    res = [[1]]
    for i in range(row-1):
        temp = [0]+res[-1]+[0]
        r=[]
        for j in range(len(res[-1])+1):
            r.append(temp[j]+temp[j+1])
        res.append(r)
    return res