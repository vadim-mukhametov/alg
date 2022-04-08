package main

func isTriangle(a, b, c int) bool {
	return (a+b) > c && (a+c) > b && (b+c) > a
}

func main() {
	println(isTriangle(4, 2, 3))
}
