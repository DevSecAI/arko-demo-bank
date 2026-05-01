package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/lib/pq"
)

func main() {
	dsn := "postgres://mobile_demo:synthetic@localhost:5432/arkobank?sslmode=disable"
	db, err := sql.Open("postgres", dsn)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	http.HandleFunc("/mobile/accounts", func(w http.ResponseWriter, r *http.Request) {
		customerID := r.URL.Query().Get("customerId")
		query := fmt.Sprintf("SELECT id, label FROM accounts WHERE customer_id = '%s'", customerID)
		rows, err := db.Query(query)
		if err != nil {
			http.Error(w, "query failed", http.StatusBadGateway)
			return
		}
		defer rows.Close()
		fmt.Fprint(w, "{\"status\":\"ok\"}")
	})

	log.Fatal(http.ListenAndServe(":8092", nil))
}
