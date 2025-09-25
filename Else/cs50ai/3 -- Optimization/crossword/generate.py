import sys

from crossword import *

class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        # Creates a crossword object that has all the properties below.
        self.crossword = crossword
        # Give each variable in a crossword a domain of possible answers that is all words in the dataset.
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        # Leave all the words that have the same length.
        # Loop over all the variables.
        #🟢
        for item in self.domains:
            #print("length:", item.length)
            for word in self.domains[item].copy():
                if item.length != len(word):
                    self.domains[item].remove(word)
            #print(self.domains[item])  
        
        variables=list(self.crossword.variables)
        x=variables[0]
        y=variables[1]
        self.revise(x, y)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        🟢 False if no revision was made. => Have I actually accounted for all the cases?
        """
        
        #INPUTS 
        # Variable x and y. Which I figured out how to access only now.
        #self.print({})
        # print(self.crossword.variables)
        # print("")
        # print("x",x,self.domains[x])
        # print("")
        # print("y",y,self.domains[y])
        # print("")

        #COMPUTATIONS
        #1. Start with checking whether X has neighbors and if so, who they are.
        #2. Remove the corresponding value of X if it doesn't have a corresponding value in Y. 
        #*no double choosing of words allowed. hm.

        # print("Neighbors of X:",self.crossword.neighbors(x))
        # print("")
        # print("Overlaps:", self.crossword.overlaps[x,y])
        # print("")
        overlap=self.crossword.overlaps[x,y]

        if self.crossword.overlaps[x,y] == None: return False

        # So for the (0,1) down 5 X and (4,1) across 4 Y the overlap is (4,0)
        # For x it is the last letter, for y it is the first.
        # This X has: seven, eight, three domain; and Y: five, four, nine.
        # but shouldn't it overlap be 4,1?
        # Thankfully we know the (4,0) is not the overlap field, but the letter of xth and yth words that overlap. That makes things easier.
        # Now I need to check for each word in Xth domain and for xth overlap letter, whether there is in Yth domain a yth overlap letter. If no, remove word from domain.
        revision_made = False
        for xword in self.domains[x].copy():
            has_compatible_word = False
            for yword in self.domains[y]:
                # Check for word uniqueness in variables in consistent function. xword != yword and 
                if xword[overlap[0]] == yword[overlap[1]]:
                    has_compatible_word = True
                    break
            if not has_compatible_word:
                self.domains[x].remove(xword)
                revision_made = True
        # If no revision was made, but there are still values in the domain, return False
        if not revision_made and len(self.domains[x]) > 0:
            return False
        return revision_made

        # print("X Domains:", self.domains[x])
        # print("")

        #OUTPUTS
        # Return true if changes to domain of x were made, and false if not.

    def ac3(self, arcs=None):
        #🟡🧪 Not tested yet, so might have to go back.

        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        #INPUTS
        # A list of tuples (x,y), aka arcs, where x has an overlap with y (i.e. connection).

        #🟢 How do I get the initial list of all arcs in the problem?
        if arcs == None:
            arcs=[]
            for variable in self.crossword.variables:
                #print("V:", variable, "It's neighbors:", self.crossword.neighbors(variable))
                #print("")
                for neighbor in self.crossword.neighbors(variable):
                    arcs.append((variable, neighbor))
            #print(arcs)
            #print("")

        #COMPUTATIONS
        #1. Revise each arc one at a time via queue.
        for arc in arcs:
            #print(arc[0], arc[1])
            if self.revise(arc[0], arc[1]) == True:
                #make revision to arcs and add additional arcs to check consistency.
                #❓What arcs should I add when revision is made?
                # You loop over each neighbor of arc[0], except arc[1], 
                for neighbor in self.crossword.neighbors(arc[0]):
                    if neighbor == arc[1]: continue
                    arcs.append((arc[0], neighbor))
                    # then you check whether it is arc consistent. How to do that?
                    # add each neighbor of arc[0] back to the queue.

        #OUTPUT
        #return false is some variable has empty domain, else, if all constaints are enforced and all no domain is empty return true.
        for variable in self.domains:
            #print(self.domains[variable])
            if self.domains[variable] == {}:
                #print("Empty domain, and we should return false")
                return False

        #else, we return true.
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        # Check if every variable in the crossword has been assigned
        for variable in self.crossword.variables:
            if variable not in assignment:
                return False
        return True

        #⏩OUTPUT
        # return true if it is full, else false

        #🟡🧪 IDK how to test this.

    def consistent(self, assignment):
    
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        #➡️INPUT 
        # Assignment is a dictionary with keys of crossword variables, and values of words they take in.

        #🔀COMPUTATIONS
        #1️⃣ Check if all the values are distinct.
            # Check the length of unique set vs just of values, if differ, assignment inconsistent. 
        if len(set(assignment.values())) != len(assignment.values()):
            return False

        #2️⃣ Check if every value is of correct length.
        for variable, value in assignment.items():
            if len(value) != variable.length:
                return False

        #3️⃣ Check if there are no conflicts between neighbors.
        for var1 in assignment:
            for var2 in self.crossword.neighbors(var1):
                # Only check if var2 is also assigned
                if var2 in assignment:
                    overlap = self.crossword.overlaps[(var1, var2)]
                    if overlap is not None:
                        i, j = overlap
                        word1 = assignment[var1]
                        word2 = assignment[var2]
                        if word1[i] != word2[j]:
                            return False

        #⏩OUTPUT
        # Return true if assignment consistent, else false.
        return True

        #🟡🧪 TESTING
        #❓ How do I test this?

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        #➡️INPUT 
        # var is a variable object, while assignment is the dictionary with keys of 
        # variable names and values of words they take in.
        # use revise function  


        #🔀COMPUTATIONS

        #3a.
        value_counts = {value: 0 for value in self.domains[var]}

        #1️⃣ Looping
        # Loop over var's domain values.
        for value in self.domains[var]:
            # For each value, loop over var's neighbors. 
            count=0
            for neighbor in self.crossword.neighbors(var):
                #2️⃣ Checking
                # Check how much neighbor's values each var's value rules out. Keep count.
                # Two things rule out neighbor's domain values: uniqueness and overlap letters.
                
                #🔴 forgot to check whether the neighbor value is already in assignment, so it shouldn't count.
                if neighbor in assignment: continue

                #2a. Check uniqueness. Loop over neighbor domains, compare it with value
                for neighbor_domain in self.domains[neighbor]:
                    if value==neighbor_domain: 
                        count+=1
                        continue
                
                    #2b. Check letter overlap. Loop over neighbor domains
                    overlap = self.crossword.overlaps[(var, neighbor)]
                    if overlap is not None:
                        i, j = overlap
                        if value[i] != neighbor_domain[j]:
                            count+=1

            value_counts[value] = count

        #3️⃣ Sorting and returning
        #3a. Make a dictionary that keeps a score of domain's values and their adjacent rule out score.
        # Based on that dictionary return a list of sorted values.

        #⏩OUTPUT
        # Should return the list of all the domain values of var, ordered to the least constraining heuristic.
        return sorted(value_counts.keys(), key=lambda x: value_counts[x])

        #🟡🧪 TESTING
        #

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        #➡️INPUT 
        # Assignment that is a dictionary with keys of variables and values of words represent.

        #🔀COMPUTATIONS
        # Minimum remaining value heuristic is about assigning variables starting with the one with smallest domain length.
        # If tie in domains, choose the one with the biggest number of neighbors, if tie again, return any.

        #1️⃣ Get all unassigned variables and loop over them.
        unassigned_vars = [var for var in self.crossword.variables if var not in assignment]
        
        # If no unassigned variables, return None
        if not unassigned_vars:
            return None

        min_domain=float('inf')
        candidates = []

        for variable in unassigned_vars:

            #2️⃣ Save those with the least domain.
            domain_size = len(self.domains[variable])
            
            if domain_size < min_domain:
                candidates = [variable]
                min_domain = domain_size
                
            elif domain_size == min_domain:
                candidates.append(variable)

        #3️⃣ If more than 1, pick the one with the biggest number of neighbors.
        #for neighbor in self.crossword.neighbors(variable):
        if len(candidates)==1:
            return candidates[0]

        else:
            max_neighbors = -1
            best_vars = []

            for var in candidates:
                num_neighbors = len(self.crossword.neighbors(var))
                
                if num_neighbors > max_neighbors:
                    best_vars = [var]
                    max_neighbors = num_neighbors
                    
                elif num_neighbors == max_neighbors:
                    best_vars.append(var)
            
            return best_vars[0]

        #⏩OUTPUT
        # Return a single variable that is not yet assigned based on the minimum remaining value heuristic

        #🧪TESTING
        #

        #❤️MISTAKES
        #looped over all variables, not just the unassigned ones.

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        #➡️INPUT 
        # Takes in a partial assignment dictionary

        #🔀COMPUTATIONS
        # From input computes output via backtracking search.

        # Check if assignment is complete (base case)
        if self.assignment_complete(assignment):
            return assignment

        #1️⃣ Select an unassigned variable using the select_unassigned_variable function.
        var = self.select_unassigned_variable(assignment)
        print(var)

        # If no unassigned variable found, return None
        if var is None:
            return None

        #2️⃣ Loop over all the values in that variable's domain. Try to assign it.
        for value in self.domains[var]:
            print(var, value)
            print("")
            #2a. make a copy and add value to the new assignment
            new_assignment = assignment.copy()
            new_assignment[var]=value
            print(new_assignment)
            print("")
            print("")

            #2b. check if new assignment is consistent
            if self.consistent(new_assignment):
                #3️⃣ If assignment of that variable is good: add it to the assignment, and call backtrack with this new assignment, repeat that until it is good. if all filled, return the assignment.
                
                
                result=self.backtrack(new_assignment)

                if result is not None: 
                    print(result)
                    return result
        
        #4️⃣ Else remove that value from the variable's domain as eventually it leads to a problem.

        return None

        #⏩OUTPUT
        # Returns a completed assignment dictionary if possible, else None (i.e. return None if none of the options worked.)

        #🧪TESTING
        #

        #❓QUESTIONS
        #1. How backtracting search works? => Check cs50ai lecture.
            # We make assignment to variables, and if at any point we can't make further assignments, we go back and try different values.

        #❤️MISTAKES
        #

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)

if __name__ == "__main__":
    main()
