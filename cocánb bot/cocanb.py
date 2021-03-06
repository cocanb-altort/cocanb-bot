import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*', description='A bot for members of the Cocánb')

class Cocanb(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @bot.command(name='cocanb', help='Sends thPoéo thCocán Altorn Onécmdf Bec Bftf')
  async def cocanb (self, ctx, format: str=None):
    if format is None:
      await ctx.send ('thPoéo thCocán Altorn Onécmdf Bec Bftf\n\nCocánb altort, ürpenîtort ürodictort ürişêxu áaç tivitin volvinãp plicat īóopaioc onşt rictiot thpení otês ticlen onkdd cłdeğse egřbk degsbáal fýhginkf bňdřbň lobec seřbsi. Thîmain vòlvdir ectlpá infuác tiviti, esücağ énitap iercinŵap, lagenít, aspan, kiñşqué ezinb, albüs tingen, itafløg, ginürethrap, latickłt ortú, rerotielec trøstim ulatiok, néeinok ickinnons dýce gýhlgşjħd sbłggħx cýdłggh gildggłg ghlhýd efegč fňřg gřbgg. Thrécipie nosûcác tiviti émareç eivdir ecphýş icaple asurvim asochísœ, motionâp leasürt hrouğe rôti chumili, atióok noŵledgt hath plaipléa sint sadis tidomin antnon ectifbh dşjýčeğtflħe hačmir bliehhğclčfň křbeit decýds bgho báachth. Manóth éspraç tičecarrsiğ nifîca nħéal trisk nonýdf béesi yetkħfse.')
    elif format == 'ipa':
      await ctx.send ('[θ‿poˈe̯.o̞̯ θ‿koˈkɐn älˈtorn‿ɔnɛkm̩df bek.ˈbf̩tf̩]\n\n[ko̞ˈkɐnb ʔälˈtort | ˈʔyrpeni̞ˌtort‿yrodi̞k̚ˈtort‿yrɪʃe̞ksu ʔʌsˑ ˌtɪvɪˈtʲɪn vɤɫviˈnʌ̃ᵐp pliˈkɐt joːpɐˈjok‿on̠ʃt ri̞kˈtʲjot θ‿ˈpe̞ni o̞ˈte̙ʃ ‖ ti̞klen ʔo̞ŋkt | kl̩ˈdeɪ̯s̬ə‿eˈɡr̩b̥k deg̊sˈbaˑɫ fy̞̆ˈgi̞nk͡f | ˈbn̩dr̩ˌbn̩ lɔ̞ˈbe̞k̚ ˈse̞.r̩b.siˑ ‖ tʰɪˈmɐɪ̯n vo̞ɫvˈdiːr ekt͡ɬˈpä ɪnˈfʷɐk̚ tiviˈtʲiː | e̞sʉˈkäɪ̯ e̞nɪ̆ˈtäp̚ jɤrt͡ʃinˈwɐp̚ | läʒe̽ni̞t | ɐsˈpɐn | ˈki̞n̠ʃke‿eˌz̥inb | älˈbys tiˈŋe̽n | i̞täfløɡ̟ | gi̞nʲʏ̙rəˈθr̥ɐp̚ | lɐˈti̞kl̩t‿ɔrˌtu | re̞roˈtʲjelɪk t̪ʰr̥østim uläˈtʲjɔk̚ ‖ neɪ̯no̞k ɪkĭ̞ˈnˑɔns dʲyke ˈgɪɫgʃ̟ɯ̽̆d ˈsb̥ɫ̩gɯ̽̆ks ˈkʰɪdɫ̩g ˈgɪɫdgɫ̩g ˈglɪd | e̞fe̞t͡ʃʰ fn̩ˈr̩g gr̩b̥g̊ ‖ θr̥esiˈpiː nosuˈkɐk̚ tivitʲiˑ‿e̞mäˈresˑ‿eɪ̯vˈdir‿ekˈfi̞s‿iˈkapl‿ɐsʊrˈvɪm‿ɐso̞t͡ʃɪ̆sœː | motʲjoˈnɐp̚ le.ɐˈsɯ̽rt r̥uːd͡ʒ roˈtʲi t͡ʃʊmɪliː ‖ ɐtʲjʊ̆k̚ noˑˈle̞d̥ktʰ hɐθ plɐɪ̯ˈpleːɐ̯ sɪnt ˈsädɪs ti̞do̞ˈmɪn ɐntʰˈnɔn ɛkˈti̞v d͡ʒɨˈt͡ʃetfle hɐt͡ʃˈmiːr bleɪ̯t͡ʃʒ̩̊̆t͡ʃfn̩ kr̩ˈbɐɪ̯t̚ deˈki̞d̥s bˠo bɐt͡ʃθ ‖ mäˈnɔθ‿esˌprɑːk̚ tɪt͡ʃə̆ˈkɐrse̽ɪ ˈnɪfɪkä n̥eːɐ̯ɫ t̪ʰr̥ɪskʰ | nɔˈnɪd͡f beːs̬i ˈjetkfsɛː]')
    elif format == 'braille':
      await ctx.send ('⠞⠓⠠⠏⠕⠑⠕⠀⠞⠓⠠⠉⠕⠉⠁⠝⠀⠠⠁⠇⠞⠕⠗⠝⠀⠠⠕⠝⠑⠉⠍⠙⠋⠀⠠⠃⠑⠉⠀⠠⠃⠋⠞⠋\n\n⠠⠉⠕⠉⠁⠝⠃⠀⠁⠇⠞⠕⠗⠞⠂⠀⠥⠗⠏⠑⠝⠊⠞⠕⠗⠞⠀⠥⠗⠕⠙⠊⠉⠞⠕⠗⠞⠀⠥⠗⠊⠎⠑⠭⠥⠀⠁⠁⠉⠀⠞⠊⠧⠊⠞⠊⠝⠀⠧⠕⠇⠧⠊⠝⠁⠏⠀⠏⠇⠊⠉⠁⠞⠀⠊⠕⠕⠏⠁⠊⠕⠉⠀⠕⠝⠎⠞⠀⠗⠊⠉⠞⠊⠕⠞⠀⠞⠓⠏⠑⠝⠊⠀⠕⠞⠑⠎⠀⠞⠊⠉⠇⠑⠝⠀⠕⠝⠅⠙⠙⠀⠉⠇⠙⠑⠛⠎⠑⠀⠑⠛⠗⠃⠅⠀⠙⠑⠛⠎⠃⠁⠁⠇⠀⠋⠽⠓⠛⠊⠝⠅⠋⠀⠃⠝⠙⠗⠃⠝⠀⠇⠕⠃⠑⠉⠀⠎⠑⠗⠃⠎⠊⠲⠀⠠⠞⠓⠊⠍⠁⠊⠝⠀⠧⠕⠇⠧⠙⠊⠗⠀⠑⠉⠞⠇⠏⠁⠀⠊⠝⠋⠥⠁⠉⠀⠞⠊⠧⠊⠞⠊⠂⠀⠑⠎⠥⠉⠁⠛⠀⠑⠝⠊⠞⠁⠏⠀⠊⠑⠗⠉⠊⠝⠺⠁⠏⠂⠀⠇⠁⠛⠑⠝⠊⠞⠂⠀⠁⠎⠏⠁⠝⠂⠀⠅⠊⠝⠎⠟⠥⠑⠀⠑⠵⠊⠝⠃⠂⠀⠁⠇⠃⠥⠎⠀⠞⠊⠝⠛⠑⠝⠂⠀⠊⠞⠁⠋⠇⠕⠛⠂⠀⠛⠊⠝⠥⠗⠑⠞⠓⠗⠁⠏⠂⠀⠇⠁⠞⠊⠉⠅⠇⠞⠀⠕⠗⠞⠥⠂⠀⠗⠑⠗⠕⠞⠊⠑⠇⠑⠉⠀⠞⠗⠕⠎⠞⠊⠍⠀⠥⠇⠁⠞⠊⠕⠅⠂⠀⠝⠑⠑⠊⠝⠕⠅⠀⠊⠉⠅⠊⠝⠝⠕⠝⠎⠀⠙⠽⠉⠑⠀⠛⠽⠓⠇⠛⠎⠚⠓⠙⠀⠎⠃⠇⠛⠛⠓⠭⠀⠉⠽⠙⠇⠛⠛⠓⠀⠛⠊⠇⠙⠛⠛⠇⠛⠀⠛⠓⠇⠓⠽⠙⠀⠑⠋⠑⠛⠉⠀⠋⠝⠗⠛⠀⠛⠗⠃⠛⠛⠲⠀⠠⠞⠓⠗⠑⠉⠊⠏⠊⠑⠀⠝⠕⠎⠥⠉⠁⠉⠀⠞⠊⠧⠊⠞⠊⠀⠑⠍⠁⠗⠑⠉⠀⠑⠊⠧⠙⠊⠗⠀⠑⠉⠏⠓⠽⠎⠀⠊⠉⠁⠏⠇⠑⠀⠁⠎⠥⠗⠧⠊⠍⠀⠁⠎⠕⠉⠓⠊⠎⠕⠑⠂⠀⠍⠕⠞⠊⠕⠝⠁⠏⠀⠇⠑⠁⠎⠥⠗⠞⠀⠓⠗⠕⠥⠛⠑⠀⠗⠕⠞⠊⠀⠉⠓⠥⠍⠊⠇⠊⠂⠀⠁⠞⠊⠕⠕⠅⠀⠝⠕⠺⠇⠑⠙⠛⠞⠀⠓⠁⠞⠓⠀⠏⠇⠁⠊⠏⠇⠑⠁⠀⠎⠊⠝⠞⠀⠎⠁⠙⠊⠎⠀⠞⠊⠙⠕⠍⠊⠝⠀⠁⠝⠞⠝⠕⠝⠀⠑⠉⠞⠊⠋⠃⠓⠀⠙⠎⠚⠽⠉⠑⠛⠞⠋⠇⠓⠑⠀⠓⠁⠉⠍⠊⠗⠀⠃⠇⠊⠑⠓⠓⠛⠉⠇⠉⠋⠝⠀⠅⠗⠃⠑⠊⠞⠀⠙⠑⠉⠽⠙⠎⠀⠃⠛⠓⠕⠀⠃⠁⠁⠉⠓⠞⠓⠲⠀⠠⠍⠁⠝⠕⠞⠓⠀⠑⠎⠏⠗⠁⠉⠀⠞⠊⠉⠑⠉⠁⠗⠗⠎⠊⠛⠀⠝⠊⠋⠊⠉⠁⠀⠝⠓⠑⠁⠇⠀⠞⠗⠊⠎⠅⠀⠝⠕⠝⠽⠙⠋⠀⠃⠑⠑⠎⠊⠀⠽⠑⠞⠅⠓⠋⠎⠑⠲')
    else:
      await ctx.send ('Invalid format')

  @bot.command (name="script", help= "Sends the Cocánb symbols\nSupported: cocanb/cocánb, cock, and, ball, torture, shit, cringe, constriction, onomatopoeia/onomatopœia, altort\n(Words separated with / output the same thing)")
  async def script(self, ctx, *, word):
    word = word.lower()
    if word == "cocanb" or word == "cocánb":
      await ctx.send ("<:cocanb:812322440351842365>")
    elif word == "cock":
      await ctx.send ("<:cock:794451604278870026>")
    elif word == "and":
      await ctx.send ("<:and:794451630194950174>")
    elif word == "ball":
      await ctx.send ("<:ball:794451654098419712>")
    elif word == "torture":
      await ctx.send ("<:torture:794451672641961985>")
    elif word == "shit":
      await ctx.send ("<:shit:806451654362136606>")
    elif word == "cringe":
      await ctx.send("<:cringe:801335612699181056>")
    elif word == "constriction":
      await ctx.send("<:constriction:794505293333266432>")
    elif word == "onomatopoeia" or word == "onomatopœia":
      await ctx.send ("<:onomatopoeia:810395187372752946>")
    elif word == "altort":
      await ctx.send ("<:altort:806454273935933460>")
    else:
      await ctx.send ("This word has not been created yet.")
