
episode_viewed = ["The new Project", 1, 98, 1]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

episode = episode_viewed
# episode = episode_not_viewed

if episode[3] > 0:
    print("l'épisode a été vu")
else:
    print("l'épisode n'a pas été vu")

if episode[3]:
    print("l'épisode a été vu")
else:
    print("l'épisode n'a pas été vu")

# avec fonction
import stage.media_utils as utils

if utils.is_viewed(episode_viewed):
    print("l'épisode a été vu")
else:
    print("l'épisode n'a pas été vu")

if utils.is_viewed(episode_not_viewed):
    print("l'épisode a été vu")
else:
    print("l'épisode n'a pas été vu")
