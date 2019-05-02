## =========================================================
## Copyright 2019 Dietrich Bollmann
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##      http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------

"""nsl/go/scripts/nslgo.py:

Definition of the command line script `nslgo`.

"""

import click

from nsl.go.utils import get_version_long
from nsl.go.scripts.bot_v_bot import bot_v_bot
from nsl.go.scripts.human_v_bot import human_v_bot

## =========================================================
## Entry point of console script 'nslgo'
## ---------------------------------------------------------

## =========================================================
## Group:
## ---------------------------------------------------------

@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(get_version_long(), '-V', '--version')
def cli():
    """
    nslgo - Entertaining myself with Go and Deep Learning...
    """

## =========================================================
## Command: bvb
## ---------------------------------------------------------

# Help texts
board_size_help = "Size of the go board."
sleep_help = "Time to sleep between the moves."

@cli.command(name="bvb")
@click.option('--board-size', default=5, type=int, help=board_size_help)
@click.option('--sleep', default=0.3, type=float, help=sleep_help)
def command_generate(board_size, sleep):
    """Two bots playing randomly against each other.
    """

    # A random bot playing against another random bot
    bot_v_bot(board_size=board_size, sleep=sleep)
    
    # Done
    print('done.')
    print('')

## =========================================================
## Command: hvb
## ---------------------------------------------------------

# Help texts
board_size_help = "Size of the go board."

@cli.command(name="hvb")
@click.option('--board-size', default=5, type=int, help=board_size_help)
def command_generate(board_size):
    """A human playing against a random bot.
    """

    # A human playing against a random bot
    human_v_bot(board_size=board_size)
    
    # Done
    print('done.')
    print('')

## =========================================================
## =========================================================

## fin.
