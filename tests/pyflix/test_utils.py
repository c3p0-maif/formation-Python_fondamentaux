import pytest

from stage.pyflix import utils


def test_episode_viewed_as_bool():
    episode_viewed = ["The new Project", 1, 98, True]
    assert utils.is_viewed(episode_viewed) is True


def test_episode_not_viewed_as_bool():
    episode_not_viewed = ['Installing the softwares', 2, 42, False]
    assert utils.is_viewed(episode_not_viewed) is False


def test_episode_viewed_as_int():
    episode_viewed = ["The new Project", 1, 98, 1]
    assert utils.is_viewed(episode_viewed) is True


def test_episode_not_viewed_as_int():
    episode_not_viewed = ['Installing the softwares', 2, 42, 0]
    assert utils.is_viewed(episode_not_viewed) is False


def test_episode_not_viewed_without_arg():
    episode_not_viewed = ['Installing the softwares', 2, 42]
    assert utils.is_viewed(episode_not_viewed) is False


def test_get_minutes_from_zero():
    assert utils.to_minutes(0) == 0


def test_get_minutes_from_two_hours():
    assert utils.to_minutes(2) == 120


def test_get_minutes_from_string_hours():
    assert utils.to_minutes("20") == 1200


def test_get_minutes_from_two_hours_and_30_minutes():
    assert utils.to_minutes(2, 30) == 150


def test_get_minutes_from_two_hours_and_30_str_minutes():
    assert utils.to_minutes(2, "30") == 150


def test_get_minutes_from_neg_hours():
    with pytest.raises(ValueError):
        utils.to_minutes(-2, 30)


def test_get_minutes_from_neg_minutes():
    with pytest.raises(ValueError, match="minutes doit être positif"):
        utils.to_minutes(2, -30)


def test_get_minutes_with_str():
    with pytest.raises(ValueError, match="invalid literal for int() with base 10"):
        utils.to_minutes("blabla")
