import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def kNN_regression(X_train, y_train, k, X_test):
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return y_pred

def main():
    # Input N and k
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k (k <= N): "))

    # Input points (x, y)
    points = []
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        points.append([x, y])

    # Convert points to numpy array
    points = np.array(points)

    # Input X for prediction
    X_test = np.array([[float(input("Enter X value for prediction: "))]])

    if k <= N:
        # Splitting data into X and y
        X_train = points[:, 0].reshape(-1, 1)  # Reshape to make it 2D array
        y_train = points[:, 1]

        # Perform k-NN Regression
        y_pred = kNN_regression(X_train, y_train, k, X_test)

        # Output the result (Y) of k-NN Regression
        print("Result (Y) of k-NN Regression:", y_pred[0])

        # Calculate coefficient of determination (R^2 score)
        y_pred_train = kNN_regression(X_train, y_train, k, X_train)
        r2 = r2_score(y_train, y_pred_train)
        print("Coefficient of determination (R^2 score):", r2)
    else:
        print("Error: k should be less than or equal to N.")

if __name__ == "__main__":
    main()
