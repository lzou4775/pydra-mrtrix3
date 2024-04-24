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
            "help_string": """the input image.""",
            "mandatory": True,
        },
    ),
    (
        "out_file",
        Path,
        {
            "argstr": "",
            "position": 1,
            "output_file_template": "out_file.txt",
            "help_string": """the output mesh file.""",
        },
    ),
    (
        "blocky",
        bool,
        {
            "argstr": "-blocky",
            "help_string": """generate a 'blocky' mesh that precisely represents the voxel edges""",
        },
    ),
    (
        "threshold",
        float,
        {
            "argstr": "-threshold",
            "help_string": """manually set the intensity threshold for the Marching Cubes algorithm""",
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

Voxel2MeshInputSpec = specs.SpecInfo(
    name="Voxel2MeshInput", fields=input_fields, bases=(specs.ShellSpec,)
)


output_fields = [
    (
        "out_file",
        File,
        {
            "help_string": """the output mesh file.""",
        },
    ),
]
Voxel2MeshOutputSpec = specs.SpecInfo(
    name="Voxel2MeshOutput", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class Voxel2Mesh(ShellCommandTask):
    """This command utilises the Marching Cubes algorithm to generate a polygonal surface that represents the isocontour(s) of the input image at a particular intensity. By default, an appropriate threshold will be determined automatically from the input image, however the intensity value of the isocontour(s) can instead be set manually using the -threhsold option.

        If the -blocky option is used, then the Marching Cubes algorithm will not be used. Instead, the input image will be interpreted as a binary mask image, and polygonal surfaces will be generated at the outer faces of the voxel clusters within the mask.


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

    executable = "voxel2mesh"
    input_spec = Voxel2MeshInputSpec
    output_spec = Voxel2MeshOutputSpec
