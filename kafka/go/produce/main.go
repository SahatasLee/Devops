package main

import (
	"bufio"
	"context"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	"github.com/sahataslee/kafka/utils"

	"github.com/segmentio/kafka-go"
	"github.com/segmentio/kafka-go/sasl/scram"
)

func main() {
	// Connection
	Url := "10.111.0.124:9094"
	Topic := "topic-test"
	User := "user-test"
	Password := "UjfjpkUJgo0J"
	// cfg := config.KafkaConnCfg{
	// 	Url:   "10.111.0.124:9094",
	// 	Topic: "topic-test",
	// }
	// conn := utils.KafkaConn(cfg)

	mechanism, err := scram.Mechanism(scram.SHA512, User, Password)
	if err != nil {
		panic(err)
	}

	// Transports are responsible for managing connection pools and other resources,
	// it's generally best to create a few of these and share them across your
	// application.
	sharedTransport := &kafka.Transport{
		SASL: mechanism,
	}

	writer := kafka.Writer{
		Addr:      kafka.TCP(Url),
		Topic:     Topic,
		Balancer:  &kafka.LeastBytes{},
		Transport: sharedTransport,
	}

	// สร้างข้อมูลสำหรับส่งไปยัง Kafka
	for {
		// key := []byte(strconv.Itoa(i))
		// value := []byte("Hello, world" + strconv.Itoa(i) + "!")
		value := InputMessages()
		if value == "exit" {
			break
		}
		message := kafka.Message{
			Key:   []byte(strconv.Itoa(8)),
			Value: []byte(utils.CompressToJsonBytes(value)),
		}
		// สร้าง context สำหรับการส่งข้อมูลไปยัง Kafka
		err := writer.WriteMessages(context.Background(), message)
		if err != nil {
			fmt.Printf("Error sending message => (%v)\n", err)
			continue
		}
		log.Printf("Message sent to Kafka => (%s)\n", message.Value)
	}

	if err := writer.Close(); err != nil {
		log.Fatal("failed to close connection:", err)
	}
	log.Printf("Connection closed.")
}

func InputMessages() string {
	fmt.Print("Enter message: ")
	reader := bufio.NewReader(os.Stdin) // Create reader object
	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Printf("Error reading input: %v\n", err)
	}
	input = strings.TrimSpace(input)
	return input
}
