"""
db.module_4 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "db.module_4"
MODULE_INDEX = 4


class DbModule4:
    """Stub class for db module 4."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_4() -> DbModule4:
    return DbModule4()
