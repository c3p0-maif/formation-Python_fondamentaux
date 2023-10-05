import pylib.templating as tp
import pylib.datasource as ds
import stage.pyflix.utils as utils
from stage.exo_dict import is_viewed


def print_episodes_duration(template: str, list_ep: list, episode_duration: int):
    total_duration = episode_duration * len(list_ep)
    print(template.format(*divmod(total_duration, 60)))


def get_playlist(list_ep: list, d_max: int, episode_duration: int) -> list:
    e_max = d_max // episode_duration
    return list_ep[:e_max]


def get_playlist_from(season: list) -> list:
    for first_unseen_idx, episode in enumerate(season):
        if not is_viewed(episode):
            return season[first_unseen_idx:]
    return []


if __name__ == "__main__":
    episodes = 7
    EPISODE_DURATION = 23
    total_minutes_tosee = episodes*EPISODE_DURATION

    episodes_hours = total_minutes_tosee // 60
    episodes_minutes = total_minutes_tosee % 60
    print(tp.TIME_REMAINING.format(episodes_hours, episodes_minutes))

    start_minutes = utils.to_minutes(*ds.get_start_time().split('h'))
    total_minutes = start_minutes + total_minutes_tosee
    print(tp.END_HOUR.format(*divmod(total_minutes, 60)))

    bbt_s12 = ds.get_season("me")
    from pprint import pprint
    pprint(bbt_s12)

    pprint(get_playlist(bbt_s12, 120, EPISODE_DURATION))

    print("Exo 15")
    playlist = get_playlist_from(bbt_s12)

    total_minutes = 0
    while playlist and "duration" in playlist[0] and total_minutes + playlist[0]["duration"] < 120:
        episode = playlist.pop(0)
        episode["viewed"] = True
        total_minutes += episode["duration"]
        print(episode["title"])

    pprint(bbt_s12)
