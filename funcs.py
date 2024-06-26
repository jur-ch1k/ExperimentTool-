import json
import itertools


def readJSON(path):
    with open(path, 'r') as f:
        file = f.read()
    return json.loads(file)


def getParamsNames(paramArr):
    fileParamsNames = None
    cmdParamsNames = None

    if 'fileParams' in paramArr[0]:
        fileParamsNames = list(paramArr[0]['fileParams'].keys())
    if 'cmdParams' in paramArr[0]:
        cmdParamsNames = list(paramArr[0]['cmdParams'].keys())

    return {'fileParams': fileParamsNames, 'cmdParams': cmdParamsNames}


def getParamsCombinations(params, paramsNames):
    combinations = []
    paramDict = dict.fromkeys(paramsNames)
    for paramList in itertools.product(*list(params.values())):
        for i in range(len(paramsNames)):
            paramDict[paramsNames[i]] = paramList[i]
        combinations.append(paramDict.copy())
    return combinations


def strFromParams(paramDict, templateStr):
    if paramDict:
        for params in paramDict:
            yield templateStr.format(**params)
    else:
        yield templateStr


def tupleForSort(tup):
    res = ()

    for i, elem in enumerate(tup):
        try:
            res += int(elem),
        except ValueError:
            try:
                res += float(elem),
            except ValueError:
                res += elem,

    return res
