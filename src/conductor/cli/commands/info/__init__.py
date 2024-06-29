import os
from conductor.lib.command import BaseCommand
from conductor.lib.constants import STEAM_USERDATA_PATH, STEAM_CONFIG_VDF_PATH
from conductor.lib.steam_helper import find_steam_user_id
from conductor.lib.vdf_file import VdfFile


class Command(BaseCommand):
    def __init__(self):
        self.__command_name = 'info'

    def get_command_str(self) -> str:
        return self.__command_name

    def register_options(self, subparsers) -> None:
        subparsers.add_parser(self.__command_name, help='prints information about the current steam installation')

    def command(self, args) -> int:
        user_id = find_steam_user_id()
        shortcuts_vdf_path = os.path.expanduser(os.path.join(STEAM_USERDATA_PATH, user_id, 'config', 'shortcuts.vdf'))
        shortcuts_vdf = VdfFile(shortcuts_vdf_path, binary=True, create_if_not_exists=True)
        print('Shortcuts added to steam:')
        print(shortcuts_vdf.pretty_print())
        print('-------------------------')
        print('VDF Config:')
        config_vdf = VdfFile(STEAM_CONFIG_VDF_PATH).data
        print(config_vdf)
        return 0
