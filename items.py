import argparse
import json
import random 

def get_items(items, value):
    for key in list(items.keys()):
        if "Included" not in items[key]:
            items[key]["Included"] = []
        included = random.choice([True, False])
        if included == True:
            items[key]["Included"].append(value)
        elif value == True:
            items[key]["Included"].append(False)

def print_items(items):
    included = f""
    for i, (key, value) in enumerate(items.items()):
        included_list = value["Included"]
        if len(included_list) == 0:
            team_str = "None"
        elif len(included_list) == 1:
            team_str = included_list[0]
        else:
            team_str = "Both"
        included += f"{key}: {team_str}\n"
        if i % 6 == 5:
            included += f"\n"
    print(included)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Choose custom items")

    parser.add_argument("--items", default="./base_game/items.json",
                        type=str, help="Path of the items json")
    parser.add_argument("--teams", action='store_true',
                        help="If the script should randomize each item per team")
    args = parser.parse_args()

    with open(args.items, 'r') as items_json:
        items = json.load(items_json)
    items = {k:v for (k,v) in items.items() if v["Enable"] == True}

    if args.teams:
        get_items(items, "Red")
        get_items(items, "Blue")
        print_items(items)      

    else:
        get_items(items, True)
        print_items(items)
