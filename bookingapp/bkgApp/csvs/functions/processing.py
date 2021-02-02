def title_name(title):

    title_dict = {
        'BLI': 'Bali',
        'MDA': 'Madeira',
        'PST': 'Paris trip',
        'FOS': 'F1 stage',
        'HAB': 'Hot air balloon',
        'RSS': 'Route 66',
        'MIL': 'Milano',
        'ITL': 'Italy',
        'FRC': 'France',
        'RME': 'Rome',
        'VER': 'Versailles',
        'LDA': 'London',
        'LDB': 'London',
        'HLX': 'Halifax',
        'ENG': 'England',
        'NAN': 'NONE'
    }
    for key, value in title_dict.items():
        if value == title:
            return key
