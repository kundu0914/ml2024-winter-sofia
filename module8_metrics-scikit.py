import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Ask user for input N
    N = int(input("Enter the number of points (N): "))

    # Initialize arrays to store ground truth (X) and predicted labels (Y)
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    # Read N (x, y) points from user input
    for i in range(N):
        x = int(input(f"Enter the x value for point {i + 1}: "))
        y = int(input(f"Enter the y value for point {i + 1}: "))
        X[i] = x
        Y[i] = y

    # Compute precision and recall
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    # Output precision and recall
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    main()
