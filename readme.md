# Numeros Complejos

Una libreria capaz de realizar las operaciones basicas entre numeros complejos (suma, resta, producto, divison) y otras mas que pueden ser de mucha ayuda en la computacion cuantica

## Como Empezar

Para poder usarla solo en necesario descargar el archivo de la libreria (NumComplexLib.py) y importarlo dentro del programa

### Prerequisitos

- Phyton
- Editor de codigo

```
Visual Studio Code, PyCharm, etc
```

### Instalando

1. Abrir el repositorio de github 
2. Descargar el archivo NumComplexLib.py y guardarlo en la misma carpeta donde tenga su programa
3. Despues dentro del programa importar la libreria 
4. Llamar las funciones que requiera y digitar como argumentos el o los numeros complejos a operar

```
import NumComplexLib
```

Y llamar la funcion

```
print(NumComplexLib.SumaComplejos([5,2],[4,7]))
```

Los numeros complejos poseen dos partes (real y imaginaria), por lo tanto deben argumentarlas dentro de un vector ambas partes para que se ejecute correctamente la funcion

## Ejecutando las funciones

La Libreria contiene en total 9 funciones (suma, resta, producto, division, modulo, conjugado, fase, representacion polar, representacion cartesiana)

### Nombres de las funciones

Todas empiezan por la primera letra de cada palabra en mayuscula

```
SumaComplejos, ProductoComplejos, RestaComplejos, DivisionComplejos, ModuloComplejos, ConjugadoComplejos, FaseComplejos, RepresentacionPolar, RepresentacionCartesiana
```

### Argumentos

Para las operaciones basicas es necesario que sean dos argumentos, es decir dos numeros complejos para realizarse, sin embargo para las demas solo se requiere un numero complejo debido a que son conversiones o operaciones que solo aplican a un numero complejo

```
SumaComplejos(n1,n2), ProductoComplejos(n1,n2), ModuloComplejos(n1), FaseComplejos(n1)
```

## Adicionales

Para digitar la parte imaginaria no es necesario poner el simbolo caracteristico de esta (i), solo el digito

## Construido con

* [Phyton](https://www.python.org/) - Lenguaje de programacion
* [Pycharm](https://www.jetbrains.com/es-es/pycharm/) - IDE de python

## Contribuyendo

Estaremos abiertos a cualquier tipo de sugerencia o reclamo sobre el uso de la libreria, para asi ir mejorando cada vez mas

## Versionado

Nosotros usamos [github](https://github.com/AndresSu2342/NumComplexLib) para el versionado de la libreria. Solo estara disponible la version mas reciente

## Autores

* **Cesar Borray** - *Estudiante* - [Escuela Colombiana de Ingenieria](https://www.escuelaing.edu.co/es/)

## Licencia

Esta libreria es de uso gratuito, aunque todos los derechos de copyright son reservados

## Expresiones de gratitud

* Libreria apoyada por Luis Daniel Benavides Navarro (Profesor)
