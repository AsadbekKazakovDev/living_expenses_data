import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    file_path=open('data.json')
    x=json.load(file_path)
    arzon = float("-inf")
    for item,value in x.items():
        if value>arzon:
            arzon=value
    return arzon

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)