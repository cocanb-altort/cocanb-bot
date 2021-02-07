import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from unicodedata import *
from replit import db
from keep_alive import keep_alive
from datetime import datetime, timedelta
from time import localtime, strftime

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='*', description='A bot for members of the Cocánb')

@bot.command(name='tochar', help='Converts unicode codepoint to character')
async def unicode(ctx, codepoint):
    response = chr(int(codepoint, 16))
    await ctx.send('```' + response + '```')

@bot.command(name='tocode', help='Converts character to unicode codepoint')
async def unicode(ctx, character):
    response = hex(ord(character))
    response = response[2:]
    if len (response) == 1:
        response = '000' + response
    elif len (response) == 2:
        response = '00' + response
    elif len (response) == 3:
        response = '0' + response
    else:
        pass
    code = '```U+' + response + '```'
    await ctx.send(code.upper())

@bot.command(name='time', help='Shows current time given a timezone (In (-)HH:MM format)')
async def time (ctx, timezone: str='00:00'):
  if timezone[0] == '-':
    hours = int(timezone[:-3])-int(timezone[-2:])/60
  else:
    hours = int(timezone[:-3])+int(timezone[-2:])/60
  future_time = datetime.today() + timedelta(hours=hours)
  if timezone == '00:00':
    plus = '±'
  elif timezone[0] == '-':
    plus = ''
  elif timezone[0] == '+':
    plus = ''
  else:
    plus = '+'
  week_day = future_time.weekday()
  weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
  week_day = weekdays[week_day]
  if timezone[-3] == ':':
    await ctx.send('```' + week_day + ', ' + str(future_time) + ', UTC' + plus + timezone + '```')
  else:
    pass

