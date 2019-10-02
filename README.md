## Run the test
```bash
docker run -it --rm --name test -v "$PWD":/usr/src/app -w /usr/src/app python:3 python test.py
```