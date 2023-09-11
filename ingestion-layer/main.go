package main

import (
	"github.com/RRK1000/data-pipeline-example/ingestion-layer/internal/service"
)

func main() {
	// flag.StringVar(&brokers, "brokers", "", "Kafka bootstrap brokers to connect to, as a comma separated list")
	// flag.StringVar(&group, "group", "", "Kafka consumer group definition")
	// flag.StringVar(&topics, "topic", "", "Kafka topic to be pushed to")
	// flag.parse()
	service.Run()
}