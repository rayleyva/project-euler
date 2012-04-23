package main

import (
    "fmt"
    "strconv"
    "strings"
)

const triangle_str = `75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23`

func get_triangle() [][]int {
    lines := strings.Split(triangle_str, "\n")
    triangle := make([][]int, len(lines), len(lines))
    for i, line := range(lines) {
        numbers := make([]int, i+1, i+1)
        for j, number_str := range(strings.Split(line, " ")) {
            numbers[j], _ = strconv.Atoi(number_str)
        }
        triangle[i] = numbers
    }
    return triangle
}

func max(nums ...int) int {
    n := 0
    for _, i := range(nums) {
        if i > n {
            n = i
        }
    }
    return n
}

func main() {
    tri := get_triangle()
    for i := 1; i < len(tri); i++ {
        for j, num := range(tri[i]) {
            var top_l, top_r int
            if j > 0 {
                top_l = j - 1
            } else {
                top_l = 0
            }
            if j < len(tri[i-1]) {
                top_r = j
            } else {
                top_r = top_l
            }
            l := tri[i-1][top_l] + num
            r := tri[i-1][top_r] + num
            tri[i][j] = max(l, r)
        }
    }
    fmt.Printf("%v\n", max(tri[len(tri)-1]...))
}
