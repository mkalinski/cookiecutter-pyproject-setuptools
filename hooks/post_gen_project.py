from pathlib import Path
import subprocess
import venv


INSTALL_IMMEDIATELY = "{{ cookiecutter.install_immediately }}" == "yes"
IS_PYMODULE = "{{ cookiecutter.project_type }}" == "module"
HAS_MYPY = "{{ cookiecutter.include_mypy }}" == "yes"
SRC_DIR = Path("src")


def install_immediately():
    venv.create("venv", with_pip=True)
    subprocess.run(
        ". venv/bin/activate && pip install -e '.[dev]'",
        shell=True,
        check=True,
    )


def create_py_module():
    SRC_DIR.joinpath("{{ cookiecutter.python_src_root }}.py").touch()


def create_package():
    pkg_path = SRC_DIR / "{{ cookiecutter.python_src_root }}"
    pkg_path.mkdir()
    pkg_path.joinpath("__init__.py").touch()

    if HAS_MYPY:
        pkg_path.joinpath("py.typed").touch()


if __name__ == '__main__':
    SRC_DIR.mkdir()

    if IS_PYMODULE:
        create_py_module()
    else:
        create_package()

    if INSTALL_IMMEDIATELY:
        install_immediately()
