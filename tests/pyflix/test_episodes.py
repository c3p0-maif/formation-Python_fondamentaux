from stage.exo_dict import is_viewed
from stage.bbt import get_playlist_from


def test_episode_viewed():
    episode_viewed = {"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
    assert is_viewed(episode_viewed) is True


def test_episode_not_viewed():
    episode_not_viewed_1 = {"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
    assert is_viewed(episode_not_viewed_1) is False


def test_episode_without_viewed():
    episode_not_viewed_2 = {"title": "The Conjugal Configuration", "duration": 20}
    assert is_viewed(episode_not_viewed_2) is False


def test_get_playlist_from_emptylist():
    season = []
    assert len(get_playlist_from(season)) == 0


def test_get_playlist_from_seenlist():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration', 'viewed': True},
              {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': True}]
    assert len(get_playlist_from(season)) == 0


def test_get_playlist_from_unseenlist():
    season = [{'duration': 20, 'title': 'The Conjugal Configuration'},
              {'duration': 21, 'title': 'The Wedding Gift Wormhole', 'viewed': False}]
    assert season == get_playlist_from(season)
