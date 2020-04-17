JET_SIDE_MENU_ITEMS = [
    {'label': 'Users', 'app_label': 'EUIVUserManagement', 'items': [
        {'name': 'euivuser'},
    ]},
    {'label': 'Savegames', 'app_label': 'EUIVSaveGame', 'items': [
        {'name': 'euivsavegame'},
        {'name': 'euivpathconfig'},
    ]},
    {'label': 'Countries', 'app_label': 'EUIVCountries', 'items': [
        {'name': 'euivcountry'},
        {'name': 'euivprovince'},
    ]},
    {'label': 'Stats', 'app_label': 'EUIVStats', 'items': [
        {'name': 'euivcountrystats'},
        {'name': 'euivprovincestats'},
    ]},
]

JET_CHANGE_FORM_SIBLING_LINKS = False
JET_SIDE_MENU_COMPACT = True
