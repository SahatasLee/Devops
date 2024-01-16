package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/segmentio/kafka-go"
)

type KafkaConfig struct {
	ConsumeGroup string
}

func main() {
	config := KafkaConfig{
		ConsumeGroup: "group-test",
	}
	log.Println("Consume group", config.ConsumeGroup, "is ready...")

	// mechanism, err := scram.Mechanism(scram.SHA512, "user-test", "dNam4SJtKb81")
	// if err != nil {
	// 	panic(err)
	// }

	// dialer := &kafka.Dialer{
	// 	Timeout:       10 * time.Second,
	// 	DualStack:     true,
	// 	SASLMechanism: mechanism,
	// }

	// Handle SIGINT and SIGTERM.
	go func() {
		// Host Address
		kafkaAddress := "10.111.0.125:9094"
		focusTopic := "topic-test"

		// Create Kafka reader
		r := kafka.NewReader(kafka.ReaderConfig{
			Brokers:  []string{kafkaAddress},
			GroupID:  config.ConsumeGroup,
			Topic:    focusTopic,
			MinBytes: 10e3,
			MaxBytes: 10e6,
			MaxWait:  1 * time.Second,
			Dialer:   &kafka.Dialer{Timeout: 10 * time.Second, DualStack: true},
			// Dialer: dialer,
		})

		// defer r.Close() // ปิดการเชื่อมต่อกับ Kafka
		r.SetOffset(0) // กำหนด offset ให้กับ consumer ที่จะอ่านข้อมูล 0 คือ จะอ่านข้อมูลทั้งหมด
		ctx := context.Background()
		for {
			// อ่านข้อมูลจาก Kafka
			m, err := r.FetchMessage(ctx)
			if err != nil {
				// fmt.Printf("%v - %v - Kafka: %v\n\n", focusTopic, config.ConsumeGroup, err)
				log.Fatal("could not read message ", err)
				break
			}
			// แสดงข้อมูลที่อ่านได้
			fmt.Printf("message at topic/partition/offset %v/%v/%v: %s = %s\n", m.Topic, m.Partition, m.Offset, string(m.Key), string(m.Value))

			if err := r.CommitMessages(ctx, m); err != nil {
				log.Println("Kafka failed to commit messages:", err)
			}
		}

		if err := r.Close(); err != nil {
			log.Fatal("failed to close reader:", err)
		}
		log.Println("Connection close")
	}()

	// Handle SIGINT and SIGTERM.
	signalChan := make(chan os.Signal, 1)                      // สร้าง channel สำหรับรับค่าsignal ระหว่าง goroutine บน กับ os เลย 1 คือ กำหนดขนาดของ channel ให้มีขนาดเท่าไหร่(buffer)
	signal.Notify(signalChan, syscall.SIGINT, syscall.SIGTERM) // สั่งให้ channel รับค่า signal จาก os แล้วส่งค่าไปที่ channel ที่สร้างขึ้นมา
	<-signalChan                                               // รอรับค่าจาก channel ที่สร้างขึ้นมา ถ้ามีค่าส่งมา ก็จะทำการอ่านค่านั้นออกมา ถ้าไม่มีก็จะรออยู่จนกว่าจะมีค่าส่งมา
}
