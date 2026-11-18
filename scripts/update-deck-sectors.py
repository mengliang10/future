import glob, json

# Map deck sector to Future Tech category
# For the 11 official sector decks:
OFFICIAL_MAP = {
    'information-technology-01': 'semiconductors',
    'financials-01': 'blockchain',
    'health-care-01': 'drugs-biotech',
    'consumer-discretionary-01': 'spatial-computing',
    'communication-services-01': 'applied-ai',
    'industrials-01': 'robotics',
    'consumer-staples-01': 'applied-ai',
    'energy-01': 'energy',
    'materials-01': 'materials-physics',
    'real-estate-01': 'applied-ai',
    'utilities-01': 'energy',
}

DECK_PREFIX_MAP = {
    'semiconductors': 'semiconductors',
    'ai': 'applied-ai',
    'quantum': 'quantum',
    'biotech': 'drugs-biotech',
    'robotics': 'robotics',
    'autonomous': 'autonomous',
    'energy': 'energy',
    'space': 'space',
    'cyber': 'cybersecurity',
    'blockchain': 'blockchain',
    'xr': 'spatial-computing',
    'bci': 'bci',
    'marketing': 'applied-ai',
    'policy': 'applied-ai',
    'markets': 'blockchain',
}

files = glob.glob('/media/ml/Storage1/The Future Tomorrow/src/content/decks/*.json')
for f in files:
    with open(f, 'r', encoding='utf-8') as df:
        d = json.load(df)
    did = d['id']
    if did in OFFICIAL_MAP:
        d['sector'] = OFFICIAL_MAP[did]
    else:
        prefix = did.split('-')[0]
        if prefix in DECK_PREFIX_MAP:
            d['sector'] = DECK_PREFIX_MAP[prefix]
        else:
            d['sector'] = 'applied-ai'
    with open(f, 'w', encoding='utf-8') as df:
        json.dump(d, df, indent=2)

print("Updated deck sectors to Future Tech categories.")
