programm
    // Declaration of variables.
    dim count, valid, ask, w_input, i, j, k, None als word
    dim f_input, sum als float
    dim sizeA, sizeB als word[2]
    dim matA, matB, matC als float[5][5]
    
    sub read:
    begin
        count = 0
        aus("Enter dimensions for matrix 1:")
        wahrend (count < 2)
            ein(w_input)
            sizeA[count] = w_input
            count = count + 1
        ende
        count = 0
        aus("Enter dimensions for matrix 2:")
        wahrend (count < 2)
            ein(w_input)
            sizeB[count] = w_input
            count = count + 1
        ende
    rukkher

    sub fill_mat:
    begin
        i = 0
        wahrend (i < sizeA[0])
            j = 0
            wahrend (j < sizeA[1])
                aus("Enter value for Mat1 [" + i + "] [" + j + "]")
                ein(f_input)
                matA[i][j] = f_input
                j = j + 1
            ende
            i = i + 1
        ende
        i = 0
        wahrend (i < sizeB[0])
            j = 0
            wahrend (j < sizeB[1])
                aus("Enter value for Mat2 [" + i + "] [" + j + "]")
                ein(f_input)
                matB[i][j] = f_input
                j = j + 1
            ende
            i = i + 1
        ende
    rukkher

    sub add_mat:
    begin
        wenn (sizeA[0] == sizeB[0]) && (sizeA[1] == sizeB[1]) dann
            valid = 1
            gsub fill_mat
            i = 0
            wahrend (i < sizeA[0])
                j = 0
                wahrend (j < sizeA[1])
                    matC[i][j] = matA[i][j] + matB[i][j]
                    j = j + 1
                ende
                i = i + 1
            ende
        sonnst dann
            aus("Dimensions must be the same!")
        ende
    rukkher

    sub zero_mat:
    begin
        i = 0
        wahrend (i < 5)
            j = 0
            wahrend (j < 5)
                matC[i][j] = None
                j = j + 1
            ende
            i = i + 1
        ende
    rukkher

    sub mult_mat:
    begin
        wenn (sizeA[1] == sizeB[0]) dann
            valid = 1
            gsub fill_mat
            i = 0
            wahrend (i < sizeA[0])
                j = 0
                wahrend (j < sizeB[1])
                    k = 0
                    sum = 0
                    wahrend (k < sizeB[0])
                        sum = sum + matA[i][k] * matB[k][j]
                        k = k + 1
                    ende
                    matC[i][j] = sum
                    j = j + 1
                ende
                i = i + 1
            ende
        sonnst dann
            aus("Matrix dimensions cannot be multiplied!")
        ende
    rukkher

    sub out_mat:
    begin
        i = 0
        aus("Resulting matrix is:")
        wahrend (i < sizeA[0])
            aus("[" + matC[i][0] + matC[i][1] + matC[i][2] + matC[i][3] + matC[i][4] + "]")
            i = i + 1
        ende
    rukkher

    sub ask_option:
    begin
        aus("Enter next desired action:")
        aus("1 : Matrix addition")
        aus("2 : Matrix multiplication")
        aus("3 : Exit")
        ein(ask)
    rukkher

begin
    gsub ask_option
    wahrend (ask != 3)
        valid = 0
        gsub read
        gsub zero_mat
        wenn (ask == 1) dann
            gsub add_mat
        ende
        wenn (ask == 2) dann
            gsub mult_mat
        ende
        wenn (valid == 1) dann
            gsub out_mat
        ende
        gsub ask_option
    ende

schluss
