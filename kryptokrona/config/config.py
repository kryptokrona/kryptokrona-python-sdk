class Config:
    """Config definition."""

    decimal_places = 2
    address_prefix = 3914525
    request_timeout = 10 * 1000
    block_target_time = 30
    sync_thread_interval = 10
    daemon_update_interval = 10 * 1000
    locked_transactions_check_interval = 30 * 1000
    blocks_per_tick = 1
    ticker = 'XKR'
    scan_coinbase_transactions = False
    minimum_fee = 10
    fee_per_byte_chunk_size = 256
    minimum_fee_per_byte = 500.00 / fee_per_byte_chunk_size

    standard_address_length = 99
    integrated_address_length = 99 + ((64 * 11) / 8)

    block_store_memory_limit = 1024 * 1024 * 50
    blocks_per_daemon_request = 100
    max_last_fetched_block_interval = 60 * 3
    max_last_updated_network_height_interval = 60 * 3
    max_last_updated_local_height_interval = 60 * 3

    custom_user_agent_string = '%s-sdk-%s'.format(ticker, '1.0.0')
    custom_request_options = {}

    def __init__(self):
        pass
