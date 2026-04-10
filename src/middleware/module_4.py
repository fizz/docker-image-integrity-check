"""
middleware.module_4 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "middleware.module_4"
MODULE_INDEX = 4


class MiddlewareModule4:
    """Stub class for middleware module 4."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_4() -> MiddlewareModule4:
    return MiddlewareModule4()
