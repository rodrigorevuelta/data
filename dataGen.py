import json

def readJson():
    with open('json/item.json') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            print('Name: ' + p['name'])
            print('Website: ' + p['website'])
            print('From: ' + p['from'])
            print('')
def main():
    file = open('json/item.json')
    dct = json.load(file)
    print(dct)

if __name__=="__main__":
    main()
