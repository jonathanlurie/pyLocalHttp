# pyLocalHttp

Creates a local HTTP server on the current directory, accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  

## How to launch?

pyLocalHttp has no dependency except Python itself, to launch in a terminal, just type:

```
cd /place/where/to/create/aServer/
python /place/where/pyLocalHttp/is/pyLocalHttp.py
```

Note that it's really easier to create an alias to it in your *.bashrc*:

```
alias serveHere='python /place/where/pyLocalHttp/is/pyLocalHttp.py'
```

The server will run **for ever**, sot to stop it your have to use a *ctrl+c* interruption, or just to kill your terminal...

## What else?

You can specify the port, like that:

```
cd /place/where/to/create/aServer/
python /place/where/pyLocalHttp/is/pyLocalHttp.py 8123
```

## Compatibilities

Supposed to be cross-platform.