# FASTAPI Proxy Server

This app serves as a http proxy server and passes on the JWT token as a upstream server.

## Requirements
Following are the requirements for running this app
- Docker
- Docker Compose

## Steps to Run the app

```
make build
make run
```

### Step to run with a single command
```
make all
```

## APIs available

- [Swagger API](http://127.0.0.1:8000/docs)
- [User API](http://127.0.0.1:8000/user)
- [Default Page](http://127.0.0.1:8000/)
- [App Status](http://127.0.0.1:8000/status)