@bot.command(name='cocanb', help= 'sends thPoéo thCocán Altorn Onécmdf Bec Bftf')
async def cocanb (ctx, format: str=None):
  if format is None:
    await ctx.send ('thPoéo thCocán Altorn Onécmdf Bec Bftf\n\nCocánb altort, ürpenîtort ürodictort ürişêxu áaç tivitin volvinãp plicat īóopaioc onşt rictiot thpení otês ticlen onkdd cłdeğse egřbk degsbáal fýhginkf bňdřbň lobec seřbsi. Thîmain vòlvdir ectlpá infuác tiviti, esücağ énitap iercinŵap, lagenít, aspan, kiñşqué ezinb, albüs tingen, itafløg, ginürethrap, latickłt ortú, rerotielec trøstim ulatiok, néeinok ickinnons dýce gýhlgşjħd sbłggħx cýdłggh gildggłg ghlhýd efegč fňřg gřbgg. Thrécipie nosûcác tiviti émareç eivdir ecphýş icaple asurvim asochísœ, motionâp leasürt hrouğe rôti chumili, atióok noŵledgt hath plaipléa sint sadis tidomin antnon ectifbh dşjýčeğtflħe hačmir bliehhğclčfň křbeit decýds bgho báachth. Manóth éspraç tičecarrsiğ nifîca nħéal trisk nonýdf béesi yetkħfse.')
  elif format == 'ipa':
    await ctx.send ('[θ‿poˈe̯.o̞̯ θ‿koˈkɐn älˈtorn‿ɔnɛkm̩df bek.ˈbf̩tf̩] \n\n[ko̞ˈkɐnb ʔälˈtort | ˈʔyrpeni̞ˌtort‿yrodi̞k̚ˈtort‿yrɪʃe̞ksu ʔʌsˑ ˌtɪvɪˈtʲɪn vɤɫviˈnʌ̃ᵐp pliˈkɐt joːpɐˈjok‿on̠ʃt ri̞kˈtʲjot θ‿ˈpe̞ni o̞ˈte̙ʃ ‖ ti̞klen ʔo̞ŋkt | kl̩ˈdeɪ̯s̬ə‿eˈɡr̩b̥k deg̊sˈbaˑɫ fy̞̆ˈgi̞nk͡f | ˈbn̩dr̩ˌbn̩ lɔ̞ˈbe̞k̚ ˈse̞.r̩b.siˑ ‖ tʰɪˈmɐɪ̯n vo̞ɫvˈdiːr ekt͡ɬˈpä ɪnˈfʷɐk̚ tiviˈtʲiː | e̞sʉˈkäɪ̯ e̞nɪ̆ˈtäp̚ jɤrt͡ʃinˈwɐp̚ | läʒe̽ni̞t | ɐsˈpɐn | ˈki̞n̠ʃke‿eˌz̥inb | älˈbys tiˈŋ͊e̽n | i̞täfløɡ̟ | gi̞nʲʏ̙rəˈθr̥ɐp̚ | lɐˈti̞kl̩t‿ɔrˌtu | re̞rotʲiˈelɪk t̪ʰr̥østim ulätʲiˈɔk̚ ‖ neɪ̯no̞k ɪkĭ̞ˈnˑɔns dʲyke ˈgɪɫgʃ̟ɯ̽̆d ˈsb̥ɫ̩gɯ̽̆ks ˈkʰɪdɫ̩g ˈgɪɫdgɫ̩g ˈglɪd | e̞fe̞t͡ʃʰ fn̩ˈr̩g gr̩b̥g̊ ‖ θr̥esiˈpiː nosuˈkɐk̚ tivitʲiˑ‿e̞mäˈresˑ‿eɪ̯vˈdir‿ekˈfi̞s‿iˈkapl‿ɐsʊrˈvɪm‿ɐso̞t͡ʃɪ̆sœː | motʲi.oˈnɐp̚ le.ɐˈsɯ̽rt r̥uːd͡ʒ roˈtʲi t͡ʃʊmɪliː ‖ ɐtʲi.ʊ̆k̚ noˑˈle̞d̥ktʰ hɐθ plɐɪ̯ˈpleːɐ̯ sɪnt ˈsädɪs ti̞do̞ˈmɪn ɐntʰˈnɔn ɛkˈti̞v d͡ʒɨˈt͡ʃetfle hɐt͡ʃˈmiːr bleɪ̯t͡ʃʒ̩̊̆t͡ʃfn̩ kr̩ˈbɐɪ̯t̚ deˈki̞d̥s bˠo bɐt͡ʃθ ‖ mäˈnɔθ‿esˌprɑːk̚ tɪt͡ʃə̆ˈkɐrse̽ɪ ˈnɪfɪkä n̥eːɐ̯ɫ t̪ʰr̥ɪskʰ | nɔˈnɪd͡f beːs̬i ˈjetkfsɛː]')
  elif format == 'braille':
    await ctx.send ('⠞⠓⠠⠏⠕⠑⠕⠀⠞⠓⠠⠉⠕⠉⠁⠝⠀⠠⠁⠇⠞⠕⠗⠝⠀⠠⠕⠝⠑⠉⠍⠙⠋⠀⠠⠃⠑⠉⠀⠠⠃⠋⠞⠋\n\n⠠⠉⠕⠉⠁⠝⠃⠀⠁⠇⠞⠕⠗⠞⠂⠀⠥⠗⠏⠑⠝⠊⠞⠕⠗⠞⠀⠥⠗⠕⠙⠊⠉⠞⠕⠗⠞⠀⠥⠗⠊⠎⠑⠭⠥⠀⠁⠁⠉⠀⠞⠊⠧⠊⠞⠊⠝⠀⠧⠕⠇⠧⠊⠝⠁⠏⠀⠏⠇⠊⠉⠁⠞⠀⠊⠕⠕⠏⠁⠊⠕⠉⠀⠕⠝⠎⠞⠀⠗⠊⠉⠞⠊⠕⠞⠀⠞⠓⠏⠑⠝⠊⠀⠕⠞⠑⠎⠀⠞⠊⠉⠇⠑⠝⠀⠕⠝⠅⠙⠙⠀⠉⠇⠙⠑⠛⠎⠑⠀⠑⠛⠗⠃⠅⠀⠙⠑⠛⠎⠃⠁⠁⠇⠀⠋⠽⠓⠛⠊⠝⠅⠋⠀⠃⠝⠙⠗⠃⠝⠀⠇⠕⠃⠑⠉⠀⠎⠑⠗⠃⠎⠊⠲⠀⠠⠞⠓⠊⠍⠁⠊⠝⠀⠧⠕⠇⠧⠙⠊⠗⠀⠑⠉⠞⠇⠏⠁⠀⠊⠝⠋⠥⠁⠉⠀⠞⠊⠧⠊⠞⠊⠂⠀⠑⠎⠥⠉⠁⠛⠀⠑⠝⠊⠞⠁⠏⠀⠊⠑⠗⠉⠊⠝⠺⠁⠏⠂⠀⠇⠁⠛⠑⠝⠊⠞⠂⠀⠁⠎⠏⠁⠝⠂⠀⠅⠊⠝⠎⠟⠥⠑⠀⠑⠵⠊⠝⠃⠂⠀⠁⠇⠃⠥⠎⠀⠞⠊⠝⠛⠑⠝⠂⠀⠊⠞⠁⠋⠇⠕⠛⠂⠀⠛⠊⠝⠥⠗⠑⠞⠓⠗⠁⠏⠂⠀⠇⠁⠞⠊⠉⠅⠇⠞⠀⠕⠗⠞⠥⠂⠀⠗⠑⠗⠕⠞⠊⠑⠇⠑⠉⠀⠞⠗⠕⠎⠞⠊⠍⠀⠥⠇⠁⠞⠊⠕⠅⠂⠀⠝⠑⠑⠊⠝⠕⠅⠀⠊⠉⠅⠊⠝⠝⠕⠝⠎⠀⠙⠽⠉⠑⠀⠛⠽⠓⠇⠛⠎⠚⠓⠙⠀⠎⠃⠇⠛⠛⠓⠭⠀⠉⠽⠙⠇⠛⠛⠓⠀⠛⠊⠇⠙⠛⠛⠇⠛⠀⠛⠓⠇⠓⠽⠙⠀⠑⠋⠑⠛⠉⠀⠋⠝⠗⠛⠀⠛⠗⠃⠛⠛⠲⠀⠠⠞⠓⠗⠑⠉⠊⠏⠊⠑⠀⠝⠕⠎⠥⠉⠁⠉⠀⠞⠊⠧⠊⠞⠊⠀⠑⠍⠁⠗⠑⠉⠀⠑⠊⠧⠙⠊⠗⠀⠑⠉⠏⠓⠽⠎⠀⠊⠉⠁⠏⠇⠑⠀⠁⠎⠥⠗⠧⠊⠍⠀⠁⠎⠕⠉⠓⠊⠎⠕⠑⠂⠀⠍⠕⠞⠊⠕⠝⠁⠏⠀⠇⠑⠁⠎⠥⠗⠞⠀⠓⠗⠕⠥⠛⠑⠀⠗⠕⠞⠊⠀⠉⠓⠥⠍⠊⠇⠊⠂⠀⠁⠞⠊⠕⠕⠅⠀⠝⠕⠺⠇⠑⠙⠛⠞⠀⠓⠁⠞⠓⠀⠏⠇⠁⠊⠏⠇⠑⠁⠀⠎⠊⠝⠞⠀⠎⠁⠙⠊⠎⠀⠞⠊⠙⠕⠍⠊⠝⠀⠁⠝⠞⠝⠕⠝⠀⠑⠉⠞⠊⠋⠃⠓⠀⠙⠎⠚⠽⠉⠑⠛⠞⠋⠇⠓⠑⠀⠓⠁⠉⠍⠊⠗⠀⠃⠇⠊⠑⠓⠓⠛⠉⠇⠉⠋⠝⠀⠅⠗⠃⠑⠊⠞⠀⠙⠑⠉⠽⠙⠎⠀⠃⠛⠓⠕⠀⠃⠁⠁⠉⠓⠞⠓⠲⠀⠠⠍⠁⠝⠕⠞⠓⠀⠑⠎⠏⠗⠁⠉⠀⠞⠊⠉⠑⠉⠁⠗⠗⠎⠊⠛⠀⠝⠊⠋⠊⠉⠁⠀⠝⠓⠑⠁⠇⠀⠞⠗⠊⠎⠅⠀⠝⠕⠝⠽⠙⠋⠀⠃⠑⠑⠎⠊⠀⠽⠑⠞⠅⠓⠋⠎⠑⠲')
  else:
    await ctx.send ('Invalid format')

keep_alive()
bot.run(TOKEN)
