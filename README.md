# Katas

Repositorio donde dejar guardadas las katas.

## Lanzar los test 

Para lanzar estos test tenemos que entrar en la kata en cuestión, construir y lanzar una imagen de docker. Una vez construyamos la imagen por primera vez, nos bastará con crear un nuevo contenedor cada vez que lancemos los tests.

1. `docker build -t criskrus/python-test /`
2. `docker run --rm -v $(pwd):/app criskrus/python-test`

# TODO
- [ ] test watch
