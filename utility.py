
#Simple utility functions for data preprocessing

#convert percent to float
def p2f(x):
    return float(x.strip('%'))/100

#convert percent to int
def percent_to_int(df_in):
    for col in df_in.columns.values:
        if col.startswith("Percentage") or col.endswith("%") or col.startswith('Percent') or col.endswith("Rate"):
            df_in[col] = df_in[col].astype(np.object).str.replace('%', '').astype(float)
    return df_in
