programm
    dim a, b, c  als word
    dim dim1, dim2 als word[2]
    dim mat1, mat2 als word[3][3]    
begin

a = 0
b = 1
c = 2
dim1[a] = 1
dim1[b] = 5 + dim1[a]
mat1[c][1] = dim1[0] + dim1[b]
mat1[1][2] = 7 + mat1[c][1]
mat2[0][2] = mat1[2][1] + mat1[1][2]
mat2[0][1] = mat1[2][1] + mat2[0][2]

schluss
