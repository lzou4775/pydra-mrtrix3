# Auto-generated test for dwibiascorrect_mtnorm

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwibiascorrect_mtnorm


def test_dwibiascorrect_mtnorm(tmp_path, cli_parse_only):

    task = dwibiascorrect_mtnorm(
        in_file=Nifti1.sample(),
        out_file=ImageFormat.sample(),
        lmax=list([1]),
        grad=File.sample(),
        fslgrad=File.sample(),
        mask=Nifti1.sample(),
        bias=False,
        nocleanup=True,
        scratch=False,
        cont=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored