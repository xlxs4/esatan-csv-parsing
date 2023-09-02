from IOutils import read_config
from parse import read_csv, read_csv_meta
from plot import lineplot, setup_plots

if __name__ == "__main__":
    CONFIG = read_config("config.toml")
    meta_row_idx, meta_map = read_csv_meta(CONFIG.filename)
    df = read_csv(CONFIG.filename, meta_row_idx)
    setup_plots()
    lineplot(df, meta_map["Measurement Kind"], meta_map["Element"])
