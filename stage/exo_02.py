
episode = ["The new Project", 1, 98, 0]
print(episode[0])
print(episode[2])

title, _, duration, viewed = episode
print(title)
print(duration)

print(viewed)
viewed += 1
print(viewed)
print(episode[3])
episode[3] += 1
print(episode[3])
