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
    for j = 3; j < sqrt(i); j+=2 {
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
    var i, largest, num int64 = 0, 0, 600851475143
    for i = 3; i < sqrt(num); i+= 2 {
        if num % i == 0 && is_prime(i) {
            largest = i
        }
    }
    fmt.Printf("Largest: %v\n", largest)
}
