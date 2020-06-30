# ScrabbleAR-Grupo29
Integrantes :
  Delmas Leonardo, Legajo: 15993/3
  Silva Marco, Legajo: 16234/2
  Batisti Matias, Legajo: 15083/0

El programa:

  El programa principal es ScrabbleAR.py su ejecución requiere todos los archivos en la misma carpeta.
  Si el jugador no configura en opciones el usuario se ejecuatará la partida con un usuario 'Default'.
  El Tablero permite colocar una ficha seleccionando una en el atril y luego cliqueando la casilla deseada, en caso de ser el usuario quien comience la partida deberá colocar la primera ficha en el cuadrado negro del centro.
  Las puntuaciones pueden visualizarse en el talero pero no se guardarán en la tabla de posiciones.


Consideraciones:

  El boton intercambiar fichas no funciona adecuadamente, esta disponible para su prueba pero pueden surgir errores.
  La AiMaquina solo forma palabras de izquierda a derecha y de arriba a  abajo.
  El reloj no funciona dado que generaba errores con los windows.read y se implementará una correción para la próxima entrega, posiblemente con hilos.
  Puede que durante la ejecución de la partida se bloquea la posibilidad de colocar una ficha en una posición que ya había sido ocupada en un determinado momento; deberá terminar el turno para poder volver a utilizar esa posición.
