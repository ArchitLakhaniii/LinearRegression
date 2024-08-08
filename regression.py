import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
  n = np.size(x)

  m_x = np.mean(x)
  m_y = np.mean(y)

  SS_xy = np.sum(y*x) - n*m_y*m_x
  SS_xx = np.sum(x*x) - n*m_x*m_x

  b_1 = SS_xy / SS_xx
  b_0 = m_y - b_1*m_x

  return (b_0, b_1)
def plot_regression_line(x, y, b):
  plt.scatter(x, y, color = "m",
        marker = "o", s = 30)
  y_pred = b[0] + b[1]*x
  plt.plot(x, y_pred, color = "g")
  plt.xlabel('x')
  plt.ylabel('y')

def main():
    x = np.array([1.1, 1.3, 1.5, 2, 2.2, 2.9, 3, 3.2, 3.2, 3.7, 3.9, 4, 4.5, 4.9, 5.1])
    y = np.array([39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189, 63218, 55794, 56957, 57081, 61111])
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {} \
        \nb_1 = {}".format(b[0], b [1]))
    plot_regression_line(x, y, b)
    
if __name__ == "__main__":
  main()
