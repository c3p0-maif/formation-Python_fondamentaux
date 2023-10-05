def is_viewed(episode: dict):
    return "viewed" in episode and bool(episode["viewed"])


def is_viewed_2(episode: dict):
    return bool(episode.get("viewed", False))


if __name__ == "__main__":
    episode_viewed = {"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
    episode_not_viewed_1 = {"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
    episode_not_viewed_2 = {"title": "The Conjugal Configuration", "duration": 20}

    print(episode_not_viewed_1["title"])
    episode_not_viewed_1["viewed"] = True
    print(episode_not_viewed_1["viewed"])

    print(f"{episode_viewed=} => {is_viewed(episode_viewed)}")
    print(f"{episode_not_viewed_1=} => {is_viewed(episode_not_viewed_1)}")
    print(f"{episode_not_viewed_2=} => {is_viewed(episode_not_viewed_2)}")

