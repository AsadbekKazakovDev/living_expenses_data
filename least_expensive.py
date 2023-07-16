import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    file_path=open('data.json')
    x=json.load(file_path)
    arzon = float("inf")
    for item,value in x.items():
        if value<arzon:
            arzon=value
    return arzon

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
