class CartesianProduct:
    def get_cartesian_product(A, B, C, n, n1,n2):
 
        for i in range(0,n):
            for j in range(0,n1):
                for k in range(0,n2):
                    print("[",A[i],", ",B[j],",",C[k],"], ",sep="",end="")
 
# Driver code
A = [ 1, 2 ] # first set
B = ['a','b'] # second set
C = [ 3.5,4.7 ]
 
n1 = len(A) # sizeof(arr1[0])
n2 = len(B) # sizeof(arr2[0]);
n3 = len(C)
 
get_cartesian_product(A,B,C, n1, n2, n3);
