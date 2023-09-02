import matplotlib.pyplot as plt
import seaborn as sns


def setup_plots():
    sns.set_style("whitegrid")


def lineplot(df, measurement_kinds, element_ids, dims=(15, 8)):
    plt.figure(figsize=dims)
    for idx, (t_col, val_col) in enumerate(zip(df.columns[::2], df.columns[1::2])):
        sns.lineplot(
            x=t_col,
            y=val_col,
            data=df[[t_col, val_col]],
            label=f"{measurement_kinds[idx]} of element {element_ids[idx]}",
        )
    plt.show()
