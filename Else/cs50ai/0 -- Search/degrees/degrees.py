import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}

# loads data from csv files to these data structures 
def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass

#❌ What loading into memory means?

#loads data into memory (you can specify which directory)
def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.
    
    If no possible path, returns None.
    """
    # the source and target are already transcribed into ids

    """ 🚨 right now i'm trying to understand what neighbors for person function actually returns as it is my first clue
     💡 It returns a set (unordered collection of unique items) of tuples. 
           Each tuple is a pair and has a movie_id and person_id that represent an actor and the movie where 
           they had played together with the inputted actor."""

    """  We can check whether each of the items is a target, if it isn't we call a function for each of the actor in a pair 
    and check the further resulted are the target, we do that recursively until we either find target, or ran out of options returning none"""

    """ 🚨 How to implement a bread first search for that problem?
         Let's review how he explained it in the lecture
     💡 In BFS we use queue data structure
        I'd guess we go over each item added to the queue and if it's not the target go to the next one. 
        If we're out of options, there's no connecting path.
        how do we use neighbors for person function? We explore the set of tuples to check if either of them is a target, 
        if it isn't, we call neighbors for person function for each of the person, and go over that list, """

    # 🚨 in a node I don't need to represent an action or path cost, just parent. What do I do with state? 

    # print("Source ID:")
    # print(source)
    # print("Target ID:")
    # print(target)

    # keep track of explored actors
    num_explored = 0

    #initialize the frontier
    frontier = QueueFrontier()

    # Add source as the first node in a frontier
    start = Node(movie = None, actor = source, parent = None)
    frontier.add(start)

    # initialize an empty explored set
    explored = set()

    # keep looping until solution is found
    while True:
        # if nothing left in frontier, then no path
        if frontier.empty():
            raise Exception("no solution")
        
        #choose a node from the frontier
        node = frontier.remove()
        #print("Comparing this actor to target: ")
        #print(node.actor)
        num_explored+=1

        # if node.actor is the target, then we have a solution
        if node.actor == target:
            print("Found!")
            parents = []

            #print("Parent of the final node")
            #print(node.parent)
            # follow parent nodes to find solution
            # 🚨 problem with node.parent line, goes forever for some reason.
            while node.parent is not None:
                parents.append(node)
                node = node.parent
            
            print(parents)
            parents.reverse()

            solution = []

            for parent in parents:
                solution.append((parent.movie, parent.actor))

            print("Solution:")
            print(solution)
            return solution

        # else
        # mark node as explored
        explored.add(node.actor)
        #print("Explored so far: ")
        #print(explored)

        # add neighbors to frontier
        # 🚨 how to make this shit work
        for neighbor in neighbors_for_person(node.actor):
            # print("All the neighbors there are")
            # print(neighbors_for_person(node.actor))
            # print("of the actor")
            # print(node.actor, node.movie)
            # print("The neighbor")
            # print(neighbor)

            #just check whether the neighbor is a target
            if not frontier.contains_state(neighbor[1]) and neighbor[1] not in explored:
                    # print("Creating a node out of a neighbor")
                    neighbor_node = Node(movie = neighbor[0], actor= neighbor[1], parent = node)
                    frontier.add(neighbor_node)
                    # print("Updating the frontier by adding the neighbor to it")
                    # print(frontier.frontier)

    """your function should return a list, where each list item is the next (movie_id, person_id) 
        pair in the path from the source to the target.
    💡 so I can just use the neighbors_for_person tuples"""

    raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]

#returns a set (unordered collection of unique items) of tuples with (movie_id, person_id) pairs
def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
