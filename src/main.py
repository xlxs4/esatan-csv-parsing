import parse
import plot


if __name__ == "__main__":
    filename = "../attribute.csv"
    meta_row_idx, meta_map = parse.parse_csv_meta(filename)
    df = parse.read_csv(filename, meta_row_idx)
    plot.setup_plots()
    plot.lineplot(df, meta_map["Measurement Kind"], meta_map["Element"])
