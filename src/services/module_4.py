"""
services.module_4 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "services.module_4"
MODULE_INDEX = 4


class ServicesModule4:
    """Stub class for services module 4."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_4() -> ServicesModule4:
    return ServicesModule4()
