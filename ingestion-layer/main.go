package main

import (
	"log"

	"github.com/RRK1000/data-pipeline-example/ingestion-layer/internal/service"
)

func main() {
	log.Println("ingestion service started")
	service.Run()
}
