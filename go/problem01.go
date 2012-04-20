package main

import "fmt"

func is_fizzbuzz(i int) bool {
    return i % 5 == 0 || i % 3 == 0;
}

func main() {
    s := 0
    for i := 0; i < 1000; i++ {
        if is_fizzbuzz(i) {
            s += i
        }
    }
    fmt.Printf("Sum: %v\n", s)
}
