#XGBoost with lag features
import xgboost as xgb
df["lag1"] = df["y"].shift(1)
df["roll6"] = df["y"].shift(1).rolling(6).mean() df = df.dropna()
X, y = df[["lag1", "roll6", "temp", "flow"]], df["y"]
cut = int(len(df) * 0.8)
m = xgb.XGBRegressor(n_estimators=300, max_depth=4, learning_rate=0.05)
m.fit(X[:cut], y[:cut])
