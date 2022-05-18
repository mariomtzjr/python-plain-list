# Tech Challenge

Escribe un código en ***Python*** que aplane un arreglo de enteros o arreglos de enteros (que puede estar anidado arbitrariamente) a un arreglo plano de enteros.  

Por ej. para el arreglo:
```
[1, [2, [3, [4, 5]]]]
```  
Tu código debe devolver:  
```
[1, 2, 3, 4, 5]
```

### Requirements
- Python3.9

### Files
Contamos con dos archivos, ***main.py*** y ***tests.py***, el primero contiene el método (***get_plain_list***) que genera un arreglo plano a partir de un arreglo aninado. El segundo, realiza un set de pruebas (3) que valida la salida correcta de un arreglo aplanado.  

#### main.py
Para ejecutar el archivo principal (__main.py__), es necesario estar en el mismo nivel del archivo, bajo una consola o terminal.  
Ejecutar el comando:  
`python3 main.py`  
Obtendremos la siguiente salida:  
```
Arreglo original:  [1, [2, [3, [4, 5]]]]
Arreglo plano:  [1, 2, 3, 4, 5]
```

#### tests.py
Para ejecutar el archivo de pruebas (__tests.py__), es necesario estar en el mismo nivel del archivo, bajo la misma consola o terminal.  
Ejecutar el comando:  
`python3 tests.py` o `python3 tests.py -v`  
Obtendremos la siguiente salida:  
```
test_plain_list_1 (__main__.TestPlainIntegerList) ... ok
test_plain_list_2 (__main__.TestPlainIntegerList) ... ok
test_plain_list_3 (__main__.TestPlainIntegerList) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```  

La salida anterior indica que las tres pruebas fueron exitosas, de acuerdo a las entradas que fueron proporcionadas, las cuales, son las siguientes:

- `nested_list1 = [1, [2, [3, [4, 5]]]]`
- `nested_list2 = [1, [2, [3, 4, [5, 6], 7]], 8, [9, 10]]`
- `nested_list3 = [1, [2, "a", ["b", 3, 4]]]`