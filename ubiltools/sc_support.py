from ubiltools.structures import RevDict as _RevDict

SEVERITIES: _RevDict = _RevDict()

SEVERITIES.update({0: 'Info',
                   1: 'Low',
                   2: 'Medium',
                   3: 'High',
                   4: 'Critical'})
