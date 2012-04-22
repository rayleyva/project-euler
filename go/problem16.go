package main

import (
    "fmt"
    "math/big"
)

func main() {
    var z = new(big.Int)
    sum := 0
    digits := z.Exp(big.NewInt(2), big.NewInt(1000), nil).String()
    for _, digit := range(digits) {
        sum += int(digit) - int('0')
    }
    fmt.Printf("%v\n", sum)
}
