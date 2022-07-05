class Daemon:
    """Daemon definition."""

    def __init__(self, hostname, port, ssl=False, use_raw_blocks=False):
        self.hostname = hostname
        self.port = port
        self.ssl = ssl
        self.use_raw_blocks = use_raw_blocks

    async def init(self):
        pass

    async def update_daemon_info(self):
        pass

    def get_node_fee(self):
        pass

    async def get_wallet_sync_data(self, block_hash_checkpoints, start_height, start_timestamp):
        pass

    async def get_global_indexes_for_range(self, start_height, end_height):
        pass

    async def get_cancelled_transactions(self, transaction_hashes):
        pass

    async def get_random_outputs_by_amount(self, amounts, requested_outs):
        pass

    async def send_transaction(self, raw_transaction):
        pass

    def get_connection_info(self):
        pass

    def get_connection_string(self):
        pass

    async def raw_blocks_to_blocks(self, raw_blocks):
        pass

    async def update_fee_info(self):
        pass

    async def make_post_request(self, endpoint):
        pass

    async def make_get_request(self, endpoint, body):
        pass

    async def make_request(self, endpoint, method, body=None):
        pass
