import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

partner_list = []

@bot.slash_command(name="파트너추가")
async def add_partner(interaction: nextcord.Interaction, user: nextcord.User):
    if user.id not in partner_list:
        partner_list.append(user.id)
        await interaction.response.send_message(f"{user.mention}님이 파트너로 추가되었습니다.")
    else:
        await interaction.response.send_message(f"{user.mention}님은 이미 파트너입니다.")

@bot.slash_command(name="파트너리스트")
async def list_partners(interaction: nextcord.Interaction):
    if partner_list:
        partners = [f"<@{user_id}>" for user_id in partner_list]
        await interaction.response.send_message("파트너 리스트:\n" + "\n".join(partners))
    else:
        await interaction.response.send_message("파트너가 없습니다.")

@bot.slash_command(name="파트너삭제")
async def remove_partner(interaction: nextcord.Interaction, user: nextcord.User):
    if user.id in partner_list:
        partner_list.remove(user.id)
        await interaction.response.send_message(f"{user.mention}님이 파트너에서 삭제되었습니다.")
    else:
        await interaction.response.send_message(f"{user.mention}님은 파트너 목록에 없습니다.")

bot.run("YOUR_TOKEN")
