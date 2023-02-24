import decisionTrees
import helper

sourceFiles = ["sample.data"]
for file in sourceFiles:
    dataSet = helper.importFile(file)
    dataSet = helper.convertToDict(dataSet)

    for attribute in decisionTrees.getDatasetAttributes(dataSet):
        helper.printHeader(attribute)
        for attrValue in decisionTrees.getAttributeValues(dataSet, attribute):
            attrEntropy = decisionTrees.getEntropy(decisionTrees.getSubsetByAttributeValue(dataSet, attribute, attrValue))
            print(attrValue + ": " + str(round(attrEntropy, 3)))
        print("Information Gain: " + str(round(decisionTrees.getInformationGainOfAttribute(dataSet, attribute), 3)))

    bestPartitionAttribute = ""
    bestPartition = 0
    for attribute in decisionTrees.getDatasetAttributes(dataSet):
        if decisionTrees.getInformationGainOfAttribute(dataSet, attribute) > bestPartition:
            bestPartition = decisionTrees.getInformationGainOfAttribute(dataSet, attribute)
            bestPartitionAttribute = attribute

    print("\nThe attribute that best paritions the data is " + bestPartitionAttribute + ".")