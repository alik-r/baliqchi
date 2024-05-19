# Baliqchi
## Usage
To run the project, first create a virtual environment and install the requirements by running:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then, run:

```sh
$ docker compose up --build
```

Lastly, run:

```sh
$ ./run.sh
```

> You will need API key for Twilio to send real SMS messages.
See `.env.example`.

