import math

# Given a list of dictionaries representing a dataset,
# returns the subset of dictionaries where a specific attribute matches a given value.
def getSubsetByAttributeValue(dataSet, attribute, value):
    subset = []
    for instance in dataSet:
        if instance[attribute] == value:
            subset.append(instance)
    return subset

# Returns all non-oracle attributes for a given dataset
def getDatasetAttributes(dataSet):
    attributes = []
    for key in dataSet[0]:
        if key != "Oracle":
            attributes.append(key)
    return attributes

# Iterates through a list of dictionaries and
# returns a list of all the values for a given attribute
def getAttributeValues(dataSet, attribute):
    values = []
    for instance in dataSet:
        if instance[attribute] not in values:
            values.append(instance[attribute])
    return values

# Returns the entropy of a given dataset,
# for traditional or multiclass problems.
def getEntropy(dataSet) -> float:
    entropy = 0
    for hypothesisClass in getAttributeValues(dataSet, "Oracle"):
        hypothesisClassSubset = getSubsetByAttributeValue(dataSet, "Oracle", hypothesisClass)
        probability = len(hypothesisClassSubset)/len(dataSet)
        entropy = entropy + (probability * math.log2(probability))
    # Avoid a -0 because I don't like how it looks
    if entropy != 0:
        entropy *= -1
    return entropy


# Returns the expected reduction in impurity in the given dataset,
# when partitioning by the given attribute.
def getInformationGainOfAttribute(dataSet, attribute) -> float:
    dataSetEntropy = getEntropy(dataSet)
    informationGain = dataSetEntropy
    for attrValue in getAttributeValues(dataSet, attribute):
        attributeSubset = getSubsetByAttributeValue(dataSet, attribute, attrValue)
        attrEntropy = getEntropy(attributeSubset)
        informationGain = informationGain - len(attributeSubset)/len(dataSet) * attrEntropy
    return informationGain