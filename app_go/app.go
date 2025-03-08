package main

import (
	"encoding/json"
	"html/template"
	"log"
	"net/http"
	"time"
	"os"
	"strconv"
)

// API response structure
type TimeAPIResponse struct {
	DateTime string `json:"dateTime"`
}

// path to the visits file
var visitsFile = "/data/visits.txt"

// function to increment the visit counter
func incrementVisits() int {
	// read the current visit count
	visits := 0
	if _, err := os.Stat(visitsFile); err == nil {
		data, err := os.ReadFile(visitsFile)
		if err == nil {
			visits, _ = strconv.Atoi(string(data))
		}
	}

	// increase
	visits++

	// save and update
	err := os.WriteFile(visitsFile, []byte(strconv.Itoa(visits)), 0644)
	if err != nil {
		log.Println("error occured while saving visits:", err)
	}

	return visits
}


// handler for the homepage
func homeHandler(w http.ResponseWriter, r *http.Request) {

	// increase the
	incrementVisits()

	// API URL
	timeAPIURL := "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Moscow"

	// HTTP client with timeout (5 seconds)
	client := http.Client{Timeout: 5 * time.Second}
	resp, err := client.Get(timeAPIURL)
	if err != nil {
		http.Error(w, "failed to fetch time: " + err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	// parse JSON response
	var timeData TimeAPIResponse
	if err := json.NewDecoder(resp.Body).Decode(&timeData); err != nil {
		http.Error(w, "failed to parse time response", http.StatusInternalServerError)
		return
	}

	// format the time string
	formattedTime := timeData.DateTime
	if len(formattedTime) > 0 {
		formattedTime = formattedTime[:19] // keep only YYYY-MM-DD HH:MM:SS
	}

	// render the template and execute it with the formatted time
	tmpl, err := template.ParseFiles("index.html")
	if err != nil {
		http.Error(w, "error loading template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, map[string]string{"Time": formattedTime})
}

// handler for the visits counter
func visitsHandler(w http.ResponseWriter, r *http.Request) {
	// read the visit count from the file
	visits := 0
	if _, err := os.Stat(visitsFile); err == nil {
		data, err := os.ReadFile(visitsFile)
		if err == nil {
			visits, _ = strconv.Atoi(string(data))
		}
	}

	// return the visit count as a response
	w.Write([]byte("Total visits: " + strconv.Itoa(visits)))
}

func main() {

	// initialize the visits file if it doesn't exist
	if _, err := os.Stat(visitsFile); os.IsNotExist(err) {
		os.WriteFile(visitsFile, []byte("0"), 0644)
	}

	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/visits", visitsHandler)

	log.Println("Server started on :8000")
	log.Fatal(http.ListenAndServe(":8000", nil))
}
