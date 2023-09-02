from IOutils import read_config
from parse import read_csv, read_csv_meta
from paths import get_path
from plot import lineplot, setup_plots

if __name__ == "__main__":
    RELATIVE_PATHS = True
    CONFIG = read_config(get_path("config", RELATIVE_PATHS))
    meta_row_idx, meta_map = read_csv_meta(CONFIG.filename)
    df = read_csv(CONFIG.filename, meta_row_idx)
    setup_plots()
    lineplot(
        df, meta_map["Data Source"], meta_map["Element"], meta_map["Measurement Kind"]
    )
