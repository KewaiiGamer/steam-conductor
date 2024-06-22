# Steam Conductor

## Description

All in one solution for managing all games within steam.

## Goals of this project

- Enabling batch (un)installation of games with tools such as ansible or plain shell scripts
- Create a tool for managing mods for all steam games
  - This includes downloading, installing, updating and removing mods
  - Letting the user define virtual file systems for mods, much like [Mod Organizer 2](https://www.nexusmods.com/skyrimspecialedition/mods/6194)
  but for linux
- Letting the user define game profiles that specify launch options, environment variables, etc. for official steam games
in an effort to make linux gaming even more accessible.
  - Allow users to share these profiles with others
  - Find a way to allow users to map these profiles with their hardware configurations to make it easier for others to discover
  compatibility fixes

## Development

### Requirements
- [Python 3.10+](https://www.python.org/downloads/)
- [PyCharm (optional, recommended)](https://www.jetbrains.com/pycharm/download/)

### Getting started

Recommended to use virtual environments to avoid conflicts with system packages.

```bash
$ cd /path/to/conductor/project/root
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -e .
$ python3 ./src/conductor/cli --help
```

## How to build conductor-cli

Currently, the project uses pyinstaller to build the binary. This is subject to change.

```bash
$ cd /path/to/conductor/project/root
$ ./scripts/build.sh
$ ./bin/conductor-cli --help
```

To clean up all build artifacts, run:

```bash
$ ./scripts/clean.sh
```

## how to use conductor-cli
    
```bash
$ ./bin/conductor-cli --help
usage: conductor-cli [-h] [--version] [command] ...

All in one steam game manager

positional arguments:
  [command]        Available commands
    info           prints information about the current steam installation
    add_shortcut   adds an executable shortcut to steam
    remove_shortcut
                   removes an executable shortcut to steam
    install        installs a non-steam game

options:
  -h, --help    show this help message and exit
  --version     Print the version of conductor
```

### Commands

- [info](src/conductor/cli/commands/info/README.md)
- [add_shortcut](src/conductor/cli/commands/add_shortcut/README.md)
- [remove_shortcut](src/conductor/cli/commands/remove_shortcut/README.md)
- [install](src/conductor/cli/commands/install/README.md)
