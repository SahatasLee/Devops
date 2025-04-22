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
	Urls := []string{"10.7.36.202:9094"}
	Topic := "da-oth1-budget-incentive"
	User := "eaadmin"
	Password := "qiRAPiBZWJlB"
	// ConsumeGroup := "eaadmin-group"

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
		Brokers: Urls,
		// GroupID:   ConsumeGroup,
		Partition: 0,
		Topic:     Topic,
		Dialer:    dialer,
		MaxBytes:  10e6, // 10MB
	})
	r.SetOffset(0) // กำหนด offset ให้กับ consumer ที่จะอ่านข้อมูล 0 คือ จะอ่านข้อมูลทั้งหมด

	i := 0

	for {
		m, err := r.FetchMessage(context.Background())
		// m, err := r.ReadMessage(context.Background())
		if err != nil {
			break
		}
		log.Printf("message at topic/partition/offset %v/%v/%v: %s = %s\n", m.Topic, m.Partition, m.Offset, string(m.Key), string(m.Value))

		if i == 0 {
			break
		}

		i++
	}

	if err := r.Close(); err != nil {
		log.Fatal("failed to close reader:", err)
	}
	log.Printf("Connections close.")
}
