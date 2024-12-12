import numpy as np

# A method that retrieves 3 matrices, taking the input from the user
def get_input(equations, variables):
    final_variables = np.array(np.zeros((variables, 1)))
    final_results = np.array(np.zeros((equations,1)))
    final_numbers = np.array(np.zeros((variables,equations)))
    for i in range(0,equations):
        final_results[i,0] = float(input(f"Enter result for equation {i+1}: "))
        for x in range(0, variables):
            final_numbers[i,x] = float(input(f"Enter number for equation {i+1} variable {x+1}: "))
    return final_variables, final_results, final_numbers
            

def gauss_jordan(equations, variables):
    final_variables, final_results, final_numbers = get_input(equations, variables)
    
    # Declaring n, and m to shorten our code, Didn't utilize it well, unfortunately
    n = len(final_results)
    m = n - 1
    final_concate = np.concatenate((final_numbers, final_results), axis=1, dtype = float)

    # Forward elimination, to eliminate all numbers below the first row
    for i in range(len(final_results-1)):
            for j in range(i+1, len(final_results)):
                if final_concate[i,i] != 0:
                    final_concate[j,:] = final_concate[j,:] - (final_concate[j,i] / final_concate[i,i]) * final_concate[i,:]

    # Finding the last variable
    final_variables[m] = final_concate[m][n] / final_concate[m][m]

    # Backward substitution, to find the rest of the variables using the last variable
    for k in range(n - 2, -1, -1):
        final_variables[k] = final_concate[k][n]
        for l in range(k + 1, n):
            final_variables[k] = final_variables[k] - final_concate[k][l] * final_variables[l]
        final_variables[k] = final_variables[k] / final_concate[k][k]
        
    print("Final result",final_variables)

    return final_variables
    
def cramer_rule(equations, variables):
    final_variables, final_results, final_numbers = get_input(equations, variables)

    # Determinant of the main matrix
    a_det = np.linalg.det(final_numbers)

    # Substitution of the final results in the main matrix
    n = len(final_results)
    for i in range(0, n):
        tempMatrix = np.copy(final_numbers)
        for j in range(0, n):
            tempMatrix[j][i] = final_results[j]
            final_variables[i] = np.linalg.det(tempMatrix) / a_det # Determinant of the substituted matrix / determinant of the main matrix to find the result for the variable

    print("Final result",final_variables)
        
    return final_variables


def main():
    option = int(input("Enter 1.Gauss-Jordan 2.Cramer's Rule: "))
    
    equations = int(input("Enter number of equations: "))
    variables = int(input("Enter number of variables: "))
    if equations != variables:
        print("Invalid input, equations must best equal to variables")
        return
    
    if option == 1:
        gauss_jordan(equations, variables)
    elif option == 2:
        cramer_rule(equations, variables)
    else:
        print("Invalid option")
    
    
main()