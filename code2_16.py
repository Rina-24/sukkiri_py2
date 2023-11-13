scores = {"network":60,"database":80,"security":50}
del scores["security"]
print(scores)

score = scores.pop("network")
print(score)
print(scores)

print(list(scores.keys()))
print(scores.values())