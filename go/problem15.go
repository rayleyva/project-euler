package main

import (
    "fmt"
    "math/big"
)

func main() {
    var bincoeff = new(big.Int);
    bincoeff.Binomial(40, 20)
    fmt.Printf("%v\n", bincoeff)
}
