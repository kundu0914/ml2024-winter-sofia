import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Function to read pairs from user input
def read_pairs(num_pairs):
    pairs = []
    for _ in range(num_pairs):
        x = float(input("Enter x value: "))
        y = int(input("Enter y value: "))
        pairs.append((x, y))
    return pairs

# Function to prepare data for training and testing
def prepare_data(train_pairs, test_pairs):
    train_X, train_y = zip(*train_pairs)
    test_X, test_y = zip(*test_pairs)
    return np.array(train_X).reshape(-1, 1), np.array(train_y), np.array(test_X).reshape(-1, 1), np.array(test_y)

# Function to perform kNN classification and find best k
def knn_classification(train_X, train_y, test_X, test_y):
    best_accuracy = 0
    best_k = 0
    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train_X, train_y)
        predictions = knn.predict(test_X)
        accuracy = accuracy_score(test_y, predictions)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    return best_k, best_accuracy

# Main function
def main():
    # Read number of pairs for training set
    N = int(input("Enter the number of pairs for training set (N): "))
    train_pairs = read_pairs(N)

    # Read number of pairs for test set
    M = int(input("Enter the number of pairs for test set (M): "))
    test_pairs = read_pairs(M)

    # Prepare data
    train_X, train_y, test_X, test_y = prepare_data(train_pairs, test_pairs)

    # Perform kNN classification
    best_k, best_accuracy = knn_classification(train_X, train_y, test_X, test_y)

    # Output results
    print(f"The best k for kNN classification is {best_k} with a test accuracy of {best_accuracy:.2f}")

if __name__ == "__main__":
    main()
