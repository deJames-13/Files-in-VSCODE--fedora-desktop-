import random
import discord
from pandas import DataFrame
from discord.ext import commands
from music_bot3t3 import Music, PREFIX

PREFIX = PREFIX
client = discord.Client()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX),
                      description='Relatively simple music bot example')
discord.opus.is_loaded()
valid_user = ["Perseus 13th#4292"]
admins = []
blacklisted = []
games = {}
is_admin = False


# ++++++++++++++++++++++++++++++++++++++++++  Client Events  ++++++++++++++++++++++++++++++++++++++++++ #
@bot.event
async def on_ready():
    print(f'\n>> Logged In as {bot.user}\n')
    try:
        await bot.add_cog(Music(bot))
    except TypeError:
        pass

@bot.event
async def on_message(message):
    global prefix, games, is_admin
    prefix = PREFIX
    # guild = await bot.fetch_guild(message.guild.id)
    msg = message.content
    author = message.author
    author_handle = {author.id: f"{author.name}#{author.discriminator}"}
    channel = message.channel
    games[channel.id] = TicTacToe()
    if author == bot.user or (valid_user.count(author_handle[author.id]) > 0 and is_admin):
        return
    with open("logger", "a+") as f:
        f.write(f'{author} in {channel}: {msg} \n')
        print(f'{author} in {channel}: {msg} \n')
    if valid_user.count(author_handle[author.id]) > 0 or admins.count(author.id) > 0:
        if msg.startswith(f"{prefix}toggle-admin"):
            is_admin = not is_admin
            return
        elif msg.startswith(f"{prefix}make-admin"):
            for usr in message.mentions:
                if admins.count(usr.id) > 0:
                    return
                make_admin_user = usr.id
                admins.append(make_admin_user)
            return await channel.send('User {} is now an admin.'.format(', '.join([f"@{usr.name}" for usr in message.mentions])))
        elif msg.startswith(f'{prefix}pakyu'):
            for usr in message.mentions:
                if blacklisted.count(usr.id) > 0:
                    return
                block_user = usr.id
                blacklisted.append(block_user)
            return await channel.send('Blocked {}'.format(', '.join([usr.name for usr in message.mentions])))

        try:
            if msg.startswith(f"{prefix}remove-admin"):
                for usr in message.mentions:
                    admin_user = usr.id
                    admins.remove(admin_user)
            elif msg.startswith(f"{prefix}unblock"):
                for usr in message.mentions:
                    block_user = usr.id
                    blacklisted.remove(block_user)
                    print(f"Unblocked {usr.name}. {blacklisted}")

        except Exception as exc:
            return exc

    if blacklisted.count(author_handle) > 0:
        return
    if msg.startswith(f'{prefix}hello'):
        await channel.send(f'Hi there {author}')
    if msg.startswith(f'{prefix}say') and valid_user.count(str(author)) > 0:
        emb = discord.Embed(colour=0x48E7BF)
        emb.add_field(name=f'**🗨️{author} said... **', value=f'>>> *```{msg[5:]}```* ')
        await channel.send(content=None, embed=emb)
        try:
            await message.delete()
        except discord.NotFound or discord.Forbidden:
            return
    if msg.startswith(f'{prefix}tictactoe'):
        if len(games[channel.id].players) == 0 or valid_user.count(author) == 1:
            await mini_game_tictactoe(channel)
        elif games[channel.id].players.count(author) > 0:
            await mini_game_tictactoe(channel)
        else:
            await channel.send(f"Player {games[channel.id].players[0]} is playing...")
    await bot.process_commands(message)


# ++++++++++++++++++++++++++++++++++++++++++  Mini Game  ++++++++++++++++++++++++++++++++++++++++++ #
class TicTacToe:
    def __init__(self, pmove=None, turn=None):
        self.move = pmove
        self.turn = turn
        self.players = []
        self.game = []
        self.moves = []
        self.untiled = "⬛"
        self.player1_move = "❌"
        self.player1_moves = []
        self.player2_move = "⏺"
        self.player2_moves = []
        self.win = ['123', '147', '159', '258', '357', '369', '456', '789']


