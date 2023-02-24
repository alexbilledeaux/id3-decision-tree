# Imports the content of a given filename from the assets subdirectory.
def importFile(fileName: str):
    file = open('assets/' + fileName, 'r')
    content = file.read()
    file.close()
    content = content.encode('ascii', 'ignore')
    content = content.decode()
    return content

# Converts a string into an list of dictionaries,
# each of which represents an instance (row) in the data set.
def convertToDict(content: str):
    # Use column headers to structure dictionary
    headers = []
    headerString = content.partition("\n")[0]
    for x in range(headerString.count(' ') + 1):
        headers.append(headerString.partition(" ")[0])
        headerString = headerString.partition(" ")[2]
    # Remove column headers
    content = content.partition("\n")[2]
    # Get a list of each line in the data file
    lines = content.splitlines()
    # Convert each line into a dictionary that represents an instance (row)
    instances = []
    for line in lines:
        instance = {}
        for i, header in enumerate(headers):
            instance[header] = line.partition(" ")[0]
            line = line.partition(" ")[2]
        instances.append(instance)
    return instances

# Prints a formatted header with the given text to the console
def printHeader(header: str):
    print("\n--------------------\n" + header + "\n--------------------")