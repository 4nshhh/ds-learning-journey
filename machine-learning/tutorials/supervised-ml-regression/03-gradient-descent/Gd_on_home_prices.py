import numpy as np
import pandas as pd

def gradient_descent(x,y, lr = 0.01, epochs = 3000):
    m = 0.0
    b = 0.0

    # Now both x and y are in different scale(Thousand & Hundreds).
    # So we need to bring them in same scale
    # Using (current - min)/(max - min)

    # Let's first find min and max of x&y
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()

    # Now let's do min-max scaling
    x_scaled = (x-x_min)/(x_max-x_min)
    y_scaled = (y-y_min)/(y_max-y_min)

    for epoch in range(epochs):
        y_predicted = m*x_scaled + b
        error = y_scaled - y_predicted
        cost = np.mean(error**2)

        dm = -2*np.mean(x_scaled*error)
        db = -2*np.mean(error)

        m -= dm*lr
        b -= db*lr

        if epoch%100 == 0:
            print(f"m : {m}, b : {b}, cost : {cost}, Epoch : {epoch}")

    # Scale back to original values
    m_original = m * (y_max - y_min) / (x_max - x_min)
    b_original = y_min + (y_max - y_min) * b - m_original * x_min

    return b_original,m_original

if __name__ == "__main__":
    df = pd.read_csv("home_prices.csv")

    x = df["area_sqr_ft"].to_numpy()
    y = df["price_lakhs"].to_numpy()


    b,m = gradient_descent(x,y)
    print(f"Final Results: m = {m}, b = {b}")