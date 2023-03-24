import json


def memorize(lst, typ):
    """Take a lst and spit out a dictionary."""
    dict = {}
    for appliance in lst:
        dict[appliance.name] = {"price": appliance.price,
                                "img": appliance.img,
                                "desc": appliance.desc,
                                "depth": appliance.depth}

    with open(f"{typ}.txt", "w") as f:
        f.write(json.dumps(dict))
        f.close()
    return dict

def remember(typ):
    """Check for existing json"""
    jsn = ""
    with open(f"{typ}.txt", "r") as f:
        jsn = f.readline()
    return json.loads(jsn)