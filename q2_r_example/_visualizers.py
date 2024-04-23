# ----------------------------------------------------------------------------
# Copyright (c) 2024, A QIIME 2 Plugin Developer.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ---------------------------------------------------------------------------

import os
import shutil
import subprocess
import tempfile

import pandas as pd
import pkg_resources


def plot_sorted_samples(output_dir: str, table: pd.DataFrame) -> None:
    with tempfile.TemporaryDirectory() as tempdir:
        input_fp = os.path.join(tempdir, 'input-table.csv')
        visualization_fp = os.path.join(tempdir, 'figure.svg')

        table.reset_index(inplace=True, names='id')
        table.to_csv(input_fp, index=False)

        subprocess.run(['barplot.R', str(input_fp), str(visualization_fp)])

        assets_dir = pkg_resources.resource_filename('q2_r_example', 'assets')
        shutil.copy(os.path.join(assets_dir, 'index.html'), output_dir)
        shutil.copy(visualization_fp, output_dir)
