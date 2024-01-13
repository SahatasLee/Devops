package main

import (
	"bufio"
	"context"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/segmentio/kafka-go"
)

func main() {
	kafkaAddress := "localhost:9092"
	focusTopic := "logs"

	// Create Kafka writer
	writer := kafka.NewWriter(kafka.WriterConfig{
		Brokers: []string{kafkaAddress},
		Topic:   focusTopic,
	})

	reader := bufio.NewReader(os.Stdin) // Create reader object

	fmt.Print("Enter a number: ")
	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Printf("Error reading input: %v\n", err)
	}

	input = strings.Trim(input, "\n")
	num, err := strconv.Atoi(input)
	if err != nil {
		fmt.Printf("Invalid input: %v\n", err)
	}

	// สร้างข้อมูลสำหรับส่งไปยัง Kafka
	for i := 1; i <= num; i++ {
		key := []byte(strconv.Itoa(i))
		value := []byte("Hello, world" + strconv.Itoa(i) + "!")
		message := kafka.Message{
			Key:   key,
			Value: value,
		}
		// สร้าง context สำหรับการส่งข้อมูลไปยัง Kafka
		ctx := context.Background()
		err = writer.WriteMessages(ctx, message)
		if err != nil {
			fmt.Printf("Error sending message: %v\n", err)
			continue
		}

		log.Printf("Message sent to Kafka: %s\n", message.Value)
	}

	writer.Close()
}
