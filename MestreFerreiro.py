import discord
from discord.ext.commands import Bot as commands
import random

token = '' #Insira o seu token aqui.

Prefix = '.'
intents = discord.Intents.all()
client = commands(command_prefix=Prefix, intents=intents)

@client.event
async def on_ready():
    print('Logado como {0.user}'.format(client))
    print(f'Ping:  {round (client.latency * 1000)}')

@client.command()
async def info(ctx):
    user_id = ctx.message.author.id
    user = await client.fetch_user(user_id)
    await ctx.message.delete()
    msg = f'Olá {ctx.author.mention}!'
    print(f'O usuário {ctx.author} utilizou o comando .info.')
    msg2 = 'Eu sou o maior ferreiro de toda Rune-Midgard!\n\nChances por Refino:\n(Elu Enriquecido/Perfeito)\n\n+4 para +5: 84%\n+5 para +6: 64%\n+6 para +7: 64%\n+7 para +8: 36%\n+8 para +9: 36%\n+9 para +10:19%\n'
    msg3 = 'Chances por Refino:\n(Elunium Normal)\n\n+4 para +5: 60%\n+5 para +6: 40%\n+6 para +7: 40%\n+7 para +8: 20%\n+8 para +9: 20%\n+9 para +10:10%\n'
    msgobs = '\nOBS: Só suporto refinar até 10 itens por simulação.'
    msg4 = f'Comandos:\n.refino x (Simula refino com Elunium Enriquecido/Perfeito)\n.refinocomum x (Simula refino com Elunium normal)\n.ping (Consulta o ping do Bot)\n.info (Informações).{msgobs}\n\nAutor: Lucassi'
    await user.send(embed=discord.Embed(title='Informações', url='https://www2.worldrag.com/forum/topic/94668-tabela-de-refinamento/', description=f'{msg}\n{msg2}\n{msg3}\n{msg4}\n'))

@client.command()
async def refino(ctx, itens=0):
    print(f'O usuário {ctx.author} utilizou o comando .refino para {itens} itens.')
    user_id = ctx.message.author.id
    user = await client.fetch_user(user_id)
    await ctx.message.delete()
    if itens > 0 and itens < 11:
        msg = f'Olá, {ctx.author.mention}!\nIniciando o refino em {itens} itens:'
        await user.send(msg)

        qtditem = itens
        qtditem4 = qtditem
        elunium = [0 , 0, 0]
        isucess = [0, 0, 0, 0, 0, 0]
        c = [0, 0, 0, 0, 0, 0]
        iquebra = [0]
        report = []

        async def refino5(qtditem4):
            qtditem4 -= 1
            elunium[1] += 1
            chance = int(84)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+4 para +5) Sucesso!\n')
                isucess[0] += 1
                c[0] += 1
            else:
                resultado = False
                report.append('(+4 para +5) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')
            if resultado:
                await refino6()    
    
            return qtditem4

        async def refino6():
            isucess[0] -= 1
            elunium[1] += 1
            chance = int(64)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+5 para +6) Sucesso!\n')
                isucess[1] += 1
                c[1] += 1
            else:
                resultado = False
                report.append('(+5 para +6) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')
            if resultado:
                await refino7()   

        async def refino7():
            isucess[1] -= 1
            elunium[1] += 1
            chance = int(64)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+6 para +7) Sucesso!\n')
                isucess[2] += 1
                c[2] += 1
            else:
                resultado = False
                report.append('(+6 para +7) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')       
            if resultado:
                await refino8()  

        async def refino8():
            isucess[2] -= 1
            elunium[2] += 1
            chance = int(36)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+7 para +8) Sucesso!\n')
                isucess[3] += 1
                c[3] += 1
            else:
                resultado = False
                report.append('(+7 para +8) Falha!\n')
                report.append('O refino retornou para +6...\n')
                isucess[2] += 1
            report.append('...\n')  
            if resultado:
                await refino9()
            else:
                await refino7()  

        async def refino9():
            isucess[3] -= 1
            elunium[2] += 1
            chance = int(36)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+8 para +9) Sucesso!\n')
                isucess[4] += 1
                c[4] += 1
            else:
                resultado = False
                report.append('(+8 para +9) Falha!\n')
                report.append('O refino retornou para +7...\n')
                isucess[3] += 1
            report.append('...\n')
            if resultado:
                await refino10()
            else:
                await refino8()

        async def refino10():
            isucess[4] -= 1
            elunium[2] += 1
            chance = int(19)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+9 para +10) Sucesso!\n')
                isucess[5] += 1
                c[5] += 1
            else:
                resultado = False
                report.append('(+9 para +10) Falha!\n')
                report.append('O refino retornou para +8...\n')
                isucess[4] += 1
            report.append('...\n')   
            if resultado == False:
                await refino9()
                
        while qtditem4 > 0:
            qtditem4 = await refino5(qtditem4)
            if qtditem4 == 0:
                embedreport = discord.Embed(title=f'**SIMULAÇÃO DO REFINO**\n', url='https://www2.worldrag.com/', description=''.join(report))
                await user.send(embed=embedreport)

        report2 = []
        report2.append(f'Quantidade de Itens +4: {qtditem}\n')
        report2.append(f'Itens +5: {c[0]}\n')
        report2.append(f'Itens +6: {c[1]}\n')
        report2.append(f'Itens +7: {c[2]}\n')
        report2.append(f'Itens +8: {c[3]}\n')
        report2.append(f'Itens +9: {c[4]}\n')
        report2.append(f'Itens +10: {c[5]}\n')
        report2.append(f'Itens Quebrados: {iquebra}\n')
        report2.append(f'Qtd de Elunium Enriquecido: {elunium[1]}\n')
        report2.append(f'Qtd de Elunium Perfeito: {elunium[2]}\n')

        embedreport2 = discord.Embed(title='**RESUMO DA SIMULAÇÃO**\n', url='https://www2.worldrag.com/', description=''.join(report2))
        await user.send(embed=embedreport2)

    else:
        msg = f'{ctx.author.mention}, não foi possível iniciar sua simulação!'
        msg2 = 'Adicione a quantidade de itens que deseja refinar depois do comando. Exemplo para refinar 4 itens: .refino 4'
        msg3 = '\nOBS: Só suporto simular 10 itens por vez!'
        embederro = discord.Embed(title='*ERRO!*', url='https://www2.worldrag.com/', description=f'{msg}\n{msg2}\n{msg3}')
        await user.send(embed=embederro)

    print(f'O refino para o usuário {ctx.author} foi encerrado.')

