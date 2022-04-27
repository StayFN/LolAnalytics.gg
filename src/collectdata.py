import cassiopeia as cass
from cassiopeia import Summoner, Match
from cassiopeia.data import Season, Queue
from collections import Counter


def print_matches(name: str, region: str):

    cass.set_riot_api_key("API Key - DONT INCLUDE API KEYS in Github!!!") #Get it from Riot Dev Portal https://developer.riotgames.com/

    # Notice how this function never makes a call to the summoner endpoint because we provide all the needed data!

    summoner = Summoner(name=name, region=region)

    # A MatchHistory is a lazy list, meaning it's elements only get loaded as-needed.

    match_history = cass.get_match_history(
        continent=summoner.region.continent,
        puuid=summoner.puuid,
        begin_index = 0,
        end_index = 100)
    

    matchcount = 0
    for match in match_history:
        print(match.creation)
        for p in match.participants:
        # print(p.summoner.name, 'playing', p.champion.name)
          name = p.summoner.name
          print(f"Match: {matchcount} Name: {p.summoner.name}")
        
        matchcount += 1
         

print_matches("Fod Zensei" , "EUW")
