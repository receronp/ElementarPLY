programm
    dim a, b, c, d als float
    dim prev, res, num, den als float
    dim fnum, count, ask, even als word
    dim d1, d2, n1, n2 als float
    dim root1, root2 als float
    dim in_sq als float

begin

ask = 1

wahrend (ask == 1)
    aus("Enter value for a:")
    ein(a)
    aus("Enter value for b:")
    ein(b)
    aus("Enter value for c:")
    ein(c)
    aus("Enter amount of iterations to run:")
    ein(d)

    in_sq = b * b - 4 * a * c
    wenn (in_sq > 0) dann
        count = 0
        wahrend (count < d)
            n2 = 1.0
            wenn (count == 0) dann
                res = 1.0
                num = 1.0
                n1 = 1.0
                d1 = 1.0
                d2 = 1.0
                prev = 0.0
            sonnst dann
                wenn (in_sq < 2) dann
                    n1 = n1 * (in_sq - 1)
                sonnst dann
                    n1 = n1 * (1 / in_sq- 1)
                ende
                fnum = 2 * count
                wahrend (fnum > 0)
                    n2 = n2 * fnum
                    fnum = fnum - 1
                ende
                d1 = count * d1
                d2 = d2 * 4
                num = n2 * n1

                even = count % 2
                wenn (even != 0) dann
                    num = -1 * num
                ende
                den = (1 - 2 * count) * (d1 * d1) * d2
                prev = res
                res = num / den
            ende
            count = count + 1
            res = res + prev
        ende

        wenn (in_sq > 2) dann
            res = 1 / res
        ende
        
        root1 = (-1 * b + res) / (2 * a)
        root2 = (-1 * b - res) / (2 * a)
        aus("Roots are:")
        aus(root1)
        aus(root2)
        
    sonnst dann
        aus("Imaginary roots.")
    ende
    aus("Run again: 1: yes, 2: exit")
    ein(ask)
ende
schluss
