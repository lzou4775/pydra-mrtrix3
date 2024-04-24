# Auto-generated by mrtrix3/app.py:print_usage_pydra()

import typing
from pathlib import Path  # noqa: F401
from fileformats.generic import FsObject, File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import Tracks, ImageIn, ImageOut  # noqa: F401
from pydra.engine.task import ShellCommandTask
from pydra.engine import specs

input_fields = [
    (
        "inputs",
        File,
        {
            "help_string": "The input response function files",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "The output mean response function file",
            "position": 1,
            "argstr": "",
            "output_file_template": "out_file.txt",
        },
    ),
    (
        "nocleanup",
        bool,
        {
            "help_string": "do not delete intermediate files during script execution, and do not delete scratch directory at script completion.",
            "argstr": "-nocleanup",
        },
    ),
    (
        "scratch",
        typing.Union[Path, bool],
        False,
        {
            "help_string": "manually specify the path in which to generate the scratch directory.",
            "argstr": "-scratch",
            "output_file_template": "scratch",
        },
    ),
    (
        "cont",
        typing.Any,
        {
            "help_string": "continue the script from a previous execution; must provide the scratch directory path, and the name of the last successfully-generated file.",
            "argstr": "-cont",
        },
    ),
    (
        "info",
        bool,
        {
            "help_string": "display information messages.",
            "argstr": "-info",
            "xor": ("info", "quiet", "debug"),
        },
    ),
    (
        "quiet",
        bool,
        {
            "help_string": "do not display information messages or progress status. Alternatively, this can be achieved by setting the MRTRIX_QUIET environment variable to a non-empty string.",
            "argstr": "-quiet",
            "xor": ("info", "quiet", "debug"),
        },
    ),
    (
        "debug",
        bool,
        {
            "help_string": "display debugging messages.",
            "argstr": "-debug",
            "xor": ("info", "quiet", "debug"),
        },
    ),
    (
        "force",
        bool,
        {"help_string": "force overwrite of output files.", "argstr": "-force"},
    ),
    (
        "nthreads",
        int,
        {
            "help_string": "use this number of threads in multi-threaded applications (set to 0 to disable multi-threading).",
            "argstr": "-nthreads",
        },
    ),
    (
        "config",
        specs.MultiInputObj[str],
        {
            "help_string": "temporarily set the value of an MRtrix config file entry.",
            "argstr": "-config",
        },
    ),
    (
        "help",
        bool,
        {"help_string": "display this information page and exit.", "argstr": "-help"},
    ),
    (
        "version",
        bool,
        {"help_string": "display version information and exit.", "argstr": "-version"},
    ),
    (
        "legacy",
        bool,
        {
            "help_string": 'Use the legacy behaviour of former command "average_response": average response function coefficients directly, without compensating for global magnitude differences between input files',
            "argstr": "-legacy",
        },
    ),
]
ResponseMeanInputSpec = specs.SpecInfo(
    name="ResponseMeanInput", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("out_file", File, {"help_string": "The output mean response function file"}),
    (
        "scratch",
        Directory,
        {
            "help_string": "manually specify the path in which to generate the scratch directory."
        },
    ),
]
ResponseMeanOutputSpec = specs.SpecInfo(
    name="ResponseMeanOutput", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class ResponseMean(ShellCommandTask):
    """
            References
        ----------

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** Robert E. Smith (robert.smith@florey.edu.au) and David Raffelt (david.raffelt@florey.edu.au)

        **Copyright:** Copyright (c) 2008-2024 the MRtrix3 contributors.

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

    Covered Software is provided under this License on an "as is"
    basis, without warranty of any kind, either expressed, implied, or
    statutory, including, without limitation, warranties that the
    Covered Software is free of defects, merchantable, fit for a
    particular purpose or non-infringing.
    See the Mozilla Public License v. 2.0 for more details.

    For more details, see http://www.mrtrix.org/.

    """

    input_spec = ResponseMeanInputSpec
    output_spec = ResponseMeanOutputSpec
    executable = "responsemean"