import csv
import json
from .config import ADD_RARITY, LAYER_ORDER

def rarity_json(data):
    with open('rarity.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
def init_CSV():
    with open(r'results/csv/nft.csv', 'a') as f:
        CSV_HEADERS = LAYER_ORDER
        CSV_HEADERS.insert(0, 'edition')
        if ADD_RARITY:
            CSV_HEADERS.append('rarity')
        writer = csv.writer(f)
        writer.writerow(CSV_HEADERS)

def write_to_CSV(data):
    with open(r'results/csv/nft.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
def individual_json(data):
    #data needs to come in as a dictionary for this to work
    with open(f'results/json/{data["edition"]}.token.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def json_metadata(data):
    with open(f'results/json/_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)