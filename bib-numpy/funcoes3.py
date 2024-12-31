import numpy as np
arr_3d = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

print(arr_3d)
print('Numeros de dimensões: ', arr_3d.ndim)
print('--' * 20)
print('Shape da listas: ', arr_3d.shape)
print('--' * 20)
print('Buscar o elemento da indice da dimensão 0 da linha 2 e coluna 1: ', arr_3d[0, 2, 1])

arr_4d = np.array([
    [    
        [
            [1 ,2 ,3 ,4 ,5],
            [6 ,7 ,8 ,9 ,10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40]
        ],
        [
            [41, 42, 43, 44, 45],
            [46, 47, 48, 49, 50],
            [51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60]
        ]
    ],
    [
        [
            [61, 62, 63, 64, 65],
            [66, 67, 68, 69, 70],
            [71, 72, 73, 74, 75],
            [76, 77, 78, 79, 80]
        ],
        [
            [81, 82, 83, 84, 85],
            [86, 87, 88, 89, 90],
            [91, 92, 93, 94, 95],
            [96, 97, 98, 99, 100]
        ],
        [
            [101, 102, 103, 104, 105],
            [106, 107, 108, 109, 110],
            [111, 112, 113, 114, 115],
            [116, 117, 118, 119, 120]
        ]
    ]
])

print(arr_4d)
print('Numeros de dimensões: ', arr_4d.ndim)
print('O Shape de arr_4d é: ', arr_4d.shape)
print('Buscar o grupo 0, o subgrupo 2, Linha 1: ', arr_4d[0, 2, 1])
print('Buscar o grupo 0, o subgrupo 2, Linha 1, coluna 4: ', arr_4d[0, 2, 1, 4])
