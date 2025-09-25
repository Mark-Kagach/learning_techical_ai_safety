class Node():
    def __init__(self, movie, actor_id, parent):
        # 🚨 how to define state and parent here?
        # 💡 it is the movie actor pair, and from that I need to take the actor
        # 🚨 Should I do self.actor self.movie? self.parent? and put it instead of self.state everywhere

        self.movie = movie
        self.actor_id = actor_id
        self.parent = parent

class solution():
    def solve(self):
        # finds the path to the target if one exists

        # keep track of N of actors explored
        self.num_explored = 0

        # initialize frontier to just the starting position
        start = Node(state=self.start, parent=None)
        frontier = QueueFrontier()
        frontier.add(start)

        # initialize an empty explored set
        self.explored = set()

        # keep looping until solution found
        while True:
            # if nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")
            
            #choose a node from the frontier
            node = frontier.remove()
            self.num_explored+=1

            #if node is the goal, then we have a solution
            if node.state == self.goal:
                #cells?
                parents = []

                # Follow parent nodes to find solution
                while node.parent is not None:
                    parents.append(node.parent)
                parents.reverse()
                self.solution = (parents)
                return
            
            # mark node as explored
            self.explored.add(node.state)

            # add neighbors to frontier
            for xyz in self.neighbors_for_person(node.xyz):
                if not frontier.contains_state(xyz) and xyz not in self.explored:
                    child = Node(state=xyz, parent=node)
                    frontier.add(child)
