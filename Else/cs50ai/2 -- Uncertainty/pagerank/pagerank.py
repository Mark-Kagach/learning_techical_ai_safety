import os
import random
import re
import sys
import copy

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    #print(f"PageRank Results from Sampling (n = {SAMPLES})")
    #for page in sorted(ranks):
        #print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    #print(f"PageRank Results from Iteration")
    #for page in sorted(ranks):
        #print(f"  {page}: {ranks[page]:.4f}")

def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    #INPUTS
    #corpus is a dictionary representing link structure
    #page is the current page string
    #damping is the floating point

    #COMPUTATION
    #≈🟡 0. If page has no links, take all pages in the corpus and assign equal probabilities to them.
    #corpus[page]= ""
    if corpus[page] == "":
        print(page, "is empty.")
        #new_prob_distr = {key: 1/len(corpus) for key in corpus}
        for key in corpus:
            corpus[key] = 1/len(corpus)
        print(corpus)
        print("")
        return corpus

    #✅1. Create a dictionary with the same keys as corpus.
    #new_prob_distr = {key: 0 for key in corpus}
        #✅3. Take all pages in the corpus and divide the 1-d factor equally between them.
        #new2_prob_distr = {key: (1-damping_factor)/len(corpus) for key in corpus}
    new_prob_distr = {key: (1-damping_factor)/len(corpus) for key in corpus}
    
    #✅2. Take links of the current page, divide the dampling factor equally between them.
    #new2_prob_distr = {key: damping_factor/len(corpus[page]) for key in corpus[page]}
        #✅4. Sum up the values from step 2 and 3 and output probabilities.
    for key in corpus[page]:
        new_prob_distr[key] += damping_factor/len(corpus[page])
    

    #OUTPUT
    # the output is a dictionary for each page in the corpus with probability of getting to it
    #print(" ")
    #print("probability distr:", new_prob_distr)
    #print(" ")
    return new_prob_distr

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    #INPUTS:
    # corpus
    # damping factor
    # n of samples

    #COMPUTATION
    #1. Pick a random page from the corpus.
    #2. Generate the first sample based on it.
    #3. Iterate for N of sample times:
        #3a. generate the next sample from the past sample's transition model.
        # You will likely want to pass the previous sample into your transition_model function, along with the corpus and the damping_factor, to get the probabilities for the next sample.
        #3b. Count which page was chosen and add 1 to it.
    #4. Once the loop is over divide counts by sample n and return the probability dictionary.

    #0. duplicate the corpus with values 0.
    count_corpus = {key: 0 for key in corpus}
    #print("Count corpus:", count_corpus)

    #🟢1. iterate for N of samples
    count = 0
    while count < n:
        
        #🟢2. if first sample, pick a random page from the corpus.
        if count == 0:
            page = random.choice(list(corpus))
            #print("Random first page:", page)

        #🟢3. generate transition model based on the probabilities and page
        trans_mod = transition_model(corpus, page, damping_factor)

        #🟢4. pick random page based on the transition model
        # Extract keys and corresponding weights
        keys = list(trans_mod.keys())
        weights = list(trans_mod.values())
        # Choose one key based on weights
        random_page = random.choices(keys, weights=weights, k=1)[0]
        #print("Randomly chosen page:", random_page)

        #🟢5. Update count_corpus based on the picked random page.
        count_corpus[random_page]+=1
        #print(count_corpus)

        #🟢6. Updata page based on the chosen page.
        page = random_page

        #print(count)
        count+=1

    print("Count corpus updated:", count_corpus)

    #🟢7. Calculate the probabilities based on the count corpus.
    prob_corpus = {key: 0 for key in corpus}
    for key in corpus:
        prob_corpus[key] += count_corpus[key]/SAMPLES
    print("Prob corpus:", prob_corpus)


    #OUTPUT:
    # Dictionary based on corpus with probability distributions based on sample and damping factor.

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    #INPUTS
    #corpus 
    #damping factor

    #COMPUTATION
    #🟢1. Assign each page a 1/N probability.
    pr_corpus = {key: (1)/len(corpus) for key in corpus}
    #print()
    #print("PR corpus:", pr_corpus)
    #print()

    #2. Calculate the new values based on the math formula.
        #PR(page) = (1-d)/N + d +d*∑PR(i)/NumLinks(i)
        #pr(i) is the pagerank of the page that links "page"
        #NumLinks(i) is the number of total links of page i
        #so when we divide pr(i) by numlinks(i) we calculate the chance user ends up on our "page" given
    
    
    #🟢3a. Make a duplicate of the pr_corpus before the calculation
    #🔴This is not a duplication, but a pointer!
    before_pr_corpus=copy.copy(pr_corpus)
    #print("")
    #print("Past corpus:",before_pr_corpus)
    #print("")

    while True:

        #🔴2a. Iterate over the corpus, calculate the PR using formula
        for key in corpus:
            #print(f"For {x}, {key}:")

            sum_links=0
            #🟢2b. calculate the sum part of the formula
                #🟢2ba. Find each page i that links to our "key page"
            for k,v in corpus.items():
                #print(k,v)
                for link in v:
                    #print(link)
                    if link==key: 
                        #print("Sum links before:", sum_links)
                        #print("Adding:", pr_corpus[k]/len(corpus[k]))
                        # 🔴 GOT LOST IN WHOM IN K VS KEY WAS TAKING THE WRONG VALUES.
                        sum_links=sum_links+(pr_corpus[k]/len(corpus[k]))
                        #print("Sum links after:",sum_links)

            pr_corpus[key] = (1-damping_factor)/len(corpus)+damping_factor*sum_links

            #print(pr_corpus[key])
            #print("")
            
            #2b. If page has no links treat as if it has one link to every page including itself (i.e. spread probability equally).

        #🟢3c. Check the differences and quit the loop if all values are within the 0.001 range.
        #print("")
        #print(f"{x}: pr_corpus:{pr_corpus}")
        #print(f"{x}: before corpus:{before_pr_corpus}")
        difference=[]
        for key in corpus:
            difference.append(pr_corpus[key]-before_pr_corpus[key])
        #print(f"{x}: difference: {difference}")
        if all(val > 0.001 or val<-0.001 for val in difference):
            break
        
        #🟢Change the value of the past corpus.
        before_pr_corpus=copy.copy(pr_corpus)
    
    #3. Repeat step 2 until no pagerank value changes for more than 0.001.
        #3a. Make a duplicate of the pr_corpus before the calculation
        #3b. make calculation to find new version of after_pr_corpus
        #3c. Compare the each value of after_pr_corpus with the before_pr_corpus, if any differs by more than 0.001 continue, else break

    #OUTPUT
    # Return dictionary based on corpus of pagerank probabilities within 3 decimals (0.001).
    print()
    print("PR Corpus Output:", pr_corpus)
    print()

    return pr_corpus

if __name__ == "__main__":
    main()
