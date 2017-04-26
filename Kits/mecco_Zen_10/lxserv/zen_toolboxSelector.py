# python

import lx, lxifc, lxu
from zen import CommanderClass
from zen.Notifier import Notifier

CMD_NAME = 'zen.toolboxSelector'

TOOLBOXES = sorted([
    ('context', 'Context'),
    ('fusion', 'Fusion'),
    ('uv', 'UV'),
    ('paint', 'Paint'),
    ('sculpt', 'Sculpt'),
    ('animate', 'Animate'),
    ('game', 'Game'),
    ('actors', 'Actors'),
    ('deformers', 'Deformers'),
    ('dynamics', 'Dynamics'),
    ('particlePaint', 'Particle Paint'),
    ('vmap', 'Vertex Maps'),
    ('hair', 'Hair'),
    ('particles', 'Particles'),
    ('setup', 'Setup'),
    ('commandRegions', 'Command Regions'),
    ('ik', 'Inverse Kinematics')
])

CURRENT_TOOLBOX = 'context'

class CommandClass(CommanderClass):
    def commander_arguments(self):
        return [
                {
                    'name': 'toolbox',
                    'datatype': 'string',
                    'values_list': TOOLBOXES,
                    'values_list_type': 'popup',
                    'flags': ['query'],
                }, {
                    'name': 'is_enabled',
                    'datatype': 'boolean',
                    'flags': ['query', 'optional', 'hidden'],
                }
            ]

    def commander_execute(self, msg, flags):
        toolbox = self.commander_arg_value(0)

        global CURRENT_TOOLBOX
        CURRENT_TOOLBOX = toolbox

        notifier = Notifier()
        notifier.Notify(lx.symbol.fCMDNOTIFY_CHANGE_ALL)

    def commander_query(self, index):
        if index == 0:
            return CURRENT_TOOLBOX
        elif index == 1:
            toolbox_to_check = self.commander_arg_value(0)
            if CURRENT_TOOLBOX == toolbox_to_check:
                return True
            else:
                return False

    def commander_notifiers(self):
        return [("zen.notifier", "")]

lx.bless(CommandClass, CMD_NAME)
