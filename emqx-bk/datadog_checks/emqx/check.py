from datadog_checks.base import OpenMetricsBaseCheckV2
from datadog_checks.base import ConfigurationError

from .config_models import ConfigMixin
from .metrics import METRIC_MAP


class EmqxCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = "emqx"

    DEFAULT_METRIC_LIMIT = 0

    def __init__(self, name, init_config, instances):

        super(EmqxCheck, self).__init__(name, init_config, instances)
        self.openmetrics_endpoint = self.instance.get('openmetrics_endpoint')

    def get_default_config(self):
        default_config = {
            'openmetrics_endpoint': self.openmetrics_endpoint,
            'metrics': METRIC_MAP,
            'namespace': self.__NAMESPACE__,
        }

        return default_config

    def check(self, instance):
        endpoint = instance.get('openmetrics_endpoint')
        if endpoint is None:
            raise ConfigurationError("Unable to find openmetrics_endpoint in config file.")
        super().check(instance)
