import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []
    
    # Month name to number mapping
    months = {
        'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5,
        'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
    }
    
    # Open the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        # Skip the header row
        next(reader)
        
        # Process each row
        for row in reader:
            # Convert each column to the appropriate type
            evidence_row = [
                int(row[0]),           # Administrative
                float(row[1]),         # Administrative_Duration
                int(row[2]),           # Informational
                float(row[3]),         # Informational_Duration
                int(row[4]),           # ProductRelated
                float(row[5]),         # ProductRelated_Duration
                float(row[6]),         # BounceRates
                float(row[7]),         # ExitRates
                float(row[8]),         # PageValues
                float(row[9]),         # SpecialDay
                months[row[10]],       # Month (convert to 0-11)
                int(row[11]),          # OperatingSystems
                int(row[12]),          # Browser
                int(row[13]),          # Region
                int(row[14]),          # TrafficType
                1 if row[15] == 'Returning_Visitor' else 0,  # VisitorType
                1 if row[16] == 'TRUE' else 0                # Weekend
            ]
            
            # Convert Revenue (last column) to label
            label = 1 if row[17] == 'TRUE' else 0
            
            evidence.append(evidence_row)
            labels.append(label)
    
    #print(evidence[379])
    #print(labels[379])
    return (evidence, labels)

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    #print(model.predict([[2, 102.5, 3, 60.0, 22, 1034.975, 0.0, 0.014, 16.14384, 0.0, 2, 1, 1, 4, 2, 1, 0]]))
    return model

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    #➡️INPUT 
    # List of actual labels, and a list of predicted labels.

    #🔀COMPUTATIONS
    #1️⃣ Loop over the predicted, compare the value to the actual ones.
    true_positive=0
    false_positive=0
    true_negative=0
    false_negative=0

    for i, label in enumerate(labels):
        #2️⃣ To calculate sensitivity:
            #2a. Calculate true positives: If predicted is 1 and it equals actual then it is true positive.
            #2b. Calculate false negatives: if predicted is 0, yet actual is 1.
            #2c. Calculate true negatives: If predicted is 0 and it equals actual then it is true negative.
            #2d. Calculate false positives: if predicted is 1, yet actual is 0.
            
        if label==1 and label==predictions[i]: 
            true_positive+=1
        if label==1 and predictions[i]==0:
            false_negative+=1
        if label==0 and label==predictions[i]:
            true_negative+=1
        if label==0 and predictions[i]==1:
            false_positive+=1

    print(true_positive)
    print(true_negative)
    print(false_positive)
    print(false_negative)

    #3️⃣ To calculate specificity, sensitivity:
        #3a. Divide the true positives by true positives+false negatives.
        #3b. Divide the true negatives by true negatives+false positives.
    sensitivity = true_positive/(true_positive+false_negative)
    specificity = true_negative/(true_negative+false_positive)

    #⏩OUTPUT
    # A tuple of (sensitivity, specificity).
    #print(sensitivity, specificity)
    return (sensitivity, specificity)

    #🧪TESTING
    #

    #❓QUESTIONS
    #

    #❤️MISTAKES
    #



if __name__ == "__main__":
    main()
