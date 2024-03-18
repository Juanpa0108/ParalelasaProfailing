<h1>Tarea Profiling y Avx</h1>
<hr>
<h2>Participantes</h2>
<h3>Nicole Narvaez Medina (2156947), Juan Pablo Robayo Maestre (2156743)</h3>
<hr>
<h4>Explicacion de los archivos</h4>

<ul>
  <li>El archivo "productoEscalar.c" es el que contiene la libreria en c, la cual se encarga de multiplicar un vector por un escalar.</li>
  <li>Despues de crear ese archivo se deben realizar estos comandos en Consola "rm -f libMultScalar.so, 
                                                                             gcc -fPIC -shared -o libMultScalar.so productoEscalar.c -mavx" para crear el enlace dinamico a la libreria</li>
  <li>El archivo "productoTimeit.py" es donde probamos la libreria creada en c y medimos el tiempo usando la libreria timeit.</li>
  <li>El archivo "productoProf.py" es donde probamos la libreria creada en c y medimos el tiempo usando la libreria cProfile.</li>
  <li>El archivo "programaBaseTimeit.py" es el que contiene el programa base donde se multiplica un vector por un escalar y no usa ninguna libreria que lo ayude en su proceso, en este se uso la libreia timeit para medir su tiempo</li>
  <li>El archivo "programaBasePro.py" es el que contiene el programa base explicado anteriormente, en este se uso la libreia cProfile para medir su tiempo</li>
  <li>El archivo "numpyProf.py" es donde realizamos la misma funcion que el programa base pero usando la libreria numpy, en este se uso la libreria cProfile para medir el tiempo.</li>
</ul>
 
