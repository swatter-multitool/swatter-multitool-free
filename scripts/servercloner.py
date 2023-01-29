from concurrent.futures import thread
from scripts.settings import *

def svc():
    print("")
    input_guild_id = input(Colorate.Horizontal(Colors.green_to_yellow, f"[Guild] to copy » ", 1))
    output_guild_id = input(Colorate.Horizontal(Colors.purple_to_blue, f"[Guild] to paste » ", 1))

    print("  ")

    def print_add(message):
        print(Colorate.Horizontal(Colors.rainbow, f"[Successfully] > {message}", 1))

    def print_delete(message):
        print(Colorate.Horizontal(Colors.yellow_to_red, f"[Deleted] > {message}", 1))

    def print_warning(message):
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[Warning] > {message}", 1))

    def print_error(message):
        print(Colorate.Horizontal(Colors.purple_to_red, "[Error] > {message}", 1))

    client = discord.Client()

    class albanischerclon:
        @staticmethod
        async def roles_delete(guild_to: discord.Guild):
                for role in guild_to.roles:
                    try:
                        if role.name != "@everyone":
                            await role.delete()
                            print_delete(f"Deleted Role: {role.name}")
                    except discord.Forbidden:
                        print_error(f"Error While Deleting Role: {role.name}")
                    except discord.HTTPException:
                        print_error(f"Unable to Delete Role: {role.name}")

        @staticmethod
        async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
            roles = []
            role: discord.Role
            for role in guild_from.roles:
                if role.name != "@everyone":
                    roles.append(role)
            roles = roles[::-1]
            for role in roles:
                try:
                    await guild_to.create_role(
                        name=role.name,
                        permissions=role.permissions,
                        colour=role.colour,
                        hoist=role.hoist,
                        mentionable=role.mentionable
                    )
                    print_add(f"Created Role {role.name}")
                except discord.Forbidden:
                    print_error(f"Error While Creating Role: {role.name}")
                except discord.HTTPException:
                    print_error(f"Unable to Create Role: {role.name}")

        @staticmethod
        async def channels_delete(guild_to: discord.Guild):
            for channel in guild_to.channels:
                try:
                    await channel.delete()
                    print_delete(f"Deleted Channel: {channel.name}")
                except discord.Forbidden:
                    print_error(f"Error While Deleting Channel: {channel.name}")
                except discord.HTTPException:
                    print_error(f"Unable To Delete Channel: {channel.name}")

        @staticmethod
        async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
            channels = guild_from.categories
            channel: discord.CategoryChannel
            new_channel: discord.CategoryChannel
            for channel in channels:
                try:
                    overwrites_to = {}
                    for key, value in channel.overwrites.items():
                        role = discord.utils.get(guild_to.roles, name=key.name)
                        overwrites_to[role] = value
                    new_channel = await guild_to.create_category(
                        name=channel.name,
                        overwrites=overwrites_to)
                    await new_channel.edit(position=channel.position)
                    print_add(f"Created Category: {channel.name}")
                except discord.Forbidden:
                    print_error(f"Error While Deleting Category: {channel.name}")
                except discord.HTTPException:
                    print_error(f"Unable To Delete Category: {channel.name}")

        @staticmethod
        async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
            channel_text: discord.TextChannel
            channel_voice: discord.VoiceChannel
            category = None
            for channel_text in guild_from.text_channels:
                try:
                    for category in guild_to.categories:
                        try:
                            if category.name == channel_text.category.name:
                                break
                        except AttributeError:
                            print_warning(f"Channel {channel_text.name} doesn't have any category!")
                            category = None
                            break

                    overwrites_to = {}
                    for key, value in channel_text.overwrites.items():
                        role = discord.utils.get(guild_to.roles, name=key.name)
                        overwrites_to[role] = value
                    try:
                        new_channel = await guild_to.create_text_channel(
                            name=channel_text.name,
                            overwrites=overwrites_to,
                            position=channel_text.position,
                            topic=channel_text.topic,
                            slowmode_delay=channel_text.slowmode_delay,
                            nsfw=channel_text.nsfw)
                    except:
                        new_channel = await guild_to.create_text_channel(
                            name=channel_text.name,
                            overwrites=overwrites_to,
                            position=channel_text.position)
                    if category is not None:
                        await new_channel.edit(category=category)
                    print_add(f"Created Text Channel: {channel_text.name}")
                except discord.Forbidden:
                    print_error(f"Error While Creating Text Channel: {channel_text.name}")
                except discord.HTTPException:
                    print_error(f"Unable To Creating Text Channel: {channel_text.name}")
                except:
                    print_error(f"Error While Creating Text Channel: {channel_text.name}")

            category = None
            for channel_voice in guild_from.voice_channels:
                try:
                    for category in guild_to.categories:
                        try:
                            if category.name == channel_voice.category.name:
                                break
                        except AttributeError:
                            print_warning(f"Channel {channel_voice.name} doesn't have any category!")
                            category = None
                            break

                    overwrites_to = {}
                    for key, value in channel_voice.overwrites.items():
                        role = discord.utils.get(guild_to.roles, name=key.name)
                        overwrites_to[role] = value
                    try:
                        new_channel = await guild_to.create_voice_channel(
                            name=channel_voice.name,
                            overwrites=overwrites_to,
                            position=channel_voice.position,
                            bitrate=channel_voice.bitrate,
                            user_limit=channel_voice.user_limit,
                            )
                    except:
                        new_channel = await guild_to.create_voice_channel(
                            name=channel_voice.name,
                            overwrites=overwrites_to,
                            position=channel_voice.position)
                    if category is not None:
                        await new_channel.edit(category=category)
                    print_add(f"Created Voice Channel: {channel_voice.name}")
                except discord.Forbidden:
                    print_error(f"Error While Creating Voice Channel: {channel_voice.name}")
                except discord.HTTPException:
                    print_error(f"Unable To Creating Voice Channel: {channel_voice.name}")
                except:
                    print_error(f"Error While Creating Voice Channel: {channel_voice.name}")

        @staticmethod
        async def members_manage(guild_to: discord.Guild, guild_from: discord.Guild):
            member_to: discord.Member
            member_from: discord.Member
            for member_from in guild_from.members:
                if member_from in guild_to.members:
                    member_to = guild_to.get_member(member_from.id)
                    try:
                        roles = []
                        for role_from in member_from.roles:
                            role_to = discord.utils.get(guild_to.roles, name=role_from.name)
                            if role_to is not None and role_to.name != "@everyone" and role_to.name != "CopyPaste2":
                                roles.append(role_to)
                        for role in roles:
                            await member_to.add_roles(role)
                        print(Colorate.Horizontal(Colors.purple_to_red, f"Gave {member_to.name} all the Roles that he had in > [{guild_to.name}]", 1))
                    except discord.Forbidden:
                        print_error(f"Can't add roles for member {member_to.name} in {guild_to.name} (Forbidden)")
                    except discord.HTTPException:
                        print_error(f"Can't add roles for member {member_to.name} in {guild_to.name}")


        @staticmethod
        async def emojis_delete(guild_to: discord.Guild):
            for emoji in guild_to.emojis:
                try:
                    await emoji.delete()
                    print_delete(f"Deleted Emoji: {emoji.name}")
                except discord.Forbidden:
                    print_error(f"Error While Deleting Emoji{emoji.name}")
                except discord.HTTPException:
                    print_error(f"Error While Deleting Emoji {emoji.name}")

        @staticmethod
        async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
            emoji: discord.Emoji
            for emoji in guild_from.emojis:
                try:
                    emoji_image = await emoji.url.read()
                    await guild_to.create_custom_emoji(
                        name=emoji.name,
                        image=emoji_image)
                    print_add(f"Created Emoji {emoji.name}")
                except discord.Forbidden:
                    print_error(f"Error While Creating Emoji {emoji.name} ")
                except discord.HTTPException:
                    print_error(f"Error While Creating Emoji {emoji.name}")

        @staticmethod
        async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
            try:
                try:
                    icon_image = await guild_from.icon_url.read()
                except discord.errors.DiscordException:
                    print_error(f"Can't read icon image from {guild_from.name}")
                    icon_image = None
                await guild_to.edit(name=f'{guild_from.name}')
                if icon_image is not None:
                    try:
                        await guild_to.edit(icon=icon_image)
                        print_add(f"Guild Icon Changed: {guild_to.name}")
                    except:
                        print_error(f"Error While Changing Guild Icon: {guild_to.name}")
            except discord.Forbidden:
                print_error(f"Error While Changing Guild Icon: {guild_to.name}")


        @client.event
        async def on_ready():
            print(Colorate.Horizontal(Colors.rainbow, f"Logged In as : {client.user}", 1))
            print(Colorate.Horizontal(Colors.blue_to_cyan, "Start to clone Server", 1))
            print()
            guild_from = client.get_guild(int(input_guild_id))
            guild_to = client.get_guild(int(output_guild_id))

            await albanischerclon.roles_delete(guild_to)
            await albanischerclon.channels_delete(guild_to)
            await albanischerclon.emojis_delete(guild_to)
            await albanischerclon.roles_create(guild_to, guild_from)
            await albanischerclon.categories_create(guild_to, guild_from)
            await albanischerclon.channels_create(guild_to, guild_from)
            await albanischerclon.members_manage(guild_to, guild_from)
            await albanischerclon.emojis_create(guild_to, guild_from)


        def clonStartUp(self):
            client.run(token, bot=False)
            threading.Thread(target=albanischerclon.on_ready()).start()


    albanischerclon().clonStartUp()