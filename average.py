import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    file_path=open('data.json')
    load=json.load(file_path)
    ans=0
    bus=0
    res=load.values()
    for i in res:
        bus+=i
        ans+=1
    return bus/ans
# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
