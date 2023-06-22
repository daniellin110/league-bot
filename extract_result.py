import re
import requests
    
def extract_result(link):
    regex = r"(?<=lichess\.org\/)(\w{8})"
    match = re.search(regex, link)
    if not match:
        return []
    
    game_id = match.group(1)
    URL = "https://lichess.org/game/export/" + game_id
    PARAMS = {'pgnInJson':"true"}
    HEADERS = {'Accept': 'application/json'}
   
    r = requests.get(url = URL, params = PARAMS, headers=  HEADERS)
    if r.status_code != 200:
        return []
    
    data = r.json()
    white = data['players']['white']['user']['name']
    black = data['players']['black']['user']['name']
    if 'winner' in data:
        winner = data['winner']
        if winner == 'white':
            win = 'Win'
        else:
            win = 'Loss'
    else:
        winner = 'none'
        win = 'Draw'
    return [white, black, win, winner]

# if __name__ == "__main__":
#     link = <game link>
#     result = extract_result(link)
#     print(result)
