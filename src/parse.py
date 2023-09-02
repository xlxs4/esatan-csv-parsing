from pathlib import Path

import pandas as pd

from eltypes import data, meta


def read_csv_meta(filename: Path) -> meta:
    parse = lambda x: x.rstrip().split(",")[1::2]
    meta_map = {"Data Source": None, "Element": None, "Time": None}
    with open(filename, "r") as f:
        for idx, line in enumerate(f):
            for key in meta_map.keys():
                if line.startswith(key):
                    meta_map[key] = parse(line)

            if all(meta_map.values()):
                meta_row_idx = idx
                break

    meta_map["Measurement Kind"] = meta_map.pop("Time")
    meta_map["Data Source"] = [
        ds.split(" : TMD : ")[0] for ds in meta_map["Data Source"]
    ]
    return meta_row_idx, meta_map


def read_csv(filename: Path, meta_row_idx: int) -> data:
    return pd.read_csv(filename, skiprows=meta_row_idx)
