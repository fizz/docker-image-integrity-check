"""
api.module_1 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "api.module_1"
MODULE_INDEX = 1


class ApiModule1:
    """Stub class for api module 1."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_1() -> ApiModule1:
    return ApiModule1()
