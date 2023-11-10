# Agent Check: EMQX

## Overview

This check monitors [EMQX][1] through the Datadog Agent in order to:

- Collect metrics from EMQX nodes.
- Visualize EMQX performance on the provided dashboard.

### Installation

First, [download and launch the Datadog Agent][8].

Then, manually install the TiDB check. [Instructions vary depending on the environment][10].

Run `datadog-agent integration install -t datadog-emqx==<INTEGRATION_VERSION>`.

### Configuration

1. Edit the `emqx/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your HikariCP performance data.
   
2. [Restart the Agent][5].

### Validation

[Run the Agent's status subcommand][6] and look for `emqx` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][7] for a list of metrics provided by this integration.

### Service Checks

See [service_checks.json][11] for a list of service checks provided by this integration.

### Events

EMQX does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][9].

[1]: https://github.com/emqx/emqx
[2]: https://app.datadoghq.com/account/settings/agent/latest
[3]: https://docs.datadoghq.com/agent/kubernetes/integrations/
[4]: https://github.com/DataDog/integrations-extras/blob/master/hikaricp/datadog_checks/hikaricp/data/conf.yaml.example
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[6]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[7]: https://github.com/DataDog/integrations-extras/blob/master/emqx/metadata.csv
[8]: https://github.com/DataDog/integrations-extras/blob/master/emqx/assets/service_checks.json
[9]: https://docs.datadoghq.com/help/
[10]: https://docs.datadoghq.com/developers/integrations/python/
[11]: https://github.com/DataDog/integrations-extras/blob/master/emqx/assets/service_checks.json
