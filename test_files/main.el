programm
    // Declaration of variables.
    dim tempA, tempB als word
    dim iCount, jCount als word
    dim dim1, dim2 als word[2]
    dim mat1, mat2 als word[3][3]
    
    // Input parameters reading subroutine.
    sub Lesen:
        begin
        ein (dim1[0], dim1[1], dim2[0], dim2[1])
        rukkher
    
    // Input values for matrix subroutine (calls on yRead1).
    sub xRead1: 
        begin
        wenn (iCount < dim1[0]) dann
            gsub yRead1
            iCount = iCount + 1
        sonnst dann
            gsub next
        ende
        rukkher

    // Input values for matrix subroutine (calls on xRead1).
    sub yRead1: 
        begin
        wahrend (jCount < dim1[1])
            ein (mat1[iCount][jCount])
            jCount = jCount + 1
            ende
        rukkher

    // Clears counters when done reading matrix.
    sub next:  
        begin
        iCount = 0
        jCount = 0
        rukkher

    // Input values for matrix subroutine (calls on yRead2).
    sub xRead2: 
        begin
        wenn (iCount < dim2[0]) dann
            gsub yRead2
            iCount = iCount + 1
        sonnst dann
            gsub next
        ende
        rukkher

    // Input values for matrix subroutine (calls on xRead2).
    sub yRead2: 
        begin
        wahrend (jCount < dim2[1])
            ein (mat2[iCount][jCount])
            jCount = jCount + 1
        ende
        rukkher

    // Shifts selector along x axis of matrix.
    sub xShift: 
        begin 
        wenn (iCount < dim1[0]) dann
            gsub yShift
            aus ("\n")
            iCount = iCount + 1
        ende
        rukkher

    // Shifts selector along y axis of matrix.
    sub yShift: 
        begin
        wahrend (jCount < dim1[1]) 
            tempA = mat1[iCount][jCount]
            tempB = mat2[iCount][jCount]
            aus (tempA + tempB + " ")
            jCount = jCount + 1
        ende
        rukkher

begin

    gsub Lesen

    wenn (dim1[0] != dim2[0]) || (dim1[1] != dim2[1]) dann
        gsub Lesen
    ende

    iCount = 0
    jCount = 0

    gsub xRead1
    gsub xRead2
    gsub xShift

schluss