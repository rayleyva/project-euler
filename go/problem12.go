package main

import (
    "fmt"
    "math"
)

func triangle() func() int {
    i, sum := 0, 0
    return func() int {
        i += 1
        sum += i
        return sum
    }
}

func count_factors(n int) int {
    sqrt := int(math.Ceil(math.Sqrt(float64(n))))
    count := 0
    for i := 1; i <= sqrt; i++ {
        if n % i == 0 {
            // increase by 2 since there's another
            // factor on the opposite side of the sqrt
            count += 2
        }
    }
    return count
}

func main() {
    var sum int
    triangle_gen := triangle()
    for sum = 1; count_factors(sum) < 500; sum = triangle_gen() {
    }
    fmt.Printf("%v\n", sum)
}
