import numpy as np

class multply_matrix():
    '''
      Creator: Thyall D'greville
      Data: Abril 2023

      A classe para representar a multiplicação de duas raízes quadradas

      Atributos:
      shape: int
          o tamanho das matriz. Ex: passando 5 a matriz será 5x5
      
      matrix_a: array
          objeto array do numpy para representar a matriz A

      matrix_b: array
          objeto array do numpy para representar a matriz B

      Methods:
      multyply():
          multiplica as duas matrizes e retorna o resultado
      
      print_matrix:
          imprime o valor das duas matrizes e seu resultado
    '''

    def __init__(self, shape):
        self.shape = shape
        # criando matriz com números aleatórios
        self.matrix_a = np.random.randint(1, 100, size=(shape, shape))
        self.matrix_b = np.random.randint(1, 100, size=(shape, shape))

    def multyply(self):
        '''
          multiplica as duas matrizes 

          Returns:
              retorna o produto da multiplicação
        '''
        return np.matmul(self.matrix_a, self.matrix_b)

    def print_matrix(self):
        '''
          multiplica as duas matrizes 
        '''
        print("A: \n", self.matrix_a, "\n")
        print("B: \n", self.matrix_b, "\n")
        print("Result: \n", self.multyply())


if __name__ == "__main__":
    matrix = multply_matrix(4)

    matrix.print_matrix()