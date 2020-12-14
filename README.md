# Take-a-Number-Backend
## Setup
```
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
### DB
Install redis in a directory called `db`
```
db/src/redis-server
```

### Starting the server
```
source env/bin/activate
python take_a_number.py
```

## Testing
```
pytest
```

