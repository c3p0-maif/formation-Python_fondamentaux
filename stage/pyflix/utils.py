def is_viewed(episode):
    return len(episode) > 3 and bool(episode[3])


def to_minutes(hours: int, minutes: int = 0):
    """
    Converts a number of hours and minutes to a total of minutes.

    Loram Ipsum

    :param hours: Number of hours, must be positive or null
    :param minutes: Number of minutes, must be positive or null
    :raises ValueError: when a value is negative
    :return: Total number of minutes
    """
    hours = int(hours)
    minutes = int(minutes)

    if hours < 0:
        raise ValueError("hours doit être positif")
    if minutes < 0:
        raise ValueError("minutes doit être positif")
    return hours * 60 + minutes
