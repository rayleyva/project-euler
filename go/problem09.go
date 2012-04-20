package main

import "fmt"

func main() {
    for a := 1; a < 333; a++ {
        for b := a + 1; b < (1000-a-b); b++ {
            c := 1000 - b - a
            if a*a + b*b == c*c {
                fmt.Printf("%v\n", a*b*c)
                return
            }
        }
    }
}
