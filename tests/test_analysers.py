import pytest

from warcraftlogs.analysers import VashjAnalyser


class TestVashjAnalyser:
    @pytest.fixture
    def vashj_analyser(self):
        return VashjAnalyser(None, None)

    @pytest.fixture
    def empty_events_list(self):
        return []

    @pytest.fixture
    def tainted_core_debuff_events_all_lost(self):
        return [{'timestamp': 8206418, 'type': 'applydebuff', 'sourceID': 19, 'targetID': 19, 'abilityGameID': 38132},
                {'timestamp': 8206599, 'type': 'removedebuff', 'sourceID': 19, 'targetID': 19, 'abilityGameID': 38132},
                {'timestamp': 8271501, 'type': 'applydebuff', 'sourceID': 11, 'targetID': 11, 'abilityGameID': 38132},
                {'timestamp': 8284360, 'type': 'removedebuff', 'sourceID': 11, 'targetID': 11, 'abilityGameID': 38132}]

    @pytest.fixture
    def tainted_core_debuff_events(self):
        return [{'timestamp': 11075983, 'type': 'applydebuff', 'sourceID': 26, 'targetID': 26, 'abilityGameID': 38132},
                {'timestamp': 11080232, 'type': 'removedebuff', 'sourceID': 26, 'targetID': 26, 'abilityGameID': 38132},
                {'timestamp': 11080294, 'type': 'applydebuff', 'sourceID': 19, 'targetID': 19, 'abilityGameID': 38132,
                 'sourceMarker': 3, 'targetMarker': 3},
                {'timestamp': 11086834, 'type': 'removedebuff', 'sourceID': 19, 'targetID': 19, 'abilityGameID': 38132,
                 'sourceMarker': 3, 'targetMarker': 3},
                {'timestamp': 11086846, 'type': 'applydebuff', 'sourceID': 24, 'targetID': 24, 'abilityGameID': 38132},
                {'timestamp': 11088551, 'type': 'removedebuff', 'sourceID': 24, 'targetID': 24, 'abilityGameID': 38132},
                {'timestamp': 11164749, 'type': 'applydebuff', 'sourceID': 19, 'targetID': 19, 'abilityGameID': 38132,
                 'sourceMarker': 3, 'targetMarker': 3},
                {'timestamp': 11170402, 'type': 'removedebuff', 'sourceID': 19, 'targetID': 19, 'abilityGameID': 38132,
                 'sourceMarker': 3, 'targetMarker': 3},
                {'timestamp': 11170632, 'type': 'applydebuff', 'sourceID': 20, 'targetID': 20, 'abilityGameID': 38132},
                {'timestamp': 11173555, 'type': 'removedebuff', 'sourceID': 20, 'targetID': 20, 'abilityGameID': 38132},
                {'timestamp': 11173603, 'type': 'applydebuff', 'sourceID': 24, 'targetID': 24, 'abilityGameID': 38132},
                {'timestamp': 11178036, 'type': 'removedebuff', 'sourceID': 24, 'targetID': 24, 'abilityGameID': 38132},
                {'timestamp': 11178078, 'type': 'applydebuff', 'sourceID': 7, 'targetID': 7, 'abilityGameID': 38132},
                {'timestamp': 11189404, 'type': 'removedebuff', 'sourceID': 7, 'targetID': 7, 'abilityGameID': 38132},
                {'timestamp': 11189456, 'type': 'applydebuff', 'sourceID': 24, 'targetID': 24, 'abilityGameID': 38132},
                {'timestamp': 11192669, 'type': 'removedebuff', 'sourceID': 24, 'targetID': 24, 'abilityGameID': 38132},
                {'timestamp': 11234331, 'type': 'applydebuff', 'sourceID': 11, 'targetID': 11, 'abilityGameID': 38132,
                 'sourceMarker': 2, 'targetMarker': 2},
                {'timestamp': 11237632, 'type': 'removedebuff', 'sourceID': 11, 'targetID': 11, 'abilityGameID': 38132,
                 'sourceMarker': 2, 'targetMarker': 2},
                {'timestamp': 11237680, 'type': 'applydebuff', 'sourceID': 6, 'targetID': 6, 'abilityGameID': 38132},
                {'timestamp': 11241641, 'type': 'removedebuff', 'sourceID': 6, 'targetID': 6, 'abilityGameID': 38132},
                {'timestamp': 11241691, 'type': 'applydebuff', 'sourceID': 36, 'targetID': 36, 'abilityGameID': 38132},
                {'timestamp': 11243203, 'type': 'removedebuff', 'sourceID': 36, 'targetID': 36, 'abilityGameID': 38132},
                {'timestamp': 11347560, 'type': 'applydebuff', 'sourceID': 11, 'targetID': 11, 'abilityGameID': 38132,
                 'sourceMarker': 2, 'targetMarker': 2},
                {'timestamp': 11350429, 'type': 'removedebuff', 'sourceID': 11, 'targetID': 11, 'abilityGameID': 38132,
                 'sourceMarker': 2, 'targetMarker': 2},
                {'timestamp': 11350482, 'type': 'applydebuff', 'sourceID': 6, 'targetID': 6, 'abilityGameID': 38132},
                {'timestamp': 11356538, 'type': 'removedebuff', 'sourceID': 6, 'targetID': 6, 'abilityGameID': 38132},
                {'timestamp': 11356581, 'type': 'applydebuff', 'sourceID': 26, 'targetID': 26, 'abilityGameID': 38132},
                {'timestamp': 11357797, 'type': 'removedebuff', 'sourceID': 26, 'targetID': 26, 'abilityGameID': 38132}]

    def test_core_timings(self, vashj_analyser, tainted_core_debuff_events):
        expected = [12.6, 27.9, 8.9, 10.2]
        actual = vashj_analyser.core_timings(tainted_core_debuff_events)

        assert actual == expected

    def test_core_timings_lost_both_cores(self, vashj_analyser, tainted_core_debuff_events_all_lost):
        expected = [None, None]
        actual = vashj_analyser.core_timings(tainted_core_debuff_events_all_lost)

        assert actual == expected

    def test_core_timings_empty_list(self, vashj_analyser, empty_events_list):
        expected = []
        actual = vashj_analyser.core_timings(empty_events_list)

        assert actual == expected
