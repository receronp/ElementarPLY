programm
    // Declaration of variables.
    dim i, j, k, l, ask, size als word
    dim f_input, temp als float
    dim arr1 als float[10]
    
    sub read:
    begin
        aus("Enter dimension of array:")
        ein(size)
        i = 0
        wahrend (i < size)
            aus("Enter value" + i)
            ein(f_input)
            arr1[i] = f_input
            i = i + 1
        ende
    rukkher

    sub sort:
    begin
        i = 0
        wahrend (i < size)
            j = 0
            l = size - i - 1
            wahrend (j < l)
                k = j + 1
                wenn (arr1[j] > arr1[k]) dann
                    temp = arr1[k]
                    arr1[k] = arr1[j]
                    arr1[j] = temp
                ende
                j = k
            ende
            i = i + 1
        ende
    rukkher

    sub output:
    begin
        aus("Sorted array is:")
        i = 0
        wahrend (i < size)
            aus(arr1[i])
            i = i + 1
        ende
    rukkher

begin

    ask = 1
    wahrend (ask == 1)
        gsub read
        gsub sort
        gsub output
        aus("Order another vector? Input: 1: yes, 2: exit")
        ein(ask)
    ende
schluss
