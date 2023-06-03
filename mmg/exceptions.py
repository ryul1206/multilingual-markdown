

class MmgException(Exception):
    """Base exception for all exceptions raised by mmg."""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
