import numpy as np

def input_matrix():
    """Prompts the user to input a matrix."""
    print("Enter the matrix rows, one at a time. Separate elements with spaces.")
    print("Enter a blank line when you're done.")
    rows = []
    while True:
        row = input("Row: ")
        if row.strip() == "":
            break
        rows.append(list(map(float, row.split())))
    try:
        matrix = np.array(rows)
        print("\nMatrix Entered:\n", matrix)
        return matrix
    except ValueError:
        print("Invalid matrix format. Please try again.")
        return input_matrix()

def display_menu():
    """Displays the operations menu."""
    print("\nMatrix Operations Tool")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Calculate Determinant")
    print("6. Exit")

def add_matrices():
    """Adds two matrices."""
    print("\nMatrix Addition:")
    print("Matrix A:")
    A = input_matrix()
    print("Matrix B:")
    B = input_matrix()
    if A.shape == B.shape:
        print("\nResult:\n", A + B)
    else:
        print("Error: Matrices must have the same dimensions for addition.")

def subtract_matrices():
    """Subtracts two matrices."""
    print("\nMatrix Subtraction:")
    print("Matrix A:")
    A = input_matrix()
    print("Matrix B:")
    B = input_matrix()
    if A.shape == B.shape:
        print("\nResult:\n", A - B)
    else:
        print("Error: Matrices must have the same dimensions for subtraction.")

def multiply_matrices():
    """Multiplies two matrices."""
    print("\nMatrix Multiplication:")
    print("Matrix A:")
    A = input_matrix()
    print("Matrix B:")
    B = input_matrix()
    if A.shape[1] == B.shape[0]:
        print("\nResult:\n", np.dot(A, B))
    else:
        print("Error: Number of columns in A must equal number of rows in B for multiplication.")

def transpose_matrix():
    """Calculates the transpose of a matrix."""
    print("\nMatrix Transpose:")
    A = input_matrix()
    print("\nTranspose:\n", np.transpose(A))

def calculate_determinant():
    """Calculates the determinant of a square matrix."""
    print("\nMatrix Determinant:")
    A = input_matrix()
    if A.shape[0] == A.shape[1]:
        print("\nDeterminant:", np.linalg.det(A))
    else:
        print("Error: Determinant is only defined for square matrices.")

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Select an option (1-6): ")
        if choice == "1":
            add_matrices()
        elif choice == "2":
            subtract_matrices()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            calculate_determinant()
        elif choice == "6":
            print("Exiting the Matrix Operations Tool. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
