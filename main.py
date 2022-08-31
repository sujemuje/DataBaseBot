import discord
import os
from typing import *


client = discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree(client=client)


hatsune_group = discord.app_commands.Group(
    name='hatsune_database',
    description='idk',
    guild_ids=[602533696272203815]
)


@hatsune_group.command(
    name='hatsune_miku',
    description='lol'
)
async def __command_hatsune_miku(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('hatsune miku')


tree.add_command(hatsune_group)


@tree.command(
    name='add_command',
    description='Add your own command'
)
async def __command_add_command(
        interaction: discord.Interaction,
        command_name: str
) -> None:
    await \
        interaction.response.send_message(content='Creating command...')

    @tree.command(
        name=command_name,
        description=f'Custom command created by {interaction.user.name}'
    )
    async def cmd(_interaction: discord.Interaction) -> None:
        await _interaction.response.send_message(
            'Congratulations, you successfully created this command!'
        )

    await tree.sync()
    await \
        interaction.edit_original_response(content='Command successfully created')


@client.event
async def on_ready():
    await tree.sync()
    print("ready")


TOKEN = os.environ['TOKEN']
client.run(TOKEN)
