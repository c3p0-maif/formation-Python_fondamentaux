def is_viewed(episode):
    return len(episode) > 3 and bool(episode[3])


def to_minutes(hours, minutes=0):
    hours = int(hours)
    minutes = int(minutes)

    if hours < 0:
        raise ValueError("hours doit être positif")
    if minutes < 0:
        raise ValueError("minutes doit être positif")
    return hours * 60 + minutes
