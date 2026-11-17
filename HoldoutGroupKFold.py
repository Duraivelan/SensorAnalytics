#Hold out a whole chamber
from sklearn.model_selection import GroupKFold
cv = GroupKFold(n_splits=4)
for tr, te in cv.split(X, y, groups=chamber_id): model.fit(X[tr], y[tr])
print(model.score(X[te], y[te]))
