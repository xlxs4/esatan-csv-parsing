import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


parse = lambda x: x.rstrip().split(",")[1::2]

meta_map = {"Data Source": None, "Element": None, "Time": None}

with open("attribute.csv", "r") as f:
    for idx, line in enumerate(f):
        for key in meta_map.keys():
            if line.startswith(key):
                meta_map[key] = parse(line)
        if all(meta_map.values()):
            val_row = idx
            break

meta_map["Measurement Kind"] = meta_map.pop("Time")

df = pd.read_csv("attribute.csv", skiprows=val_row)

sns.set_style("whitegrid")
plt.figure(figsize=(15, 8))

for idx, (t_col, val_col) in enumerate(zip(df.columns[::2], df.columns[1::2])):
    sns.lineplot(
        x=t_col,
        y=val_col,
        data=df[[t_col, val_col]],
        label=f"{meta_map['Measurement Kind'][idx]} of element {meta_map['Element'][idx]}",
    )

plt.show()
