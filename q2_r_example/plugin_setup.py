# ----------------------------------------------------------------------------
# Copyright (c) 2024, A QIIME 2 Plugin Developer.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Citations, Plugin
from q2_types.feature_table import FeatureTable, Frequency
from q2_r_example import __version__
from q2_r_example._methods import randomize_frequencies
from q2_r_example._visualizers import plot_sorted_samples

citations = Citations.load("citations.bib", package="q2_r_example")

plugin = Plugin(
    name="r-example",
    version=__version__,
    website="https://example.com",
    package="q2_r_example",
    description=(
        "An example QIIME 2 plugin that demonstrates how to wrap software "
        "written in R."
    ),
    short_description="Example plugin.",
    citations=[citations['Caporaso-Bolyen-2024']]
)

plugin.methods.register_function(
    function=randomize_frequencies,
    inputs={'table': FeatureTable[Frequency]},
    parameters={},
    outputs=[('randomized_table', FeatureTable[Frequency])],
    input_descriptions={'table': 'The feature table in which to sum.'},
    parameter_descriptions={},
    output_descriptions={'randomized_table': 'The randomized feature table.'},
    name='Randomize feature frequencies.',
    description=(
        "Sum the features within each sample and assign this sum to each "
        "feature count in that sample."
    ),
    citations=[]
)

plugin.visualizers.register_function(
    function=plot_sorted_samples,
    inputs={'table': FeatureTable[Frequency]},
    parameters={},
    input_descriptions={'table': 'The feature table to use to plot.'},
    parameter_descriptions={},
    name='Plot sorted samples.',
    description=(
        "Plot samples in decreasing order of total sample abundance."
    ),
    citations=[]
)
