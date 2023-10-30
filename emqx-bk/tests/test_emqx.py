import pytest

from typing import Any, Dict  # noqa: F401
import logging

from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401
from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.emqx import EmqxCheck



EXPECTED_METRICS = {
    "fluxcd.gotk.reconcile.condition",
    "fluxcd.gotk.suspend.status",
    "fluxcd.gotk.reconcile.duration.seconds.count",
    "fluxcd.gotk.reconcile.duration.seconds.sum",
    "fluxcd.gotk.reconcile.duration.seconds.bucket",
    "fluxcd.controller.runtime.active.workers",
    "fluxcd.controller.runtime.reconcile.count",
    "fluxcd.controller.runtime.reconcile.time.seconds.count",
    "fluxcd.controller.runtime.reconcile.time.seconds.sum",
    "fluxcd.controller.runtime.reconcile.time.seconds.bucket",
    "fluxcd.controller.runtime.max.concurrent.reconciles",
    "fluxcd.controller.runtime.reconcile.errors.count",
}
@pytest.mark.usefixtures('dd_environment')
def test_check(aggregator, instance):
    # type: (AggregatorStub, Dict[str, Any]) -> None
    check = EmqxCheck('emqx', {}, [instance])
    check.check(instance)
    logging.error("zhongwen1")
    logging.error(get_metadata_metrics())
    logging.error("zhongwen2")
    for metric in get_metadata_metrics():
        logging.error("name: %s", metric)
    #for metric_name in EXPECTED_METRICS:
    #    aggregator.assert_metric(metric_name)
    aggregator.assert_metric('emqx.connections.count')
    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())
