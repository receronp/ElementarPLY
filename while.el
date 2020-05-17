programm
    // Declaration of variables.
    dim tempA, tempB, tempC, tempD als word
    // dim A, B, C, D, E, F, G, H, I, J als word

begin
    tempA = 5
    tempB = 6
    tempD = 3

    wahrend (tempD > 0) || (tempA < 4)
        wahrend (tempA < tempB)
            tempC = tempA + 1
            wenn ( tempB != tempC ) dann
                tempC = tempB
                ende
            ende
        ende

schluss
