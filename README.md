# Cálculo de Determinante da Matriz
Este código Python calcula o determinante de uma matriz quadrada usando o método de expansão de Laplace.
Arquivos de entrega do trabalho: *determinant.py* e *determinant.tex*

## Como usar?

Para usar este código, você pode importar a função `calculate_determinant` deste módulo e passar uma matriz quadrada como argumento. Por exemplo:

```python
from determinant import calculate_determinant

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

determinant = calculate_determinant(matrix)

print(f"The determinant of the matrix is {determinant}")
```

This will output:

```
The determinant of the matrix is 0
```

## Requirements

Este código requer Python 3.6 ou superior para ser executado. Ele também requer os módulos `functools` e `itertools`, que estão incluídos na biblioteca padrão. Para rodar os testes o `pytest` é necessária a instalação.

## 1. Para instalar 
make install

## 2. Para rodar os testes
make test

## 3. Executar o programa com as amostras de exemplo:
make run

### Saída:

```python

Determinante da matriz A [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]] = 0
Determinante da matriz B [[3, 1, 0, 0], [0, 1, 0, 0], [0, 1, 2, 1], [0, 0, 0, 1]] = 6
```
## License

This code is released under the [MIT License](LICENSE). Feel free to use it in your own projects.