@client.command()
async def ping(ctx):
    user_id = ctx.message.author.id
    user = await client.fetch_user(user_id)
    await ctx.message.delete()
    embed=discord.Embed(title="Pong!", url='https://www2.worldrag.com/',description=f'{ctx.author.mention} o ping atual é {round(client.latency * 1000)}ms', color=0xFF5733)
    await user.send(embed=embed)

@client.command()
async def refinocomum(ctx, itens=0):
    print(f'O usuário {ctx.author} utilizou o comando .refinocomum para {itens} itens.')
    user_id = ctx.message.author.id
    user = await client.fetch_user(user_id)
    await ctx.message.delete()
    if itens > 0 and itens < 11:
        msg = f'Olá, {ctx.author.mention}!\nIniciando o refino com Elunium Comum em {itens} itens:'
        await user.send(msg)

        qtditem = itens
        qtditem4 = qtditem
        elunium = [0 , 0, 0]
        isucess = [0, 0, 0, 0, 0, 0]
        c = [0, 0, 0, 0, 0, 0]
        iquebra = [0]
        report = []

        async def refino5(qtditem4):
            qtditem4 -= 1
            elunium[0] += 1
            chance = int(60)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+4 para +5) Sucesso!\n')
                isucess[0] += 1
                c[0] += 1
            else:
                resultado = False
                report.append('(+4 para +5) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')
            if resultado:
                await refino6()    
    
            return qtditem4

        async def refino6():
            isucess[0] -= 1
            elunium[0] += 1
            chance = int(40)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+5 para +6) Sucesso!\n')
                isucess[1] += 1
                c[1] += 1
            else:
                resultado = False
                report.append('(+5 para +6) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')
            if resultado:
                await refino7()   

        async def refino7():
            isucess[1] -= 1
            elunium[0] += 1
            chance = int(40)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+6 para +7) Sucesso!\n')
                isucess[2] += 1
                c[2] += 1
            else:
                resultado = False
                report.append('(+6 para +7) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')       
            if resultado:
                await refino8()  

        async def refino8():
            isucess[2] -= 1
            elunium[0] += 1
            chance = int(20)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+7 para +8) Sucesso!\n')
                isucess[3] += 1
                c[3] += 1
            else:
                resultado = False
                report.append('(+7 para +8) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')  
            if resultado:
                await refino9()

        async def refino9():
            isucess[3] -= 1
            elunium[0] += 1
            chance = int(20)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                resultado = True
                report.append('(+8 para +9) Sucesso!\n')
                isucess[4] += 1
                c[4] += 1
            else:
                resultado = False
                report.append('(+8 para +9) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')
            if resultado:
                await refino10()

        async def refino10():
            isucess[4] -= 1
            elunium[0] += 1
            chance = int(10)
            tentativa = random.randint(1, 100)
            if tentativa <= chance:
                report.append('(+9 para +10) Sucesso!\n')
                isucess[5] += 1
                c[5] += 1
            else:
                report.append('(+9 para +10) Falha, o equipamento foi quebrado...\n')
                iquebra[0] += 1
            report.append('...\n')   
                
        while qtditem4 > 0:
            qtditem4 = await refino5(qtditem4)
            if qtditem4 == 0:
                embedreport = discord.Embed(title='**SIMULAÇÃO DO REFINO**\n', url='https://www2.worldrag.com/', description=''.join(report))
                await user.send(embed=embedreport)

        report2 = []
        report2.append(f'Quantidade de Itens +4: {qtditem}\n')
        report2.append(f'Itens +5: {c[0]}\n')
        report2.append(f'Itens +6: {c[1]}\n')
        report2.append(f'Itens +7: {c[2]}\n')
        report2.append(f'Itens +8: {c[3]}\n')
        report2.append(f'Itens +9: {c[4]}\n')
        report2.append(f'Itens +10: {c[5]}\n')
        report2.append(f'Itens Quebrados: {iquebra}\n')
        report2.append(f'Qtd de Elunium Comum: {elunium[0]}\n')

        embedreport2 = discord.Embed(title='**RESUMO DA SIMULAÇÃO**\n', url='https://www2.worldrag.com/', description=''.join(report2))
        await user.send(embed=embedreport2)

    else:
        msg = f'{ctx.author.mention}, não foi possível iniciar sua simulação!'
        msg2 = 'Adicione a quantidade de itens que deseja refinar depois do comando. Exemplo para refinar 4 itens: .refinocomum 3'
        msg3 = '\nOBS: Só suporto simular 10 itens por vez!'
        embederro = discord.Embed(title='*ERRO!*', url='https://www2.worldrag.com/', description=f'{msg}\n{msg2}\n{msg3}')
        await user.send(embed=embederro)

    print(f'O refino para o usuário {ctx.author} foi encerrado.')

client.run(token)
