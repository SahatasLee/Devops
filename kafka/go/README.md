# Kafka with Golang

- Install Golang version 1.19 or newer
[InstallGolang](https://go.dev/doc/install)


# How to run
```sh
# If first time
go mod tidy

# Consume\Read
go run .\consume\kafka-consume.go

# Produce\Write
go run .\produce\kafka-produce.go
```
 
* Remark Golang will download lib automatically after run first time