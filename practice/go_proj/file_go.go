package main   // определение пакета для текущего файла
import "fmt"    // подключение пакета fmt



func main() {
	var (
		user string = "Alex"
		age int = 30
		rights string = "admin, redactor"

	)

	fmt.Println(user)
	fmt.Println(age)
	fmt.Println(rights)

}