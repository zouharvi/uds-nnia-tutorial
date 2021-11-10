#!/usr/bin/env python3

from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
import matplotlib.pyplot as plt
import numpy as np
housing = fetch_california_housing().data
LEGIT_FEATURES = 1
housing = housing[:1000, :LEGIT_FEATURES + 1]
housing[:, 1] = np.random.normal(10, 1, len(housing[:, 0]))

plt.figure(figsize=(5, 4))
plt.scatter(
    [x[0] for x in housing],
    [x[1] for x in housing],
    s=3,
    label="Original data",
)

scaler = StandardScaler().fit(housing)
housing_scaled = scaler.transform(housing)
pca = decomposition.PCA(n_components=1).fit(housing_scaled)
housing_reconstructed = pca.inverse_transform(pca.transform(housing_scaled))
housing_reconstructed = scaler.inverse_transform(housing_reconstructed)

plt.scatter(
    [x[0] for x in housing_reconstructed],
    [x[1] for x in housing_reconstructed],
    s=3,
    label="Reconstructed data",
)

first_coeft = pca.components_[0][0]
components = pca.components_[0] / first_coeft
plt.title(
    f"{LEGIT_FEATURES} legit features (" +
    ",".join([f"{x:.1f}" for x in components]) +
    ")"
)
plt.ylabel("Random variable $\sim N(10, 1)$")
plt.xlabel("Legit variable")
plt.legend()
plt.tight_layout()
plt.show()
