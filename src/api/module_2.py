"""
api.module_2 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "api.module_2"
MODULE_INDEX = 2


class ApiModule2:
    """Stub class for api module 2."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_2() -> ApiModule2:
    return ApiModule2()
