# RealWorldOne

## Running the code

### Django

Install the requirements from pip

```bash
pip install -r requirements.txt
```

Run django's development server (starts on localhost:8000):

```bash
python manage.py runserver


### RabbitMQ

use RabbitMQ to bridge the django application and the uWSGI WebSocket server. The installation process varies.

### WebSocket server

use `uWSGI` as it's websocket server, if you've already installed the requirements from `requirements.txt` if should already be installed.

You can start it with

```bash
uwsgi --http :8081 --gevent 100 --module websocket --gevent-monkey-patch --master
```


### Vue

Navigate to the `frontend directory`:

```bash
cd frontend
```

Install the dependencies from npm:

``` bash
npm install
```

Run the webpack dev server (starts on localhost:8080):

```bash
npm run dev
```

