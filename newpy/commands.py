from distutils.dir_util import copy_tree
from pathlib import Path

import click

from newpy.common import SAVE_FILE, TEMPLATE_PATH


def set_template_directory(path: Path):
    with open(SAVE_FILE, "w") as f:
        f.write(str(path.absolute()))


def spawn_template(template: Path, new_path: Path):
    src = TEMPLATE_PATH / template
    dst = new_path / template
    if not new_path.exists():
        new_path.mkdir()
        dst = new_path
    print(src, dst.absolute())
    copy_tree(str(src), str(dst))


@click.command(name="")
@click.option(
    "--set-template-dir",
    is_flag=False,
    flag_value="",
    help="Set your template directory",
)
@click.option(
    "--spawn",
    "-s",
    is_flag=False,
    flag_value="",
    help="Spawn your template",
)
@click.option(
    "--direc",
    "-d",
    is_flag=False,
    flag_value=".",
    help="Specify the directory to spawn in",
)
def main(set_template_dir: None | str, spawn: None | str, direc: None | str):
    if set_template_dir:
        set_template_directory(Path(set_template_dir))

    if spawn:
        if direc is None:
            direc = "."
        spawn_template(Path(spawn), Path(direc))
