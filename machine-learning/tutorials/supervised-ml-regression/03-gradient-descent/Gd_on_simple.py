import numpy as np

def gradient_descent(x,y, lr = 0.01, epochs = 3000):
    m = 0.0
    b = 0.0
    for epoch in range(epochs):
        y_predicted = m*x + b
        error = y - y_predicted
        cost = np.mean(error**2)

        dm = -2*np.mean(x*error)
        db = -2*np.mean(error)

        m -= dm*lr
        b -= db*lr

        print(f"m : {m}, b : {b}, cost : {cost}, Epoch : {epoch}")

if __name__ == "__main__":
    x = np.array([1,2,3,4,5])
    y = np.array([5,7,9,11,13])
    gradient_descent(x,y)