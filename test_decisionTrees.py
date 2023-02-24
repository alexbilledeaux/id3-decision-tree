import decisionTrees
import helper

dataSet = helper.importFile("test.data")
dataSet = helper.convertToDict(dataSet)

# Entropy Test Suite
attributeSet = decisionTrees.getSubsetByAttributeValue(dataSet, "Pulse", "Strong")
assert round(decisionTrees.getEntropy(attributeSet), 3) == 0.918, f"Expected 0.918 for Entropy(Pulse=Strong). Recieved {round(decisionTrees.getEntropy(attributeSet), 3)}."
attributeSet = decisionTrees.getSubsetByAttributeValue(dataSet, "Pulse", "Weak")
assert round(decisionTrees.getEntropy(attributeSet), 3) == 1, f"Expected 1 for Entropy(Pulse=Weak). Recieved {round(decisionTrees.getEntropy(attributeSet), 3)}."
attributeSet = decisionTrees.getSubsetByAttributeValue(dataSet, "BP", "Normal")
assert round(decisionTrees.getEntropy(attributeSet), 3) == 0, f"Expected 0 for Entropy(BP=Normal). Recieved {round(decisionTrees.getEntropy(attributeSet), 3)}."
attributeSet = decisionTrees.getSubsetByAttributeValue(dataSet, "BP", "Abnormal")
assert round(decisionTrees.getEntropy(attributeSet), 3) == 0, f"Expected 0 for Entropy(BP=Abnormal). Recieved {round(decisionTrees.getEntropy(attributeSet), 3)}."
attributeSet = decisionTrees.getSubsetByAttributeValue(dataSet, "Age", "Teen")
assert round(decisionTrees.getEntropy(attributeSet), 3) == 0, f"Expected 0 for Entropy(Age=Teen). Recieved {round(decisionTrees.getEntropy(attributeSet), 3)}."
attributeSet = decisionTrees.getSubsetByAttributeValue(dataSet, "Age", "Adult")
assert round(decisionTrees.getEntropy(attributeSet), 3) == 0, f"Expected 0 for Entropy(Age=Adult). Recieved {round(decisionTrees.getEntropy(attributeSet), 3)}."
attributeSet = decisionTrees.getSubsetByAttributeValue(dataSet, "Age", "Senior")
assert round(decisionTrees.getEntropy(attributeSet), 3) == 0.918, f"Expected 0.918 for Entropy(Age=Senior). Recieved {round(decisionTrees.getEntropy(attributeSet), 3)}."

# Information Gain Test Suite
assert round(decisionTrees.getInformationGainOfAttribute(dataSet, "Pulse"), 3) == 0.02, f"Expected 0.02 for the Information Gain of attribute 'Pulse'. Recieved {round(decisionTrees.getInformationGainOfAttribute(dataSet, 'Pulse'), 3)}."
assert round(decisionTrees.getInformationGainOfAttribute(dataSet, "BP"), 3) == 0.971, f"Expected 0.097 for the Information Gain of attribute 'BP'. Recieved {round(decisionTrees.getInformationGainOfAttribute(dataSet, 'BP'), 3)}."
assert round(decisionTrees.getInformationGainOfAttribute(dataSet, "Age"), 3) == 0.42, f"Expected 0.42 for the Information Gain of attribute 'Age'. Recieved {round(decisionTrees.getInformationGainOfAttribute(dataSet, 'Age'), 3)}."

print("All tests successful!")