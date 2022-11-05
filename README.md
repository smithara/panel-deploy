# Simple image to deploy panel

To Build the image:
```
podman build . -t mypanel
```

To serve the test dashboard with panel:
```
podman run --rm -it \
-p 5006:5006 -v ./src:/home/panel-user/src \
mypanel panel serve src/test-dashboard.py \
--allow-websocket-origin=* --warm
```

To serve other dashboards (.py or .ipynb), put the files in `src/` and refer to them as above in `panel serve`.

To update `environment-exact.txt`:

```
mamba env create --name panel environment.yml
mamba list --name panel --explicit > environment-exact.txt
```

To create exact environment:
```
mamba create --name panel --file environment-exact.txt
```
