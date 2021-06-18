Aquí podrás ver las diferentes soluciones que le he dado a las katas que he hecho.
Algunas de estas tienen una solución en vídeo asociada por si quieres ver el proceso
que he seguido para solucionarla.

## Lanzar los test 

Para lanzar estos test tenemos que entrar en la kata en cuestión, construir y lanzar una imagen de docker. Una vez construyamos la imagen por primera vez, nos bastará con crear un nuevo contenedor cada vez que lancemos los tests.

1. `docker build -t criskrus/python-test /`
2. `docker run --rm -v $(pwd):/app criskrus/python-test`

Estos mismos pasos están en un script dentro de las katas el cual podemos ejecutar
con `sh run_test.sh`

## Listado de katas

- [Range parser](2021-05-07-range-parser)
- [First non repeating character](2021-05-14-first-non-repeating-character)
- [Potter](2021-05-28-potter-kata)
- [Which are in](2021-06-18-which-are-in)
