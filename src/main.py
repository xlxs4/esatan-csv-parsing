import parse
import plot
import IOutils


if __name__ == "__main__":
    CONFIG = IOutils.read_config("config.toml")
    meta_row_idx, meta_map = parse.parse_csv_meta(CONFIG.filename)
    df = parse.read_csv(CONFIG.filename, meta_row_idx)
    plot.setup_plots()
    plot.lineplot(df, meta_map["Measurement Kind"], meta_map["Element"])