async def mini_game_tictactoe(channel):
    global prefix

    async def start(self):
        global start_embed, new_send
        if (start_game.content == f'{prefix}start' or start_game.content.startswith(
                f'{prefix}start bot')) and start_game.channel == channel:
            start_embed = discord.Embed(title=f"A tictactoe game was started by *```{start_game.author.name}```*",
                                        colour=0x48E7BF)
            await send_embed.edit(embed=start_embed)
            await start_game.delete()
            self.players.append(start_game.author.name)
            start_embed.add_field(name='> Player', value=f'***```{start_game.author.name}```***')
            if start_game.content.startswith(f'{prefix}start bot'):
                self.players.append('Bot')
                start_embed.remove_field(0)
                start_embed.add_field(name='> Players', value=f'***```{start_game.author.name} VS BOT```***')
            else:
                await send_embed.edit(embed=start_embed, content=None)
                await channel.send(f"> ***```Please join by {prefix}join```***")
                await join_game(self)
            if len(self.players) == 2:
                await channel.send('> ***Game Started***')
                self.game = list(self.untiled for _ in range(9))
                board = DataFrame([self.game[0:3], self.game[3:6], self.game[6:9]],
                                  columns=['    ', '    ', '    '])
                start_embed.add_field(name=f'{self.players[0]} Turn',
                                      value="```{}```".format(board.to_string(index=False)), inline=False)
                await send_embed.delete()
                new_send = await channel.send(embed=start_embed)
                await player_turn(self, self.players[0])
            else:
                return

    async def join_game(self):
        global start_embed, prefix
        if len(self.players) < 2:
            player_join = await bot.wait_for('message', check=check)
            if player_join.content.startswith(f'{prefix}join') and start_game.channel == player_join.channel:
                start_embed.remove_field(0)
                start_embed.add_field(name='> Players',
                                      value=f'***```{start_game.author.name} VS {player_join.author.name}```***')
                self.players.append(player_join.author.name)
                await player_join.delete()
            elif player_join.content.startswith(f'{prefix}tictactoe'):
                if self.players.count(player_join.author.name) == 1:
                    self.players.clear()
                    await quit_game()
            else:
                await channel.send(f"> ***```Please join by {prefix}join```***")
                await join_game(self)

            if self.players[0] == self.players[1]:
                self.players[1] = 'Bot'
                print(self.players)

    async def player_turn(self, player):
        global move, user, start_embed, new_send
        start_embed.remove_field(1)
        if len(self.player1_moves) == 5:
            return await channel.send('> ***Game Over. Draw***')
        on_going = True
        if player == 'Bot':
            move = f'{prefix}move ' + str(bot_moves(self))
            user = player
        else:
            self.turn = await bot.wait_for('message', check=check)
            move = self.turn.content
            user = self.turn.author.name
            await self.turn.delete()
        if move.startswith(f'{prefix}quit') or move.startswith(f'{prefix}tictactoe'):
            await quit_game(self.turn.author.name)
        elif user == player:
            try:
                self.turn = abs(int(move.removeprefix(f"{prefix}move").strip())) - 1
                if abs(self.turn) > 8:
                    await channel.send("> **Move from numbers 1-9**")
                    return await player_turn(self, player)
            except ValueError:
                await channel.send(f"> **Do a move using {prefix}move <1-9>**")
                return await player_turn(self, player)

            if self.game[int(self.turn)] == self.untiled:
                if player == self.players[0]:
                    self.game[int(self.turn)] = self.player1_move
                    self.player1_moves.append(self.turn + 1)
                    board = DataFrame([self.game[0:3], self.game[3:6], self.game[6:9]],
                                      columns=['    ', '    ', '    '])
                    start_embed.add_field(name=f'{self.players[1]}\'s Turn',
                                          value="```{}```".format(board.to_string(index=False)), inline=False)
                    for w_moves in range(len(self.win)):
                        points = 0
                        for w in self.win[w_moves]:
                            if self.player1_moves.count(int(w)) == 1:
                                points += 1
                        if points == 3:
                            on_going = False
                    await new_send.edit(embed=start_embed, content=None)
                    if on_going is not True:
                        await end(player)
                    else:
                        await player_turn(self, self.players[1])
                else:
                    if player == self.players[1]:
                        self.game[int(self.turn)] = self.player2_move
                        self.player2_moves.append(self.turn + 1)
                        board = DataFrame([self.game[0:3], self.game[3:6], self.game[6:9]],
                                          columns=['    ', '    ', '    '])
                        start_embed.add_field(name=f'{self.players[0]}\'s Turn',
                                              value="```{}```".format(board.to_string(index=False)), inline=False)
                        for w_moves in range(len(self.win)):
                            points = 0
                            for w in self.win[w_moves]:
                                if self.player2_moves.count(int(w)) == 1:
                                    points += 1
                            if points == 3:
                                on_going = False
                    await new_send.edit(embed=start_embed, content=None)
                    if on_going is not True:
                        await end(player)
                    else:
                        await player_turn(self, self.players[0])
            elif on_going is True:
                return await player_turn(self, player)
        else:
            return await player_turn(self, player)

    async def quit_game(player=None):
        if player:
            await channel.send(f"> ***Game Ended. {player} quited***")
        else:
            return

    async def end(player):
        await channel.send(f"> ***Game Ended.🎊 {player} WON🎊***")

    def bot_moves(self):
        global x
        print(f'Player 1: {self.player1_moves}, Player 2: {self.player2_moves}')
        for i in range(len(self.win)):
            point = 0
            for w in self.win[i]:
                if self.player2_moves.count(int(w)) == 1:
                    point += 1
                if point == 2:
                    for x in self.win[i]:
                        if self.player2_moves.count(int(x)) == 0:
                            if self.game[int(x) - 1] == self.untiled:
                                return x
        for i in range(len(self.win)):
            point = 0
            for w in self.win[i]:
                if self.player1_moves.count(int(w)) == 1:
                    point += 1
            if point == 2:
                for x in self.win[i]:
                    if self.player1_moves.count(int(x)) == 0:
                        if self.game[int(x) - 1] == self.untiled:
                            return x
        even = [2, 4, 6, 8]
        bot_move = self.player1_moves[-1] - 1
        if self.game[4] == self.untiled:
            return 5
        elif even.count(bot_move + 1) > 0:
            if self.game[bot_move - 1] == self.untiled:
                return bot_move
            else:
                if self.game[bot_move - 3] == self.untiled:
                    return bot_move - 2
        else:
            if self.game[4] == self.player1_move:
                x = ['1', '3', '7', '9']
                for i in x:
                    if self.game[int(i) - 1] == self.untiled:
                        return random.choice(x)
            for i in even:
                if self.game[int(i) - 1] == self.untiled:
                    return i
            return random.randint(1, 9)

    def check(m):
        if m.content == f'{prefix}join' and m.channel == channel:
            return m.content == f'{prefix}join' and m.channel == channel
        if m.content.startswith(f'{prefix}move') and m.channel == channel:
            return m.channel == channel
        if m.content.startswith(f'{prefix}quit') and m.channel == channel:
            return m.channel == channel
        if m.content == f'{prefix}tictactoe' and m.channel == channel:
            return m.content == f'{prefix}tictactoe' and m.channel == channel
        if (m.content == f'{prefix}start' or m.content.startswith(f'{prefix}start bot')) and m.channel == channel:
            return (m.content == f'{prefix}start' or m.content.startswith(
                f'{prefix}start bot')) and m.channel == channel

    games[channel.id].players.clear()
    embed = discord.Embed(title='Tic-Tac-Toe', colour=0x48E7BF)
    embed.add_field(name=f'{prefix}start bot',
                    value="> *```Use this command to start a game```*",
                    inline=True)
    embed.add_field(name=f'{prefix}move <1-9>',
                    value="> *```Use this command to move```*",
                    inline=True)
    embed.add_field(name=f'{prefix}quit',
                    value="> *```Use this to end an ongoing game. Only players can use this.```*",
                    inline=False)

    send_embed = await channel.send(embed=embed, content=None)
    start_game = await bot.wait_for('message', check=check)
    if start_game.channel.id == channel.id:
        if start_game.content.startswith(f'{prefix}tictactoe'):
            await quit_game()
        elif start_game.content.startswith(f'{prefix}start'):
            await start(games[channel.id])
        else:
            await channel.send(f"To play tictactoe, Do p/tictactoe then start by {prefix}start bot")


# ++++++++++++++++++++++++++++++++++++++++++  Mini Game  ++++++++++++++++++++++++++++++++++++++++++ #

token = open('token', 'r').readlines()

try:
    bot.run(token[0])
except RuntimeError or RuntimeWarning or Exception:
    print(f'{Exception}. Stopped')
