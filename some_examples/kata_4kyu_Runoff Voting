"""Your task is to implement a function that calculates an election winner from a list of voter selections using an Instant Runoff
Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this kata):

Each voter selects several candidates in order of preference.
The votes are tallied from the each voter's first choice.
If the first-place candidate has more than half the total votes, they win.
Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
In case of a tie for least, remove all of the tying candidates.
In case of a complete tie between every candidate, return nil(Ruby)/None(Python)/undefined(JS).
Start over.
Continue until somebody has more than half the votes; they are the winner.
Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in descending order of preference.
You should return the symbol corresponding to the winning candidate. See the default test for an example!"""

def get_key_from_value(value: int, data: dict) -> list[str]:
    '''return list of keys with value==value'''
    res: list[str] = []
    for key, v in data.items():
        if v == value:
            res.append(key)
    return res


def calculate_new_data(voters: list[list[str]]) -> dict:
    '''calculate dict: key=voter, value = count voter in 0 position'''
    data = {}
    for line in voters:
        data[line[0]] = data.get(line[0], 0) + 1
    return data


def runoff(voters: list[list[str]]) -> str:
    '''return the winner (name) of the voting or None
    data_res - dict: key=name, value = count
    '''

    data_res = calculate_new_data(voters=voters)

    voter_count = len(voters)
    max_voter_score = max(data_res.values())
    min_voter_score = min(data_res.values())
   
    if max_voter_score > voter_count / 2:
        return get_key_from_value(value=max(data_res.values()),
                                  data=data_res)[0]

    if max_voter_score != min_voter_score:
        key_to_delete = get_key_from_value(value=min_voter_score,
                                           data=data_res)

        voters_copy = voters.copy()
        
        for i, line in enumerate(voters):
            if line[0] not in key_to_delete:
                continue
            key = voters_copy[i][0]
            while key in key_to_delete or voters_copy[i][0] not in data_res:
                voters_copy[i].pop(0)
                key = voters_copy[i][0]
           
        return runoff(voters_copy)
