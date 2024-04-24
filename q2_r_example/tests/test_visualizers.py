# ----------------------------------------------------------------------------
# Copyright (c) 2024, A QIIME 2 Plugin Developer.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ---------------------------------------------------------------------------
import os
import tempfile

import pandas as pd

from qiime2.plugin.testing import TestPluginBase
from qiime2 import Artifact

from q2_r_example._visualizers import plot_sorted_samples


class TestVisualizers(TestPluginBase):
    package = 'q2_r_example.tests'

    def setUp(self):
        table_fp = self.get_data_path('table.qza')
        self.table = Artifact.load(table_fp)

    def tearDown(self):
        pass

    def test_plot_sorted_samples(self):
        with tempfile.TemporaryDirectory() as tempdir:
            plot_sorted_samples(tempdir, self.table.view(pd.DataFrame))

            files = os.listdir(tempdir)
            self.assertEqual(set(files), {'index.html', 'figure.svg'})

            self.assertGreater(
                os.path.getsize(os.path.join(tempdir, 'figure.svg')), 0
            )
