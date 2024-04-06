package kafka

import (
	"log"

	"github.com/IBM/sarama"
)

func InitProducer(brokerList []string) sarama.SyncProducer {
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForAll // Wait for all in-sync replicas to ack the message
	config.Producer.Retry.Max = 10                   // Retry up to 10 times to produce the message
	config.Producer.Return.Successes = true
	producer, err := sarama.NewSyncProducer(brokerList, config)
	if err != nil {
		log.Fatalln("make sure that Kafka is accessible and running. err: ", err)
	}
	return producer
}

func Publish(producer sarama.SyncProducer, topic, value string) {
	msg := &sarama.ProducerMessage{
		Topic: topic,
		Value: sarama.ByteEncoder(value),
	}

	_, _, err := producer.SendMessage(msg)
	if err != nil {
		log.Fatal(err)
	}
}
