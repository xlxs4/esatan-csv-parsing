import matplotlib.pyplot as plt
import seaborn as sns


def setup_plots():
    sns.set_style("whitegrid")


def lineplot(df, data_sources, element_ids, measurement_kinds, dims=(15, 8)):
    same = lambda xs: all(x == xs[0] for x in xs)
    same_sources = same(data_sources)
    title = f"{data_sources[0]}" if same_sources else f"{', '.join(data_sources)}"
    same_kinds = same(measurement_kinds)
    if same_kinds:
        plt.figure(figsize=dims)
        plt.title(title)

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
            plt.title(title)
            plt.show()

    if same_kinds:
        plt.show()
