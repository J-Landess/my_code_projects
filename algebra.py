
'''This is an example of how you can take any mxn or nxm matrix
 and using AtA or AAt you can get a symmetric square matrix either
 mxm or nxn. the diagonals of E will be the singular values which is 
 represented as Epsilon in UEV '''


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Define matrix A
A = np.random.rand(3,2)
At = np.transpose(A)

# Compute AtA and AAt
V = At @ A  # A^T A
U = A @ At  # A A^T

# Print AtA and AAt
print(f"\nCompute A.t * A and you get this matrice: \n{V}")
print(f"\nCompute A * A.t and you get this matrice: \n{U}")

# Sum of eigenvalues (example)
# e = 109.3 + 37  # Eigenvalues for AAt
# f = 16.21 + 130.09  # Eigenvalues for AtA

# print(f"AtA summed eigenvalues: {e}")
# print(f"AAt summed eigenvalues: {f}")

# Perform SVD
U, Sigma, Vt = np.linalg.svd(A)

# Print the SVD results
print("U matrix (left singular vectors):")
print(U)

print("\nSigma (singular values):")
print(Sigma)

print("\nVt matrix (right singular vectors):")
print(Vt)

# Plot the singular values
print("Plot the sigmas (singular values)")
plt.plot(Sigma, marker='o')
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.title("Singular Values of A")
plt.grid()
plt.show()

# Heatmap of U
print("Heatmap of U:")
plt.figure(figsize=(6, 4))
sns.heatmap(U, cmap="coolwarm", annot=True)
plt.title("Left Singular Vectors (U)")
plt.show()

# Heatmap of Vt
print("Heatmap of V^T:")
plt.figure(figsize=(6, 4))
sns.heatmap(Vt, cmap="coolwarm", annot=True)
plt.title("Right Singular Vectors (V^T)")
plt.show()

# Scatter plot of U and V vectors
if U.shape[1] >= 2 and Vt.shape[1] >= 2:
    plt.scatter(U[:, 0], U[:, 1], color='blue', label="U vectors")
    plt.scatter(Vt[:, 0], Vt[:, 1], color='red', label="V^T vectors")
    plt.xlabel("First Component")
    plt.ylabel("Second Component")
    plt.legend()
    plt.title("Singular Vectors U and V")
    plt.show()
else:
    print("U and V don't have enough components for a 2D scatter plot.")
print(f"Sigma: {Sigma}")
print(f"Sigma squared: {Sigma**2}")
cov_matrix = np.cov(A,rowvar=False)
print(f"This is the covariance matrix used to do PCA: \n{cov_matrix}")
plt.figure(figsize=(8, 5))
plt.bar(range(1, len(Sigma) + 1), Sigma, color='royalblue')
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.title("Singular Values of Matrix A")
plt.grid(True)
plt.show()




# Step 1: Center the data (subtract the mean of each feature)
data_centered = A - np.mean(A, axis=0)

# Step 2: Compute the covariance matrix
cov_matrix = np.cov(data_centered, rowvar=False)

# Step 3: Perform eigen decomposition (eigenvalues and eigenvectors)
eigvals, eigvecs = np.linalg.eigh(cov_matrix)

# Step 4: Sort eigenvalues in descending order and reorder eigenvectors accordingly
sorted_indices = np.argsort(eigvals)[::-1]
eigvals_sorted = eigvals[sorted_indices]
eigvecs_sorted = eigvecs[:, sorted_indices]

# Step 5: Project the data onto the first two principal components
# (choosing the top 2 eigenvectors)
projected_data = np.dot(data_centered, eigvecs_sorted[:, :2])

# Output
print("Covariance Matrix:")
print(cov_matrix)

print("\nEigenvalues (Variance captured by each component):")
print(eigvals_sorted)

print("\nEigenvectors (Principal components):")
print(eigvecs_sorted)

print("\nProjected Data (PCA representation):")
print(projected_data)