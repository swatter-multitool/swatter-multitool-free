from scripts.settings import *

def cleardms():
    setTitle(f"[Cleardm] > albaner#0001")

    bot = commands.Bot(command_prefix="$", self_bot=True)
    bot.remove_command("help")
    print("")
    print(Colorate.Horizontal(Colors.rainbow, f"[Selfbot] active use prefix $clear to start!", 1))
    print("")

    @bot.command()
    async def clear(ctx, limit: int=None):
        passed = 0
        failed = 0
        async for msg in ctx.message.channel.history(limit=limit):
            if msg.author.id == bot.user.id:
                try:
                    await msg.delete()
                    passed += 1
                    setTitle(f"Clear DM » Cleared {passed} » Failed {failed}")
                except:
                    failed += 1
                    setTitle(f"Clear DM » Cleared {passed} » Failed {failed}")
        textfarbe(f"[Messages] » deleted » {passed}")


    bot.run(token, bot=False)