package main

import "fmt"

func main() {
    digits := 20
    i := digits
    for ; ; i++ {
        all := true
        for j := 1; j <= digits; j++ {
            if i % j != 0 {
                all = false
                break
            }
        }
        if all {
            fmt.Printf("%v\n", i)
            break;
        }
    }
}
