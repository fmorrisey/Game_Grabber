from types import SimpleNamespace

from collections import Counter as ct
import collections as col


# names , titles = platformData.copiesPerPlatform(gameData)

class platformData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def copiesPer_Dict(game_data):  # Calls multiple functions to return one dictionary
        numberOfPlatforms = platformData._findUniquePlatforms(game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        topPlatforms = platformData._top_Platforms(platforms, numberOfPlatforms)  # Sorts the data by top platform descending order
        return topPlatforms  # Returns Dict

    def copiesPer_Lists(game_data):  # Calls multiple functions to return two serpate lists of copies per console
        numberOfPlatforms = platformData._findUniquePlatforms(game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        topPlatforms = platformData._top_Platforms(platforms, numberOfPlatforms)  # Sorts the data by top platform descending order
        platform_names, platform_titles_count = platformData._zip_Platforms(topPlatforms)
        return platform_titles_count, platform_names  # Return Lists

    def NintendoAfter(game_Data, year):
        NintendoGames = platformData._groupManufactures(game_Data, year)
        return NintendoGames

    # Counts the number of publishers    
    def _titlesPer(json_data):
        platforms = ct(k.platform for k in json_data if k.platform)
        return platforms

    def _findUniquePlatforms(json_data, yearMin, yearMax):
        # finds unique publishers taking advantage of the set data structure
        # Constructor
        platform_set = set((""))

        for platform in json_data:
            if type(platform.year) != type(None) and platform.platform != type(None) and platform != type(None):
                if yearMin <= platform.year <= yearMax:
                    platform_set.add(platform.platform)
                else:
                    pass
            else:
                pass

        unique_platforms = len(platform_set)
        return unique_platforms

    def _top_Platforms(platforms, top):
        top_platforms = set((""))
        top_platforms = dict(ct(platforms).most_common(top))
        return top_platforms

    def _zip_Platforms(platforms):
        names, titles = zip(*platforms.items())
        print(names)
        print(titles)
        return names, titles

    def _groupManufactures(publishers, year):  # Groups consoles by manufacturer
        Nintendo = []
        Sony = []
        Microsoft = []
        Atari = []
        Sega = []
        PerComp = []
        Other = []

        for publisher in publishers:
            if type(publisher.year) != type(None):
                if publisher.year >= year:
                    if (publisher.platform == 'NES') or (publisher.platform == 'GC') or (
                            publisher.platform == 'SNES') or (publisher.platform == 'GBA') or (
                            publisher.platform == 'GB') or (publisher.platform == 'Wii') or (
                            publisher.platform == 'WiiU') or (publisher.platform == 'DS') or (
                            publisher.platform == '3DS') or (publisher.platform == 'N64'):
                        Nintendo.append(publisher)
                    else:
                        Other.append(publisher)
                    """
                    elif (publisher.platform == 'XB') or (publisher.platform == 'XOne') or (publisher.platform == 'X360'):
                        Microsoft.append(publisher)
                    elif (publisher.platform == 'PS') or (publisher.platform == 'PS2') or (publisher.platform == 'PS3') or (publisher.platform == 'PSP') or (publisher.platform == 'PS4') or (publisher.platform == 'PSV') or (publisher.platform == 'PSV'):
                        Sony.append(publisher)
                    elif (publisher.platform == 'SAT') or (publisher.platform == 'GEN'):
                        Sega.append(publisher)
                    elif (publisher.platform == '2600'):
                        Atari.append(publisher)
                    elif (publisher.platform == 'PC'):
                        PerComp.append(publisher)
                    """
                else:
                    pass
            else:
                pass

        return Nintendo  # , Sony, Atari, Microsoft, Atari, Sega, PerComp, Other
