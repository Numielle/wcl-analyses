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

    @pytest.fixture
    def tainted_elementals_damage_taken_events(self):
        return [{'timestamp': 11048453, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 159, 'mitigated': 102, 'unmitigatedAmount': 261},
                {'timestamp': 11048772, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 27050, 'hitType': 2, 'amount': 261, 'unmitigatedAmount': 214},
                {'timestamp': 11049519, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 165, 'mitigated': 105, 'unmitigatedAmount': 270},
                {'timestamp': 11050392, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 35298, 'hitType': 1, 'amount': 93, 'mitigated': 59, 'unmitigatedAmount': 152},
                {'timestamp': 11050505, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 164, 'mitigated': 106, 'unmitigatedAmount': 270},
                {'timestamp': 11050690, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 27021, 'hitType': 4, 'amount': 665, 'mitigated': 512, 'unmitigatedAmount': 1177,
                 'blocked': 51, 'sourceMarker': 3},
                {'timestamp': 11051089, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 75, 'hitType': 4, 'amount': 476, 'mitigated': 390, 'unmitigatedAmount': 866,
                 'blocked': 51, 'sourceMarker': 3},
                {'timestamp': 11051491, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 167, 'mitigated': 107, 'unmitigatedAmount': 274},
                {'timestamp': 11052021, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 35298, 'hitType': 2, 'amount': 206, 'unmitigatedAmount': 169},
                {'timestamp': 11052490, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 166, 'mitigated': 106, 'unmitigatedAmount': 272},
                {'timestamp': 11052590, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 34120, 'hitType': 1, 'amount': 575, 'mitigated': 370, 'unmitigatedAmount': 945,
                 'sourceMarker': 3},
                {'timestamp': 11052892, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 75, 'hitType': 1, 'amount': 571, 'mitigated': 366, 'unmitigatedAmount': 937,
                 'sourceMarker': 3},
                {'timestamp': 11053490, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 150, 'mitigated': 96, 'unmitigatedAmount': 246},
                {'timestamp': 11053629, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 1,
                 'abilityGameID': 35298, 'hitType': 1, 'amount': 116, 'mitigated': 75, 'unmitigatedAmount': 191},
                {'timestamp': 11064967, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 1, 'hitType': 2, 'amount': 299, 'unmitigatedAmount': 245},
                {'timestamp': 11065034, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 34120, 'hitType': 1, 'amount': 518, 'mitigated': 332, 'unmitigatedAmount': 850,
                 'sourceMarker': 3},
                {'timestamp': 11065410, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 75, 'hitType': 1, 'amount': 511, 'mitigated': 328, 'unmitigatedAmount': 839,
                 'sourceMarker': 3},
                {'timestamp': 11065762, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 27050, 'hitType': 2, 'amount': 249, 'unmitigatedAmount': 204},
                {'timestamp': 11065947, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 168, 'mitigated': 107, 'unmitigatedAmount': 275},
                {'timestamp': 11066544, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 34120, 'hitType': 1, 'amount': 533, 'mitigated': 344, 'unmitigatedAmount': 877,
                 'sourceMarker': 3},
                {'timestamp': 11066940, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 164, 'mitigated': 106, 'unmitigatedAmount': 270},
                {'timestamp': 11067405, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 35298, 'hitType': 1, 'amount': 127, 'mitigated': 80, 'unmitigatedAmount': 207},
                {'timestamp': 11067934, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 161, 'mitigated': 102, 'unmitigatedAmount': 263},
                {'timestamp': 11068059, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 34120, 'hitType': 1, 'amount': 518, 'mitigated': 333, 'unmitigatedAmount': 851,
                 'sourceMarker': 3},
                {'timestamp': 11068233, 'type': 'damage', 'sourceID': 20, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 25454, 'hitType': 1, 'amount': 984, 'unmitigatedAmount': 984},
                {'timestamp': 11068438, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 75, 'hitType': 2, 'amount': 1345, 'unmitigatedAmount': 929, 'sourceMarker': 3},
                {'timestamp': 11068916, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 158, 'mitigated': 100, 'unmitigatedAmount': 258},
                {'timestamp': 11069006, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 35298, 'hitType': 1, 'amount': 104, 'mitigated': 67, 'unmitigatedAmount': 171},
                {'timestamp': 11069017, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 34027, 'hitType': 1, 'amount': 296, 'mitigated': 189, 'unmitigatedAmount': 485},
                {'timestamp': 11069051, 'type': 'damage', 'sourceID': 24, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 32379, 'hitType': 1, 'amount': 813, 'unmitigatedAmount': 813},
                {'timestamp': 11069139, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 2,
                 'abilityGameID': 27021, 'hitType': 2, 'amount': 38, 'unmitigatedAmount': 1162, 'overkill': 1644,
                 'sourceMarker': 3},
                {'timestamp': 11154373, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 27019, 'hitType': 1, 'amount': 746, 'unmitigatedAmount': 746, 'sourceMarker': 3},
                {'timestamp': 11155557, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 75, 'hitType': 1, 'amount': 515, 'mitigated': 332, 'unmitigatedAmount': 847,
                 'sourceMarker': 3},
                {'timestamp': 11156445, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 144, 'mitigated': 93, 'unmitigatedAmount': 237},
                {'timestamp': 11156445, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 27050, 'hitType': 2, 'amount': 253, 'unmitigatedAmount': 207},
                {'timestamp': 11156793, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 34120, 'hitType': 1, 'amount': 467, 'mitigated': 300, 'unmitigatedAmount': 767,
                 'sourceMarker': 3},
                {'timestamp': 11156965, 'type': 'damage', 'sourceID': 24, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 32379, 'hitType': 1, 'amount': 772, 'unmitigatedAmount': 772},
                {'timestamp': 11157710, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 164, 'mitigated': 105, 'unmitigatedAmount': 269},
                {'timestamp': 11158060, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 35298, 'hitType': 1, 'amount': 99, 'mitigated': 63, 'unmitigatedAmount': 162},
                {'timestamp': 11158313, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 34120, 'hitType': 1, 'amount': 526, 'mitigated': 338, 'unmitigatedAmount': 864,
                 'sourceMarker': 3},
                {'timestamp': 11158689, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 75, 'hitType': 1, 'amount': 491, 'mitigated': 316, 'unmitigatedAmount': 807,
                 'sourceMarker': 3},
                {'timestamp': 11158994, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 148, 'mitigated': 93, 'unmitigatedAmount': 241},
                {'timestamp': 11159355, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 27021, 'hitType': 1, 'amount': 627, 'mitigated': 403, 'unmitigatedAmount': 1030,
                 'sourceMarker': 3},
                {'timestamp': 11159675, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 35298, 'hitType': 1, 'amount': 121, 'mitigated': 77, 'unmitigatedAmount': 198},
                {'timestamp': 11159968, 'type': 'damage', 'sourceID': 24, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 25375, 'hitType': 1, 'amount': 1031, 'unmitigatedAmount': 1031},
                {'timestamp': 11160236, 'type': 'damage', 'sourceID': 19, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 27019, 'hitType': 1, 'amount': 622, 'unmitigatedAmount': 622, 'sourceMarker': 3},
                {'timestamp': 11160282, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 148, 'mitigated': 95, 'unmitigatedAmount': 243},
                {'timestamp': 11161576, 'type': 'damage', 'sourceID': 28, 'targetID': 183, 'targetInstance': 4,
                 'abilityGameID': 1, 'hitType': 1, 'amount': 112, 'mitigated': 93, 'unmitigatedAmount': 237,
                 'overkill': 32},
                {'timestamp': 11224471, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 27019, 'hitType': 1, 'amount': 649, 'unmitigatedAmount': 649, 'sourceMarker': 2},
                {'timestamp': 11226044, 'type': 'damage', 'sourceID': 6, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 26985, 'hitType': 1, 'amount': 872, 'unmitigatedAmount': 872},
                {'timestamp': 11228205, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 75, 'hitType': 1, 'amount': 513, 'mitigated': 330, 'unmitigatedAmount': 843,
                 'sourceMarker': 2},
                {'timestamp': 11228905, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 27021, 'hitType': 1, 'amount': 645, 'mitigated': 414, 'unmitigatedAmount': 1059,
                 'sourceMarker': 2},
                {'timestamp': 11230304, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 75, 'hitType': 4, 'amount': 535, 'mitigated': 429, 'unmitigatedAmount': 964,
                 'blocked': 51, 'sourceMarker': 2},
                {'timestamp': 11230448, 'type': 'damage', 'sourceID': 6, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 26985, 'hitType': 1, 'amount': 906, 'unmitigatedAmount': 906},
                {'timestamp': 11231406, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 34120, 'hitType': 2, 'amount': 1323, 'unmitigatedAmount': 913, 'sourceMarker': 2},
                {'timestamp': 11231820, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 27019, 'hitType': 1, 'amount': 631, 'unmitigatedAmount': 631, 'sourceMarker': 2},
                {'timestamp': 11231947, 'type': 'damage', 'sourceID': 6, 'targetID': 183, 'targetInstance': 5,
                 'abilityGameID': 26985, 'hitType': 2, 'amount': 912, 'unmitigatedAmount': 863, 'overkill': 816},
                {'timestamp': 11288125, 'type': 'damage', 'sourceID': 23, 'targetID': 183, 'targetInstance': 6,
                 'abilityGameID': 27209, 'hitType': 1, 'amount': 1900, 'unmitigatedAmount': 1900},
                {'timestamp': 11290215, 'type': 'damage', 'sourceID': 23, 'targetID': 183, 'targetInstance': 6,
                 'abilityGameID': 30546, 'hitType': 1, 'amount': 1274, 'unmitigatedAmount': 1274},
                {'timestamp': 11294836, 'type': 'damage', 'sourceID': 30, 'targetID': 183, 'targetInstance': 6,
                 'abilityGameID': 27267, 'hitType': 1, 'amount': 263, 'unmitigatedAmount': 263},
                {'timestamp': 11295998, 'type': 'damage', 'sourceID': 23, 'targetID': 183, 'targetInstance': 6,
                 'abilityGameID': 27209, 'hitType': 1, 'amount': 1770, 'unmitigatedAmount': 1770},
                {'timestamp': 11319140, 'type': 'damage', 'sourceID': 24, 'targetID': 183, 'targetInstance': 7,
                 'abilityGameID': 25375, 'hitType': 1, 'amount': 1027, 'unmitigatedAmount': 1027},
                {'timestamp': 11323528, 'type': 'damage', 'sourceID': 24, 'targetID': 183, 'targetInstance': 7,
                 'abilityGameID': 25364, 'hitType': 1, 'amount': 1113, 'unmitigatedAmount': 1113},
                {'timestamp': 11339424, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 8,
                 'abilityGameID': 27019, 'hitType': 2, 'amount': 1427, 'unmitigatedAmount': 600, 'sourceMarker': 2},
                {'timestamp': 11342395, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 8,
                 'abilityGameID': 75, 'hitType': 2, 'amount': 1336, 'unmitigatedAmount': 923, 'sourceMarker': 2},
                {'timestamp': 11343505, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 8,
                 'abilityGameID': 34120, 'hitType': 2, 'amount': 1278, 'unmitigatedAmount': 883, 'sourceMarker': 2},
                {'timestamp': 11344429, 'type': 'damage', 'sourceID': 6, 'targetID': 183, 'targetInstance': 8,
                 'abilityGameID': 26988, 'hitType': 1, 'amount': 479, 'unmitigatedAmount': 479},
                {'timestamp': 11345018, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 8,
                 'abilityGameID': 34120, 'hitType': 2, 'amount': 1193, 'unmitigatedAmount': 824, 'sourceMarker': 2},
                {'timestamp': 11345397, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 8,
                 'abilityGameID': 75, 'hitType': 2, 'amount': 1208, 'unmitigatedAmount': 834, 'overkill': 1,
                 'sourceMarker': 2},
                {'timestamp': 11345939, 'type': 'damage', 'sourceID': 11, 'targetID': 183, 'targetInstance': 8,
                 'abilityGameID': 27021, 'hitType': 1, 'amount': 65, 'mitigated': 403, 'unmitigatedAmount': 1030,
                 'sourceMarker': 2}]

    @pytest.fixture
    def single_phoenix_egg_damage_taken_events(self):
        return [{'timestamp': 7957411, 'type': 'damage', 'sourceID': 13, 'targetID': 202, 'abilityGameID': 26862,
                 'hitType': 2, 'amount': 1521, 'unmitigatedAmount': 990},
                {'timestamp': 7957586, 'type': 'damage', 'sourceID': 30, 'targetID': 202, 'abilityGameID': 33983,
                 'hitType': 1, 'amount': 664, 'mitigated': 426, 'unmitigatedAmount': 1090},
                {'timestamp': 7957675, 'type': 'damage', 'sourceID': 30, 'targetID': 202, 'abilityGameID': 1,
                 'hitType': 1, 'amount': 311, 'mitigated': 199, 'unmitigatedAmount': 510}]

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

    def test_enemy_uptime_damage_taken(self, vashj_analyser, tainted_elementals_damage_taken_events):
        expected = [{'damage': 3934, 'killed': False, 'duration': 5.2,
                     'distribution': [(19, 2287, 58.1), (28, 1647, 41.9)]},
                    {'damage': 6986, 'killed': True, 'duration': 4.2,
                     'distribution': [(19, 3463, 49.6), (28, 1726, 24.7), (20, 984, 14.1), (24, 813, 11.6)]},
                    {'damage': 0, 'killed': False, 'duration': None, 'distribution': []},
                    {'damage': 6986, 'killed': True, 'duration': 7.2,
                     'distribution': [(19, 3994, 57.2), (24, 1803, 25.8), (28, 1189, 17.0)]},
                    {'damage': 6986, 'killed': True, 'duration': 7.5,
                     'distribution': [(11, 4296, 61.5), (6, 2690, 38.5)]},
                    {'damage': 5207, 'killed': False, 'duration': 7.9,
                     'distribution': [(23, 4944, 94.9), (30, 263, 5.1)]},
                    {'damage': 2140, 'killed': False, 'duration': 4.4,
                     'distribution': [(24, 2140, 100.0)]},
                    {'damage': 6986, 'killed': True, 'duration': 6.5,
                     'distribution': [(11, 6507, 93.1), (6, 479, 6.9)]}]

        actual = vashj_analyser.enemy_uptime_damage_taken(8, tainted_elementals_damage_taken_events)

        assert actual == expected

    def test_enemy_uptime_damage_taken_single_enemy(self, vashj_analyser, single_phoenix_egg_damage_taken_events):
        expected = [{'damage': 2496,
                     'distribution': [(13, 1521, 60.9), (30, 975, 39.1)],
                     'duration': 0.3,
                     'killed': False}]
        actual = vashj_analyser.enemy_uptime_damage_taken(1, single_phoenix_egg_damage_taken_events)

        assert actual == expected
