# Biker

## Setup for development
* Clone the repository
* Initialize your database
```bash
python3 -m flask --app src init-db
  ```
* Run application
```bash
python3 -m flask --app src --debug run
```

### Linting your code
This project makes use of Black for linting code. You can run the following command to lint the `src` & `tests` directories:
```bash
black src && black tests
```
