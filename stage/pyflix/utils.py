def is_viewed(episode):
    return bool(episode[3])


def to_minutes(hours, minutes = 0):
    return int(hours) * 60 + int(minutes)
