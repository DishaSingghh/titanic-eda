# NumPy

Core array operations practiced here before applying them inside Pandas and for building ML models from scratch.

| File | What it covers |
|---|---|
| `arraycreation.py` | np.array, zeros, ones, arange, linspace — when to use each |
| `reshape_index_slicing.py` | indexing, slicing, boolean masking, reshape, flatten |
| `o_agg_norm.py` | vectorized ops, broadcasting, axis=0/1, standardization |

The normalization formula in `o_agg_norm.py` — `(data - mean) / std` — is the same one used in every ML preprocessing pipeline. Writing it manually first makes sklearn's `StandardScaler` make sense later.
