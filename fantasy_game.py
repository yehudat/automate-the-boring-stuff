import pprint

#pprint examples:
#   pprint.pprint(someDictionaryValue)   - print
#   pprint.pformat(someDictionaryValue)) - pass as a string

def displayInventory(inventory):
    print("Inventory:")
    sum_of_items = 0
    for k,v in inventory.items():
        print(str(v)+" "+k)
        sum_of_items += v
    print("Total number of items: " + str(sum_of_items))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

inventory  = {'arrows': 4, 'bow': 1, 'dagger': 3}
dragonLoot = ['coin', 'dagger', 'coin', 'coin', 'ruby']

displayInventory(inventory)
print("")
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
