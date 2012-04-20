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
    var i, sum int64
    for i, sum = 3, 2; i < 2000000; i+=2 {
        if is_prime(i) {
            sum += i
        }
    }
    fmt.Printf("%v\n", sum)
}
