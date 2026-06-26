class Application:
    """Application for updating README.md"""

    @classmethod
    def run(cls) -> int:
        return cls()._run()

    def __init__(self) -> None:
        pass

    # private

    def _run(self) -> int:
        return 0
