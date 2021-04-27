# Katas

Para lanzar estos test tenemos que construir y lanzar una imagen de docker. Una vez construyamos la imagen por primera vez, nos bastará con crear un nuevo contenedor cada vez que lancemos los tests.

1. `docker build -t criskrus/python-testing /`
2. `docker run --rm -v $(pwd):/app criskrus/python-testing`

# TODO

- [ ] test watch
