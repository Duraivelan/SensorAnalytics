#PCA fault detection: T² and SPE 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
sc = StandardScaler().fit(X_good)
pca = PCA(n_components=0.95).fit(sc.transform(X_good))
Z = sc.transform(X_new)
T = pca.transform(Z)
t2 = (T**2 / pca.explained_variance_).sum(axis=1)  # unusual within the model
spe = ((Z - pca.inverse_transform(T))**2).sum(axis=1) # outside the model
