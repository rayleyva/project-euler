package main

import "fmt"

func main() {
    var i, sqsum, sumsq int64

    for i = 1; i <= 100; i++ {
        sqsum += (i*i)
        sumsq += i
    }
    sumsq *= sumsq
    fmt.Printf("%v\n", sumsq - sqsum)
}
