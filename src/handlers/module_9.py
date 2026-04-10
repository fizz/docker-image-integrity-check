"""
handlers.module_9 — stub file to bulk up the build context.

Part of the repro for buildx GHA cache stale COPY bug.
"""
from typing import Optional

MODULE_NAME = "handlers.module_9"
MODULE_INDEX = 9


class HandlersModule9:
    """Stub class for handlers module 9."""

    def __init__(self, name: Optional[str] = None):
        self.name = name or MODULE_NAME
        self.index = MODULE_INDEX

    def describe(self) -> str:
        return f"{self.name}#{self.index}"


def get_module_9() -> HandlersModule9:
    return HandlersModule9()
