package main

import (
    "fmt"
    "./helpers"
)

func main() {
    var i, j int64
    i = 1 // since we're starting with 3, count two
    for j = 3; i < 10001; j += 2 {
        if helpers.IsPrime(j) {
            i += 1
        }
    }
    // go adds 2 even if the check fails so subtract here
    fmt.Printf("%v\n", j-2)
}
