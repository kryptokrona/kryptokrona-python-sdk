class Config:
    """Starting point of application."""

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
    minimum_Fee_Per_Byte = 500.00 / fee_per_byte_chunk_size

    standardAddressLength = 99
    integratedAddressLength = 99 + ((64 * 11) / 8)

    blockStoreMemoryLimit = 1024 * 1024 * 50
    blocksPerDaemonRequest = 100
    maxLastFetchedBlockInterval = 60 * 3
    maxLastUpdatedNetworkHeightInterval = 60 * 3
    maxLastUpdatedLocalHeightInterval = 60 * 3

    customUserAgentString = ''
    customRequestOptions = {}

    def __init__(self):
        pass
