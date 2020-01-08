## opsdroid / skill-prometheus-scrape
Skill to scrape prometheus metrics over chat. This repo has a "skill" for opsdroid, an open source chat-ops bot framework: https://opsdroid.dev.

#### Install:
##### **Using this skill directly:**
```
$ git clone https://github.com/codexlynx/opsdroid-skill-prometheus-scrape.git
$ cd opsdroid-skill-prometheus-scrape
$ vim configuration.sample.yaml
```
Add your connector configuration and save as `configuration.yaml`. https://docs.opsdroid.dev/en/stable/connectors/index.html
```
$ docker-compose up
```

##### **Install this skill in your current opsdroid instance:**
For more information visit: https://docs.opsdroid.dev/en/stable/configuration.html#module-options

```
skills:
  - name: prometheus-scrape
    repo: https://github.com/codexlynx/opsdroid-skill-prometheus-scrape.git
    targets:
      - http://node-exporter:9100/metrics
    metrics:
      - node_uname_info
      - node_load5
      - node_filesystem_avail_bytes
      - node_memory_MemFree_bytes
      - node_disk_io_time_weighted_seconds_total
```
