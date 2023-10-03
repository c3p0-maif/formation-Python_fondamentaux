
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

episode = episode_viewed
# episode = episode_not_viewed

if episode[3]:
    print("l'épisode a été vu")
else:
    print("l'épisode n'a pas été vu")

# avec fonction
from stage import media_utils

if media_utils.is_viewed(episode_viewed):
    print("l'épisode a été vu")
else:
    print("l'épisode n'a pas été vu")

if media_utils.is_viewed(episode_not_viewed):
    print("l'épisode a été vu")
else:
    print("l'épisode n'a pas été vu")
