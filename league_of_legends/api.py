import requests
import json
import time
import pandas as pd
import numpy as np

api_key  = "RGAPI-cb0427f5-c69a-4ae4-a5b0-79317f1de441"
kr_api   = "https://kr.api.riotgames.com"
asia_api = "https://asia.api.riotgames.com"
api_limit_secs = 125

def get_player_by_tier(api_key, queue="RANKED_SOLO_5x5", tier="challenger", division=1, page=1):
    """
    티어별 리그데이터를 가져오는 함수입니다.
    
    api_key : Riot에서 발급받은 api key
    queue   : 솔로랭크인지, 듀오랭크인지와 같은 queue type
    tier    : 랭크 티어
    division: tier에서 더 나뉘는 티어 1~4
    page    : 데이터를 가져오려는 기록 페이지
    
    """
    high_tier = ["challenger", "grandmaster", "master"]
    
    # 마스터 이상
    if tier in high_tier:
        tier_api = f"{kr_api}/lol/league/v4/{tier}leagues/by-queue/{queue}?page={page}&api_key={api_key}"
        
    # 다이아 이하
    else:
        division = "I" * division
        tier_api = f"{kr_api}/lol/league/v4/entries/{queue}/{tier}/{division}?page={page}&api_key={api_key}"
        
    data      = requests.get(tier_api).json()
    league_df = pd.DataFrame(data)
    
    return league_df

def get_summoner_data(api_key, summoner_info, typ="id"):
    """
    소환사에 관한 정보를 가져오는 함수입니다.
    
    api_key      : Riot에서 발급받은 api key
    summoner_info: 소환사의 puuid 또는 name
    typ          : 어떤 인자값을 통해 데이터를 가져올 것인지 정합니다. (id, name)
    """
    if typ == "id":
        summoner_api  = f"{kr_api}/lol/summoner/v4/summoners/{summoner_info}?api_key={api_key}"
    elif typ == "name":
        summoner_api  = f"{kr_api}/lol/summoner/v4/summoners/by-name/{summoner_info}?api_key={api_key}"
    else:
        return False
        
    response      = requests.get(summoner_api)
    summoner_data = response.json()
    
    return summoner_data


def get_matches_by_summoner_puuid(api_key, summoner_puuid, start=0, count=20):
    """
    소환사의 puuid로 match list 가져오는 함수입니다.
    
    api_key       : Riot에서 발급받은 api key
    summoner_puuid: Riot에서 제공한 소환사의 고유 ID
    start         : 가져올 매치의 시작 index
    count         : 가져올 매치의 개수 (max: 0 to 100)
    """
    if count > 100:
        raise Exception("최대 100개까지 가져올 수 있습니다.")
        
    match_list_api = f"{asia_api}/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?start={start}\
    &count={count}&api_key={api_key}"
    response       = requests.get(match_list_api)
    match_list     = response.json()
    
    return match_list

def get_match_by_match_id(api_key, match_id):
    """
    api_key : 발급받은 api key
    match_id: match id
    """
    match_data_api   = f"{asia_api}/lol/match/v5/matches/{match_id}?api_key={api_key}"
    response         = requests.get(match_data_api)
    match_basic_data = response.json()
    
    return match_basic_data

def get_timeline_match_by_match_id(api_key, match_id):
    """
    match_id로 시간별 데이터를 가져오는 함수입니다. 
    
    api_key : Riot에서 발급받은 api key
    match_id: match의 고유 id(KR_5517233316)
    
    """
    timeline_match_api = f"{asia_api}/lol/match/v5/matches/{match_id}/timeline?api_key={api_key}"
    response           = requests.get(timeline_match_api)
    time_match         = response.json()
    
    return time_match


def get_all_champion_data(version="11.19.1"):
    """
    전체 챔피언의 기본 데이터를 가져오는 함수입니다.
    
    version: 패치 버전
    """
    champion_api = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/ko_KR/champion.json"
    response = reuqests.get(champion_api)
    return response.json()