"""
common.module_6 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "common.module_6"
MODULE_INDEX = 6


class CommonModule6:
    """Stub class for common module 6."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_6() -> CommonModule6:
    return CommonModule6()
