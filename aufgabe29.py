d1 ={"Hans": [2,1,3],
    "Ueli": 2,
    "Barack": "Thanks Obama",
    "doc": {"ID": 123},
    "myBad": {420: 69}}

d2 = {"myBad": {420, 69},
    "doc": {"ID": 444},
    "Ueli": 2,
    "Barack": "Obama cares",
    "Mozart": "Can you eat this"}

sameDict = {1: 2,
            2: 3}
sameDict2 = {2: 3,
            1: 2}

notSame = {"dict": {
            1: 2
}}

notSame2 = {"dict": {
            1: 3
}}

testList = [(d1, d2), (sameDict, sameDict2), (notSame, notSame2)]

def isSame(dict1: dict, dict2: dict) -> bool:
    return dict1 == dict2

def differance (dict1: dict, dict2: dict) -> list:
    differances = []

    for key in dict1:
        if not key in dict2:
            differances.append(key)
        elif not dict1[key] == dict2[key]:
            differances.append(key)
    return differances

def bothDiferances (dict1: dict, dict2: dict) -> list:
    differances = []
    if isSame(dict1, dict2):
        return [[],[]]
    differances.append(differance(dict1, dict2))
    differances.append(differance(dict2, dict1))
    return differances



for testGroup in testList:
    print("____________________________________________________")
    print(f"Are the two dictionaries the same? {isSame(*testGroup)}")
    differances = bothDiferances(*testGroup)
    print(f"Indices in frist Dict, that are different:\n\t{differances[0]}")
    print(f"Indices in second Dict, that are different:\n\t{differances[1]}")
    differances[0].extend(differances[1])
    mySet = set(differances[0])
    print(f"all different indices: {mySet if mySet else 'None'}")
    print(f"tested Dictionaries:\n\n{testGroup[0]}\n\n"\
        f"and \n\n{testGroup[1]}")
    print("____________________________________________________")
