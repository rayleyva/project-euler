package main

import (
    "fmt"
    "math"
)

func pow(b float64, e int) int {
    return int(math.Pow(b, float64(e)))
}

func get_digits(i int) []int {
    // the number of digits is equal to the ceiling of the logb10
    digit_count := int(math.Ceil(math.Log10(float64(i))))

    // create a slice to hold the digits
    digits := make([]int, digit_count, digit_count)

    for j := 0; j < digit_count; j++ {
        power := pow(10, digit_count - j - 1)
        dig := i / power
        i -= (dig * power)
        digits[j] = dig
    }
    return digits
}

func is_palindrome(digits []int) bool {
    j := len(digits)
    for i := 0; i < j; i++ {
        j -= 1
        if digits[i] != digits[j] {
            return false
        }
    }
    return true
}

func main() {
    largest := 1
    for i := 100; i < 1000; i++ {
        for j := 100; j < 1000; j++ {
            product := i * j
            if is_palindrome(get_digits(product)) && product > largest {
                largest = product
            }
        }
    }
    fmt.Printf("%v\n", largest)
}
