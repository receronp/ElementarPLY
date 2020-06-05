programm
    // Declaration of variables.
    dim f, x als word
    
    // Input parameters reading subroutine.
    sub alfa:
    begin
        wenn (x > 1) dann
            f = f * x
            x = x - 1
            gsub alfa
        ende
    rukkher
    
begin
    aus("Enter number:")
    ein(x)
    f = 1
    gsub alfa
    aus(f)

schluss