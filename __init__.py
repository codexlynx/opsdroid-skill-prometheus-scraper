from prometheus_client.parser import text_string_to_metric_families
from opsdroid.skill import Skill
from opsdroid.matchers import match_parse
import requests


class PrometheusScraperSkill(Skill):

    def get_metrics(self, target):
        defined_metrics = self.config.get('metrics', False)
        req = requests.get(target)
        for family in text_string_to_metric_families(req.text):
            for sample in family.samples:
                if not defined_metrics:
                    yield sample
                elif sample[0] in defined_metrics:
                    yield sample

    @match_parse('/metrics')
    async def metrics(self, message):
        targets = self.config['targets']
        for target in targets:
            for metric in self.get_metrics(target):
                msg = 'Name: %s\n' % metric[0]
                if metric[1] != {}:
                    msg += 'Labels:\n'
                    for label in metric[1].keys():
                        msg += '  %s: %s\n' % (label, metric[1][label])
                msg += 'Value: %s' % metric[2]
                await message.respond(msg)
