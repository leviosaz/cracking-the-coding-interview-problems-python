def generateParenthesis(n):
    solutions = []
    
    def backtrack(string, openCount, closeCount):
        # if at end of permutation, add to the solution array
        if openCount == n and closeCount == n:
            solutions.append(string)
            return # end the backtracking
        
        # Our backtracking needs to be able to know when it's appropiate to add a "(" and when it's appropiate to add a ")".
        # It is only appropiate to add a ")" if there is a "(" that hasn't been matched to an end yet. 
        # It is only appropiate to add a "(" if the maximum amount of "(" we can do hasn't been reached.
        
        # if openCount > closeCount, add ")"
        if openCount > closeCount:
            backtrack(string + ")", openCount, closeCount + 1)

        # if openCount < n, if there's less "(" than the total "(" needed, add one.
        if openCount < n:
            backtrack(string + "(", openCount + 1, closeCount)

    backtrack("", 0, 0)
    return solutions


print(generateParenthesis(3))
