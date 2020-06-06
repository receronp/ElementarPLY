programm
    // Declaration of variables.
    dim i, ask, size, None als word
    dim f_x, average, deviation, coeff als float
    dim arr1 als float[10]

    sub ask_option:
    begin
        aus("Enter next desired action:")
        aus("1 : Get results for a new array")
        aus("2 : Exit")
        ein(ask)
    rukkher

    sub zero_array:
    begin
        i = 0
        wahrend (i < 5)
            arr1[i] = None
            i = i + 1
        ende
    rukkher

    sub read:
    begin
        aus("Enter dimension of array:")
        ein(size)
        i = 0
        wahrend (i < size)
            aus("Enter value" + i)
            ein(arr1[i])
            i = i + 1
        ende
    rukkher

    sub mean_sd:
    begin
        mittlere(average,arr1)
        abweichung(deviation,arr1)
        coeff = deviation / average * 100
    rukkher

    sub output_result:
    begin
        aus("Mean value:" + average)
        aus("Standard Deviation:" + deviation)
        aus("Coefficient of variation:" + coeff)
    rukkher

begin
    ask = 1
    wahrend (ask == 1)
        gsub zero_array
        gsub read
        gsub mean_sd
        gsub output_result
        gsub ask_option
    ende
schluss
