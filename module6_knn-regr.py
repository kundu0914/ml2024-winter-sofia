import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.Y_train = None

    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train

    def predict(self, X_test):
        distances = np.sqrt(np.sum((self.X_train - X_test)**2, axis=1))
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_labels = self.Y_train[nearest_indices]
        return np.mean(nearest_labels)

def main():
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the value of k: "))
    
    if k > N:
        print("Error: k should be less than or equal to N.")
        return

    X_train = []
    Y_train = []

    for i in range(N):
        x = float(input(f"Enter x-coordinate of point {i+1}: "))
        y = float(input(f"Enter y-coordinate of point {i+1}: "))
        X_train.append(x)
        Y_train.append(y)

    X_train = np.array(X_train)
    Y_train = np.array(Y_train)

    knn = KNNRegression(k)
    knn.fit(X_train.reshape(-1, 1), Y_train)

    X_test = float(input("Enter the value of X to predict Y: "))
    Y_pred = knn.predict(np.array([X_test]).reshape(1, -1))

    print(f"The predicted Y value for X = {X_test} is: {Y_pred}")

if __name__ == "__main__":
    main()
