import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    data1 = open(file_path)
    data = json.load(data1)
    s=0
    for i in data.values():
            s+=(i)
    return s


# test
file_path = "data.json"
total = total_expenses(file_path)
print(total)
