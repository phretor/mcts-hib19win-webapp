# Mini Capture the Signal (mCTS) per HackInBo 2019 - Winter

Questo repository contiene l'applicazione web per riprodurre gestire un mCTS
esattamente come quello di [HackInBo](https://hackinbo.it) 2019 - Winter.

Oltre a questo vi servirà un nodo radio da nascondere da qualche parte. Per il
firmware e le istruzioni potete basarvi su [quest'altro
repository](https://github.com/mcts-hib19win/mcts-hib19win-radio).

# Utilizzo

Servono Docker e Docker Compose, dopodiché vi basterà:

```bash
$ cp env-example .env   # copiare le variabili d'ambiente predefinite
$ $EDITOR .env          # modificare le variabili d'ambiente
$ docker-compose up -d  # far partire l'applicazione web
```

A questo punto puntate il vostro browser su
[http://localhost:8080](http://localhost:8080) e iniziate a giocare!
