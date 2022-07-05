class MixinLimit:
    """MixinLimit definition."""

    height = 0
    min_mixin = 0
    max_mixin = 0
    default_mixin = 0

    def __init__(self, height, min_mixin, max_mixin=None, default_mixin=None):
        self.height = height
        self.min_mixin = min_mixin
        self.max_mixin = max_mixin if max_mixin is None else min_mixin
        self.default_mixin = default_mixin if default_mixin is None else min_mixin
