package main

import (
	"context"
	"log"
	"time"

	"github.com/segmentio/kafka-go"
	"github.com/segmentio/kafka-go/sasl/scram"
)

func main() {
	// Connection
	Urls := []string{"10.111.0.124:9094"}
	Topic := "topic-test"
	User := "user-test"
	Password := "UjfjpkUJgo0J"
	ConsumeGroup := "group-test"

	mechanism, err := scram.Mechanism(scram.SHA512, User, Password)
	if err != nil {
		panic(err)
	}

	dialer := &kafka.Dialer{
		Timeout:       10 * time.Second,
		DualStack:     true,
		SASLMechanism: mechanism,
	}

	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers:  Urls,
		GroupID:  ConsumeGroup,
		Topic:    Topic,
		Dialer:   dialer,
		MaxBytes: 10e6, // 10MB
	})
	// r.SetOffset(0) // กำหนด offset ให้กับ consumer ที่จะอ่านข้อมูล 0 คือ จะอ่านข้อมูลทั้งหมด
	for {
		m, err := r.FetchMessage(context.Background())
		if err != nil {
			break
		}
		log.Printf("message at topic/partition/offset %v/%v/%v: %s = %s\n", m.Topic, m.Partition, m.Offset, string(m.Key), string(m.Value))
	}

	if err := r.Close(); err != nil {
		log.Fatal("failed to close reader:", err)
	}
	log.Printf("Connections close.")
}
