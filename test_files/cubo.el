programm
    // Declaration of variables.
    dim count, valid, ask, w_input, i, j, k, None als word
    dim f_input, sum als float
    dim cubo als float[2][2][2]
    
    sub fill_cubo:
    begin
        i = 0
        wahrend (i < 2)
            j = 0
            wahrend (j < 2)
                k = 0
                wahrend (k < 2)
                    aus("Enter value for Mat1 [" + i + "] [" + j + "] [" + k + "]")
                    ein(cubo[i][j][k])
                    k = k + 1
                ende
                j = j + 1
            ende
            i = i + 1
        ende
    rukkher

begin
    gsub fill_cubo
    aus(cubo[1][0][1])
schluss
