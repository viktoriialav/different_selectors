from pathlib import Path

import diff_selectors


def abs_path_from_root(path):
    return Path(diff_selectors.__file__).parent.parent.joinpath(path).absolute().__str__()
