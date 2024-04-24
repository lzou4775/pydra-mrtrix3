# Auto-generated by mrtrix3/app.py:print_usage_pydra()

import typing
from pathlib import Path  # noqa: F401
from fileformats.generic import FsObject, File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import Tracks, ImageIn, ImageOut  # noqa: F401
from pydra.engine.task import ShellCommandTask
from pydra.engine import specs

input_fields = [
    (
        "in_file",
        ImageIn,
        {
            "help_string": "The input DWI series",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "out_file",
        Path,
        {
            "help_string": "The output mask image",
            "position": 1,
            "argstr": "",
            "output_file_template": "out_file.mif",
        },
    ),
    (
        "bet_f",
        float,
        {
            "help_string": "Fractional intensity threshold (0->1); smaller values give larger brain outline estimates",
            "argstr": "-bet_f",
        },
    ),
    (
        "bet_g",
        float,
        {
            "help_string": "Vertical gradient in fractional intensity threshold (-1->1); positive values give larger brain outline at bottom, smaller at top",
            "argstr": "-bet_g",
        },
    ),
    (
        "bet_c",
        typing.List[float],
        {
            "help_string": "Centre-of-gravity (voxels not mm) of initial mesh surface",
            "argstr": "-bet_c",
        },
    ),
    (
        "bet_r",
        float,
        {
            "help_string": "Head radius (mm not voxels); initial surface sphere is set to half of this",
            "argstr": "-bet_r",
        },
    ),
    (
        "rescale",
        bool,
        {
            "help_string": "Rescale voxel size provided to BET to 1mm isotropic; can improve results for rodent data",
            "argstr": "-rescale",
        },
    ),
    (
        "grad",
        File,
        {
            "help_string": "Provide the diffusion gradient table in MRtrix format",
            "argstr": "-grad",
        },
    ),
    (
        "fslgrad",
        File,
        {
            "help_string": "Provide the diffusion gradient table in FSL bvecs/bvals format",
            "argstr": "-fslgrad",
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
    ("info", bool, {"help_string": "display information messages.", "argstr": "-info"}),
    (
        "quiet",
        bool,
        {
            "help_string": "do not display information messages or progress status. Alternatively, this can be achieved by setting the MRTRIX_QUIET environment variable to a non-empty string.",
            "argstr": "-quiet",
        },
    ),
    ("debug", bool, {"help_string": "display debugging messages.", "argstr": "-debug"}),
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
]
Dwi2Mask_FslbetInputSpec = specs.SpecInfo(
    name="Dwi2Mask_FslbetInput", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("out_file", ImageOut, {"help_string": "The output mask image"}),
    (
        "scratch",
        Directory,
        {
            "help_string": "manually specify the path in which to generate the scratch directory."
        },
    ),
]
Dwi2Mask_FslbetOutputSpec = specs.SpecInfo(
    name="Dwi2Mask_FslbetOutput", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class Dwi2Mask_Fslbet(ShellCommandTask):
    """
            References
        ----------

        * Smith, S. M. Fast robust automated brain extraction. Human Brain Mapping, 2002, 17, 143-155

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** Warda Syeda (wtsyeda@unimelb.edu.au) and Robert E. Smith (robert.smith@florey.edu.au)

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

    input_spec = Dwi2Mask_FslbetInputSpec
    output_spec = Dwi2Mask_FslbetOutputSpec
    executable = ("dwi2mask", "fslbet")