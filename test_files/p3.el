programm
    // Declaration of variables.
    dim w_x, w_y, w_result, ask, inputs als word
    dim f_x, f_y, f_result als float

    sub ask_option:
    begin
        aus("Enter next desired action:")
        aus("1 : X factorial --> Asks for one input")
        aus("2 : X^(y) --> Asks for two inputs")
        aus("3 : X + X * Y% --> Asks for two inputs")
        aus("4 : Exit")
        ein(ask)
        wenn (ask != 1) dann
            inputs = 2
        ende
    rukkher

    sub read:
    begin
        aus("Enter x value:")
        wenn (ask < 3) dann
            ein(w_x)
        sonnst dann
            ein(f_x)
        ende
        wenn (inputs == 2) dann
            aus("Enter y value:")
            wenn (ask == 2) dann
                ein(w_y)
            sonnst dann
                ein(f_y)
            ende
        ende
    rukkher

    sub factorial:
    begin
        w_result = 1
        wahrend (w_x > 0)
            w_result = w_result * w_x
            w_x = w_x - 1
        ende
    rukkher

    sub power:
    begin
        w_result = w_x
        wahrend (w_y > 1)
            w_result = w_result * w_x
            w_y = w_y - 1
        ende
    rukkher

    sub percent:
    begin
        f_result = f_x + f_x * f_y / 100
    rukkher

    sub out_result:
    begin
        wenn (ask < 3) dann
            aus("Result:" + w_result)
        ende
        wenn (ask == 3) dann
            aus("Result:" + f_result)
        ende
    rukkher

begin
    gsub ask_option
    wahrend (ask < 4)
        gsub read
        wenn (ask == 1) dann
            gsub factorial
        ende
        wenn (ask == 2) dann
            gsub power
        ende
        wenn (ask == 3) dann
            gsub percent
        ende
        gsub out_result
        gsub ask_option
    ende
schluss
