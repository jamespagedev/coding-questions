def maxtrix_transpose(matrix):
  # create transpose array switching height and width of matrix
  transpose_matrix = []
  transpose_matrix_row = [None] * len(matrix)
  for i in range(len(matrix[0])):
    transpose_matrix.append(transpose_matrix_row[:])

  # swap values for matrix/transpose using indexes
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      transpose_matrix[j][i] = matrix[i][j]

  return transpose_matrix

if __name__ == '__main__':
  matrix = [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ]
  print(maxtrix_transpose(matrix))

