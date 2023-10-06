from stage.pyflix.mediatheque import TvShow
import pytest


def test_simple_creation_with_title():
    myshow = TvShow("dr. who")
    assert myshow.name == "Dr. Who"
    assert len(myshow.episodes) == 0


def test_add_first_episode():
    myshow = TvShow("dr. who")
    myshow.add_episode("Rose", 1 ,1, 56, 2006)
    assert len(myshow.episodes) == 1


def test_add_duplicate_episodes():
    myshow = TvShow("dr. who")
    myshow.add_episode("Rose", 1 ,1, 56, 2006)
    myshow.add_episode("Dalek", 2 ,1, 56, 2006)
    assert len(myshow.episodes) == 2
    with pytest.raises(ValueError):
        myshow.add_episode("Rose", 1 ,1, 56, 2006)
