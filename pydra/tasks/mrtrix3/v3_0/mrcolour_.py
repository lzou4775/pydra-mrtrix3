# Auto-generated from MRtrix C++ command with '__print_usage_pydra__' secret option

import typing as ty
from pathlib import Path  # noqa: F401
from fileformats.generic import File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import ImageIn, ImageOut, Tracks  # noqa: F401
from pydra.engine import specs, ShellCommandTask


input_fields = [
    # Arguments
    (
        "in_file",
        ImageIn,
        {
            "argstr": "",
            "position": 0,
            "help_string": """the input image""",
            "mandatory": True,
        },
    ),
    (
        "map",
        str,
        {
            "argstr": "",
            "position": 1,
            "help_string": """the colourmap to apply; choices are: gray,hot,cool,jet,inferno,viridis,pet,colour,rgb""",
            "mandatory": True,
            "allowed_values": [
                "gray",
                "gray",
                "hot",
                "cool",
                "jet",
                "inferno",
                "viridis",
                "pet",
                "colour",
                "rgb",
            ],
        },
    ),
    (
        "out_file",
        Path,
        {
            "argstr": "",
            "position": 2,
            "output_file_template": "out_file.mif",
            "help_string": """the output image""",
        },
    ),
    (
        "upper",
        float,
        {
            "argstr": "-upper",
            "help_string": """manually set the upper intensity of the colour mapping""",
        },
    ),
    (
        "lower",
        float,
        {
            "argstr": "-lower",
            "help_string": """manually set the lower intensity of the colour mapping""",
        },
    ),
    (
        "colour",
        ty.List[float],
        {
            "argstr": "-colour",
            "help_string": """set the target colour for use of the 'colour' map (three comma-separated floating-point values)""",
            "sep": ",",
        },
    ),
    # Standard options
    (
        "info",
        bool,
        {
            "argstr": "-info",
            "help_string": """display information messages.""",
        },
    ),
    (
        "quiet",
        bool,
        {
            "argstr": "-quiet",
            "help_string": """do not display information messages or progress status; alternatively, this can be achieved by setting the MRTRIX_QUIET environment variable to a non-empty string.""",
        },
    ),
    (
        "debug",
        bool,
        {
            "argstr": "-debug",
            "help_string": """display debugging messages.""",
        },
    ),
    (
        "force",
        bool,
        {
            "argstr": "-force",
            "help_string": """force overwrite of output files (caution: using the same file as input and output might cause unexpected behaviour).""",
        },
    ),
    (
        "nthreads",
        int,
        {
            "argstr": "-nthreads",
            "help_string": """use this number of threads in multi-threaded applications (set to 0 to disable multi-threading).""",
        },
    ),
    (
        "config",
        specs.MultiInputObj[ty.Tuple[str, str]],
        {
            "argstr": "-config",
            "help_string": """temporarily set the value of an MRtrix config file entry.""",
        },
    ),
    (
        "help",
        bool,
        {
            "argstr": "-help",
            "help_string": """display this information page and exit.""",
        },
    ),
    (
        "version",
        bool,
        {
            "argstr": "-version",
            "help_string": """display version information and exit.""",
        },
    ),
]

MrColourInputSpec = specs.SpecInfo(
    name="MrColourInput", fields=input_fields, bases=(specs.ShellSpec,)
)


output_fields = [
    (
        "out_file",
        ImageOut,
        {
            "help_string": """the output image""",
        },
    ),
]
MrColourOutputSpec = specs.SpecInfo(
    name="MrColourOutput", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class MrColour(ShellCommandTask):
    """Under typical usage, this command will receive as input ad 3D greyscale image, and output a 4D image with 3 volumes corresponding to red-green-blue components; other use cases are possible, and are described in more detail below.

        By default, the command will automatically determine the maximum and minimum intensities of the input image, and use that information to set the upper and lower bounds of the applied colourmap. This behaviour can be overridden by manually specifying these bounds using the -upper and -lower options respectively.


        References
        ----------

            Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137


        MRtrix
        ------

            Version:3.0.4-864-gfc46d305, built Apr 11 2024

            Author: Robert E. Smith (robert.smith@florey.edu.au)

            Copyright: Copyright (c) 2008-2024 the MRtrix3 contributors.

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

    executable = "mrcolour"
    input_spec = MrColourInputSpec
    output_spec = MrColourOutputSpec