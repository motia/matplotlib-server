# MatplotLib Server
A small service that serves Matplotlib charts over http


# Endpoints
```
curl localhost:8000/bar/plot.png?x=1,2,3\&y=9,8,7\&x_ticks=1,2,3\&x_labels=Q1,Q2,Q3\&y_ticks=0,5,10\&y_labels=0,5k,10k
```

```
curl localhost:8000/plot/plot.png?x=1,2,3\&y=9,8,7\&x_ticks=1,2,3\&x_labels=Q1,Q2,Q3\&y_ticks=0,5,10\&y_labels=0,5k,10k
```
