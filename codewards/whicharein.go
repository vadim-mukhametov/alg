package main

import (
	"fmt"
	"sort"
	"strings"
)

func inArray(arr1, arr2 []string) []string {
	result := []string{}
	mapping := make(map[string]int)

	for _, j := range arr1 {
		for _, i := range arr2 {
			if strings.Contains(i, j) {
				mapping[j] += 1
				if mapping[j] == 1 {
					result = append(result, j)
				}
			}
		}
	}
	sort.Strings(result)

	return result
}

func main() {
	var a1 = []string{"cod", "code", "wars", "ewar", "ar"}
	var a2 = []string{}

	fmt.Println(inArray(a1, a2))
}
