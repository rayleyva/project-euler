package main

import (
    "fmt"
    "math"
)

func is_prime(i int64) bool {
    var j int64 = 0;
    if i < 2 {
        return false
    } else if i == 2 {
        return true
    }
    for j = 3; j <= sqrt(i); j+=2 {
        if i % j == 0 {
            return false
        }
    }
    return true
}

func sqrt(i int64) int64 {
    return int64(math.Sqrt(float64(i)))
}

func main() {
    var i, j int64
    i = 1 // since we're starting with 3, count two
    for j = 3; i < 10001; j += 2 {
        if is_prime(j) {
            i += 1
        }
    }
    // go adds 2 even if the check fails so subtract here
    fmt.Printf("%v\n", j-2)
}
