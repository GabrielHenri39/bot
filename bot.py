import discord
from random import randint


class MyClient(discord.Client):
    
  
    async def on_ready(self):
        print(f'Logged on as { self.user.name}!')
         
        
        

    async def on_message(self, message,):
        if message.author == self.user:
          return
        print(f'Message from {message.author.name}: {message.content}')
        comado = str(message.content)
        comado=comado.lower()
        
        
        d1 = list()
        if comado == '/help':
            await message.channel.send(f'{message.author.name} ex: 4d6  retorna lista de numero, d20, (/d20,/d6,/d10,/d30, /d50 e /d100) mais modificado(dos)  ')
        elif ',' in comado:
    
            try:
                
                p = comado.find(',')
                
                comado1= comado[0:p] 
                mod= eval(comado[p+1:])

                if comado1== f'/d20': 
                    dado = randint(1,20)
                    dadom = dado + mod
                    await message.channel.send(f'{message.author.name}  seu dado é {dado} mais seu modificado é de {mod}-> {dadom}')
                
        
                elif comado1 == '/d6':
                    dado = randint(1,6)
                    dadom = dado + mod
                    await message.channel.send(f'{message.author.name}  seu dado é {dado} mais seu modificado é de {mod}-> {dadom}')
                
                elif comado1 == '/d10':
                    dado = randint(1,10)
                    dadom = dado + mod
                    await message.channel.send(f'{message.author.name}  seu dado é {dado} mais seu modificado é de {mod}-> {dadom}')

                elif comado1 == '/d30':
                    dado = randint(1,30)
                    dadom = dado + mod
                    await message.channel.send(f'{message.author.name}  seu dado é {dado} mais seu modificado é de {mod}-> {dadom}')
                
                elif comado1 == '/d50':
                    dado = randint(1,50) 
                    dadom = dado + mod
                    await message.channel.send(f'{message.author.name}  seu dado é {dado} mais seu modificado é de {mod}-> {dadom}')

                elif comado1 == '/d100':
                    dado = randint(1,100)
                    dadom = dado + mod
                    await message.channel.send(f'{message.author.name}  seu dado é {dado} mais seu modificado é de {mod}-> {dadom}')
                    
                elif comado1 =='/cal':
                    await message.channel.send(f'{message.author.name} sua contar e {mod}')
            except:
                pass
        elif comado == 'd20':
            dado = randint(1,20)
            await message.channel.send(f"{message.author.name} -> : {dado}")
        
        elif comado == 'd6':
            dado = randint(1,6)
            await message.channel.send(f"{message.author.name} -> : {dado}")
        
        elif comado == 'd10':
            dado = randint(1,10)
            await message.channel.send(f"{message.author.name} -> : {dado}")
        elif comado == 'd30':
            dado = randint(1,30)
            await message.channel.send(f"{message.author.name} -> : {dado}")
        
        elif comado == 'd50':
            dado = randint(1,50)
            await message.channel.send(f"{message.author.name} -> : {dado}")

        elif comado == 'd100':
            dado = randint(1,100)
            await message.channel.send(f"{message.author.name} -> : {dado}")
        

        
        
        elif "d" in comado:
            try:
                
                d=comado.find('d') 
                qua= int(comado[0:d])
                fase =int( comado[d+1:]) 
                if comado == f"{qua}d{fase}":
                    for nq in range(1,qua+1):
                        nq = randint(1,fase)
                        d1.append(nq)
                    await message.channel.send(f'{message.author.name}->  {d1}')
            except:pass
        
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f'Bem-Vindo {member.mention} ao servidor {guild.name} digita  /help para saber mais '
            await guild.system_channel.send(message)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot= MyClient(intents=intents)
bot.run('')
