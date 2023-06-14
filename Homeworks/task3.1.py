class Matrix:

    def __init__(self, line: int, col: int, vol: int):
        #line -строки, col - колонки, vol - значения матрицы

        if col >=1:
            self.col = col
            self.line = line
            self.vol = vol
            self.matrica = []
            for i in range(line):
                self.matrica.append([vol] * col)
            print(*self.matrica, sep = "\n")
            print('End')
        else:
            print("Введите число колонок от 1 до n...")

    def add(self, line: int, col: int, vol: int):
        # line -строки, col - колонки, vol - значения матрицы

        if col >= 1:
            self.col = self.col + col
            self.line = self.line + line
            self.vol = vol
            self.matrica = []
            for i in range(self.line):
                self.matrica.append([vol] * int(self.col))
            print(*self.matrica, sep = "\n")
            print('End')
        else:
            print("Введите число колонок от 1 до n...")


    def change_vol(self, line: int, col: int, new_vol: int):
    # line -строки, col - колонки, new_vol - новое значение матрицы

        self.col = col
        self.line = line
        self.new_vol = new_vol
        self.matrica[line-1][col-1] = new_vol
        print(*self.matrica, sep = "\n")
        print('End')

    def razmer(self):
        print(f'Размер матрицы: {len(self.matrica)} строк(и) и {len(self.matrica[0])} столбца')






k = Matrix(6, 3, 7)
k.add(1, 2, 7)
k.change_vol(2, 3, 47)
k.razmer()



















