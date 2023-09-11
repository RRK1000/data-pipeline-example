package service

import (
	"encoding/json"
	"io"
	"net/http"
	"sync"
	"time"

	"github.com/RRK1000/data-pipeline-example/ingestion-layer/internal/kafka"
)

type Response struct {
	statusCode int
	data       map[string]interface{}
}

func Run() {
	var wg sync.WaitGroup
	responseChan := make(chan Response, 10) // change to response struct

	producer := kafka.InitProducer([]string{"localhost:9092"})

	for {
		wg.Add(1)
		go getUsers(&wg, responseChan)
		wg.Wait()

		response := <-responseChan
		b, _ := json.Marshal(response.data)
		kafka.Publish(producer, "payments", string(b))

		time.Sleep(time.Duration(5) * time.Second)
	}
}

func getUsers(wg *sync.WaitGroup, responseChan chan<- Response) {
	res, err := http.Get("https://random-data-api.com/api/v2/users")
	if err != nil {
		responseChan <- Response{
			statusCode: res.StatusCode,
			data:       nil,
		}
	}
	defer res.Body.Close()

	responseBody, err := io.ReadAll(res.Body)
	if err != nil {
		responseChan <- Response{
			statusCode: http.StatusInternalServerError,
			data:       nil,
		}
		return
	}

	var responseMap map[string]interface{}
	_ = json.Unmarshal(responseBody, &responseMap)
	if err != nil {
		responseChan <- Response{
			statusCode: http.StatusInternalServerError,
			data:       nil,
		}
		return
	}
	// log.Println("Here", responseMap)

	responseChan <- Response{
		statusCode: http.StatusAccepted,
		data:       responseMap,
	}
	defer wg.Done()
}
