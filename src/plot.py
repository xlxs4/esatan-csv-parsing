import matplotlib.pyplot as plt
import seaborn as sns


def setup_plots():
    sns.set_style("whitegrid")


def lineplot(df, measurement_kinds, element_ids, dims=(15, 8)):
    same_kinds = all(x == measurement_kinds[0] for x in measurement_kinds)
    if same_kinds:
        plt.figure(figsize=dims)

    for idx, (t_col, val_col) in enumerate(zip(df.columns[::2], df.columns[1::2])):
        if not same_kinds:
            plt.figure(figsize=dims)

        sns.lineplot(
            x=t_col,
            y=val_col,
            data=df[[t_col, val_col]],
            label=f"{measurement_kinds[idx]} of element {element_ids[idx]}",
        )
        if not same_kinds:
            plt.show()

    if same_kinds:
        plt.show()
