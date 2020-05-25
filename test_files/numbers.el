programm
    dim iNum, iDiv, iMod als word

begin

aus("Ingrese entero:")
ein(iNum)

iDiv = iNum / 10
iMod = iNum % 10

wahrend (iDiv > 0) || (iMod > 0)
    wenn(iMod > 4) dann
        wenn(iMod > 7) dann
            wenn(iMod == 9) dann
                aus("NUEVE")
            sonnst dann
                aus("OCHO")
            ende
        sonnst dann
            wenn(iMod > 6) dann
                aus("SIETE")
            sonnst dann
                wenn(iMod == 6) dann
                    aus("SEIS")
                sonnst dann
                    aus("CINCO")
                ende
            ende
        ende    
    sonnst dann
        wenn(iMod > 2) dann
            wenn(iMod == 4) dann
                aus("CUATRO")
            sonnst dann
                aus("TRES")
            ende
        sonnst dann
            wenn(iMod > 1) dann
                aus("DOS")
            sonnst dann
                wenn(iMod == 1) dann
                    aus("UNO")
                sonnst dann
                    aus("CERO")
                ende
            ende
        ende    
    ende

    iMod = iDiv % 10
    iDiv = iDiv / 10
ende

schluss
