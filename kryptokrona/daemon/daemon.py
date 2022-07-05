class Daemon:
    """Daemon definition."""

    def __init__(self, hostname, port, ssl=False, use_raw_blocks=False):
        self.hostname = hostname
        self.port = port
        self.ssl = ssl
        self.use_raw_blocks = use_raw_blocks
