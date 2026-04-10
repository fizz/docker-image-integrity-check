"""
utils.module_7 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "utils.module_7"
MODULE_INDEX = 7


class UtilsModule7:
    """Stub class for utils module 7."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_7() -> UtilsModule7:
    return UtilsModule7()
