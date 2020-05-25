programm
    // Declaration of variables.
    dim tempA, tempB, tempC, tempD als word
    // dim A, B, C, D, E, F, G, H, I, J als word

begin
    tempA = 1 * 2 + 3 * ( 4 - 5 * ( 6 * 7 + 8 ) + 9 * 10 ) * 11 + 12
    tempB = (1 + 2) * 3 + ( 4 + 5 ) * ( 6 + 7 * ( 8 * 9 + 10) * 11 + 12)
    tempD = 5
    wenn ( tempA > tempB ) dann
        tempC = tempA
        wenn ( tempB != tempC ) dann
            tempC = tempB
        sonnst dann
            tempB = tempC
        ende
    sonnst dann
        wenn (tempD <= tempA) dann
            tempD = tempB
        ende
    ende

schluss
