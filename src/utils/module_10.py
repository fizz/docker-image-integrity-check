"""
utils.module_10 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "utils.module_10"
MODULE_INDEX = 10


class UtilsModule10:
    """Stub class for utils module 10."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_10() -> UtilsModule10:
    return UtilsModule10()
