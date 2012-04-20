package main

import "fmt"

func fib() func() int64 {
    var a, b int64 = 1, 0
    return func() int64 {
        a, b = a+b, a
        return a
    }
}

func main() {
    fib_gen := fib()
    var i, sum, max int64 = 0, 0, 4 * 1e6
    for i = 0; i < max; i = fib_gen() {
        if i % 2 == 0 {
            sum += i
        }
    }
    fmt.Printf("%d\n", sum)
}
