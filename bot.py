import discord
from discord.ext import commands
import random
import re
import os

# ─────────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────────
TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ─────────────────────────────────────────────
#  Sourates
# ─────────────────────────────────────────────
SOURATES = [
    {
        "numero": 1,
        "nom_ar": "الفاتحة",
        "nom_fr": "Al-Fatiha (L'Ouverture)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ\n"
            "الرَّحْمَٰنِ الرَّحِيمِ\n"
            "مَالِكِ يَوْمِ الدِّينِ\n"
            "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ\n"
            "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ\n"
            "صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Louange à Allah, Seigneur de l'univers,\n"
            "le Tout Miséricordieux, le Très Miséricordieux,\n"
            "Maître du Jour de la rétribution.\n"
            "C'est Toi [Seul] que nous adorons, et c'est Toi [Seul] dont nous implorons le secours.\n"
            "Guide-nous dans le droit chemin,\n"
            "le chemin de ceux que Tu as comblés de bienfaits, non pas de ceux qui ont encouru Ta colère, ni des égarés."
        ),
    },
    {
        "numero": 112,
        "nom_ar": "الإخلاص",
        "nom_fr": "Al-Ikhlas (Le Monothéisme pur)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "قُلْ هُوَ اللَّهُ أَحَدٌ\n"
            "اللَّهُ الصَّمَدُ\n"
            "لَمْ يَلِدْ وَلَمْ يُولَدْ\n"
            "وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Dis : « Il est Allah, Unique.\n"
            "Allah, le Seul à être imploré pour ce que nous désirons.\n"
            "Il n'a pas engendré, n'a pas été engendré non plus.\n"
            "Et nul n'est égal à Lui. »"
        ),
    },
    {
        "numero": 113,
        "nom_ar": "الفلق",
        "nom_fr": "Al-Falaq (L'Aube naissante)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ\n"
            "مِن شَرِّ مَا خَلَقَ\n"
            "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ\n"
            "وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ\n"
            "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Dis : « Je cherche protection auprès du Seigneur de l'aube naissante,\n"
            "contre le mal de ce qu'Il a créé,\n"
            "et contre le mal de l'obscurité quand elle s'étend,\n"
            "et contre le mal de celles qui soufflent (les sorcières) sur les nœuds,\n"
            "et contre le mal de l'envieux quand il envie. »"
        ),
    },
    {
        "numero": 114,
        "nom_ar": "الناس",
        "nom_fr": "An-Nas (Les Hommes)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "قُلْ أَعُوذُ بِرَبِّ النَّاسِ\n"
            "مَلِكِ النَّاسِ\n"
            "إِلَٰهِ النَّاسِ\n"
            "مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ\n"
            "الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ\n"
            "مِنَ الْجِنَّةِ وَالنَّاسِ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Dis : « Je cherche protection auprès du Seigneur des hommes,\n"
            "du Roi des hommes,\n"
            "du Dieu des hommes,\n"
            "contre le mal du mauvais conseiller furtif\n"
            "qui souffle le mal dans les poitrines des hommes,\n"
            "qu'il soit djinn ou homme. »"
        ),
    },
    {
        "numero": 36,
        "nom_ar": "يس",
        "nom_fr": "Ya-Sin",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "يس\n"
            "وَالْقُرْآنِ الْحَكِيمِ\n"
            "إِنَّكَ لَمِنَ الْمُرْسَلِينَ\n"
            "عَلَىٰ صِرَاطٍ مُّسْتَقِيمٍ\n"
            "تَنزِيلَ الْعَزِيزِ الرَّحِيمِ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Yâ-Sîn.\n"
            "Par le Coran plein de sagesse,\n"
            "tu es certes du nombre des Envoyés,\n"
            "sur une voie droite.\n"
            "[C'est] une révélation du Tout Puissant, du Très Miséricordieux."
        ),
    },
    {
        "numero": 55,
        "nom_ar": "الرحمن",
        "nom_fr": "Ar-Rahman (Le Tout Miséricordieux)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "الرَّحْمَٰنُ\n"
            "عَلَّمَ الْقُرْآنَ\n"
            "خَلَقَ الْإِنسَانَ\n"
            "عَلَّمَهُ الْبَيَانَ\n"
            "فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Le Tout Miséricordieux\n"
            "a enseigné le Coran,\n"
            "a créé l'homme,\n"
            "lui a appris à s'exprimer clairement.\n"
            "Alors, lequel des bienfaits de votre Seigneur nierez-vous tous les deux ?"
        ),
    },
    {
        "numero": 67,
        "nom_ar": "الملك",
        "nom_fr": "Al-Mulk (La Royauté)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "تَبَارَكَ الَّذِي بِيَدِهِ الْمُلْكُ وَهُوَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ\n"
            "الَّذِي خَلَقَ الْمَوْتَ وَالْحَيَاةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًا ۚ وَهُوَ الْعَزِيزُ الْغَفُورُ\n"
            "الَّذِي خَلَقَ سَبْعَ سَمَاوَاتٍ طِبَاقًا ۖ مَّا تَرَىٰ فِي خَلْقِ الرَّحْمَٰنِ مِن تَفَاوُتٍ ۖ فَارْجِعِ الْبَصَرَ هَلْ تَرَىٰ مِن فُطُورٍ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Béni soit Celui en la main de qui est la royauté. Et Il est Omnipotent.\n"
            "Celui qui a créé la mort et la vie afin de vous éprouver et de savoir qui de vous est le meilleur en œuvres. Et Il est le Puissant, le Pardonneur.\n"
            "Celui qui a créé sept cieux superposés. Tu ne vois aucune disparité dans la création du Tout Miséricordieux ; ramène donc ton regard : y vois-tu une fissure ?"
        ),
    },
    {
        "numero": 2,
        "nom_ar": "البقرة",
        "nom_fr": "Al-Baqara — Ayat Al-Kursi (2:255)",
        "texte": (
            "﴿آيَةُ الْكُرْسِيِّ﴾\n"
            "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ۚ\n"
            "لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ ۚ\n"
            "لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ ۗ\n"
            "مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ ۚ\n"
            "يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ ۖ\n"
            "وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ ۚ\n"
            "وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ ۖ\n"
            "وَلَا يَئُودُهُ حِفْظُهُمَا ۚ وَهُوَ الْعَلِيُّ الْعَظِيمُ"
        ),
        "traduction": (
            "Verset du Trône\n"
            "Allah ! Point de divinité à part Lui, le Vivant, Celui qui subsiste par lui-même.\n"
            "Ni somnolence ni sommeil ne Le saisissent.\n"
            "À Lui appartient tout ce qui est dans les cieux et sur la terre.\n"
            "Qui peut intercéder auprès de Lui sans Sa permission ?\n"
            "Il sait ce qui est devant eux et ce qui est derrière eux.\n"
            "Son Trône est plus vaste que les cieux et la terre, dont la garde ne Lui coûte aucune peine.\n"
            "Et Il est le Très Haut, le Très Grand."
        ),
    },
    {
        "numero": 18,
        "nom_ar": "الكهف",
        "nom_fr": "Al-Kahf (La Caverne) — début",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "الْحَمْدُ لِلَّهِ الَّذِي أَنزَلَ عَلَىٰ عَبْدِهِ الْكِتَابَ وَلَمْ يَجْعَل لَّهُ عِوَجًا\n"
            "قَيِّمًا لِّيُنذِرَ بَأْسًا شَدِيدًا مِّن لَّدُنْهُ وَيُبَشِّرَ الْمُؤْمِنِينَ الَّذِينَ يَعْمَلُونَ الصَّالِحَاتِ أَنَّ لَهُمْ أَجْرًا حَسَنًا\n"
            "مَّاكِثِينَ فِيهِ أَبَدًا"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Louange à Allah qui a fait descendre sur Son serviteur le Livre, sans y mettre d'ambiguïté,\n"
            "[un Livre] droit, pour avertir d'un châtiment sévère de Sa part, et annoncer aux croyants qui font de bonnes œuvres qu'ils auront une belle récompense,\n"
            "où ils demeureront éternellement."
        ),
    },
    {
        "numero": 56,
        "nom_ar": "الواقعة",
        "nom_fr": "Al-Waqi'a (L'Événement)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "إِذَا وَقَعَتِ الْوَاقِعَةُ\n"
            "لَيْسَ لِوَقْعَتِهَا كَاذِبَةٌ\n"
            "خَافِضَةٌ رَّافِعَةٌ\n"
            "إِذَا رُجَّتِ الْأَرْضُ رَجًّا\n"
            "وَبُسَّتِ الْجِبَالُ بَسًّا\n"
            "فَكَانَتْ هَبَاءً مُّنبَثًّا"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Quand l'Événement arrivera,\n"
            "nul ne pourra nier son avènement,\n"
            "abaissant [les uns], élevant [les autres].\n"
            "Quand la terre sera secouée d'un violent séisme,\n"
            "et que les montagnes seront réduites en poussière,\n"
            "et deviendront une poussière dispersée."
        ),
    },
    {
        "numero": 73,
        "nom_ar": "المزمل",
        "nom_fr": "Al-Muzzammil (L'Enveloppé)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "يَا أَيُّهَا الْمُزَّمِّلُ\n"
            "قُمِ اللَّيْلَ إِلَّا قَلِيلًا\n"
            "نِّصْفَهُ أَوِ انقُصْ مِنْهُ قَلِيلًا\n"
            "أَوْ زِدْ عَلَيْهِ وَرَتِّلِ الْقُرْآنَ تَرْتِيلًا\n"
            "إِنَّا سَنُلْقِي عَلَيْكَ قَوْلًا ثَقِيلًا"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Ô toi l'enveloppé [dans tes vêtements] !\n"
            "Lève-toi [pour prier] la nuit, sauf une petite partie,\n"
            "la moitié, ou un peu moins,\n"
            "ou un peu plus. Et récite le Coran lentement et distinctement.\n"
            "Car Nous allons te révéler des paroles de grand poids."
        ),
    },
    {
        "numero": 74,
        "nom_ar": "المدثر",
        "nom_fr": "Al-Muddaththir (Le Revêtu d'un manteau)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "يَا أَيُّهَا الْمُدَّثِّرُ\n"
            "قُمْ فَأَنذِرْ\n"
            "وَرَبَّكَ فَكَبِّرْ\n"
            "وَثِيَابَكَ فَطَهِّرْ\n"
            "وَالرُّجْزَ فَاهْجُرْ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Ô toi le revêtu d'un manteau !\n"
            "Lève-toi et avertis.\n"
            "Et ton Seigneur, magnifie-Le.\n"
            "Et tes vêtements, purifie-les.\n"
            "Et les souillures, éloigne-toi en."
        ),
    },
    {
        "numero": 93,
        "nom_ar": "الضحى",
        "nom_fr": "Ad-Duha (La Matinée)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "وَالضُّحَىٰ\n"
            "وَاللَّيْلِ إِذَا سَجَىٰ\n"
            "مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَىٰ\n"
            "وَلَلْآخِرَةُ خَيْرٌ لَّكَ مِنَ الْأُولَىٰ\n"
            "وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Par la matinée,\n"
            "et par la nuit quand elle étend son calme !\n"
            "Ton Seigneur ne t'a pas abandonné, et Il ne t'a pas oublié.\n"
            "Et certes, la vie future sera meilleure pour toi que la première.\n"
            "Et certes, ton Seigneur te donnera, et tu seras satisfait."
        ),
    },
    {
        "numero": 94,
        "nom_ar": "الشرح",
        "nom_fr": "Ash-Sharh (L'Expansion)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ\n"
            "وَوَضَعْنَا عَنكَ وِزْرَكَ\n"
            "الَّذِي أَنقَضَ ظَهْرَكَ\n"
            "وَرَفَعْنَا لَكَ ذِكْرَكَ\n"
            "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا\n"
            "إِنَّ مَعَ الْعُسْرِ يُسْرًا\n"
            "فَإِذَا فَرَغْتَ فَانصَبْ\n"
            "وَإِلَىٰ رَبِّكَ فَارْغَب"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "N'avons-Nous pas déployé ta poitrine,\n"
            "et déposé de toi ton fardeau\n"
            "qui accablait ton dos ?\n"
            "Et hissé haut ta renommée ?\n"
            "Certes, avec la difficulté vient la facilité.\n"
            "Certes, avec la difficulté vient la facilité.\n"
            "Alors, quand tu te libères [de tes occupations], affaire-toi [à la prière],\n"
            "et aspire ardemment à ton Seigneur."
        ),
    },
    {
        "numero": 108,
        "nom_ar": "الكوثر",
        "nom_fr": "Al-Kawthar (L'Abondance)",
        "texte": (
            "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n"
            "إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ\n"
            "فَصَلِّ لِرَبِّكَ وَانْحَرْ\n"
            "إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ"
        ),
        "traduction": (
            "Au nom d'Allah, le Tout Miséricordieux, le Très Miséricordieux.\n"
            "Nous t'avons certes donné l'Abondance.\n"
            "Accomplis donc la Salât pour ton Seigneur et sacrifie.\n"
            "C'est bien ton ennemi qui est sans postérité."
        ),
    },
]

# ─────────────────────────────────────────────
#  Détection — toutes les combinaisons possibles
# ─────────────────────────────────────────────
MOTS_CLES = re.compile(
    r"""
    (?:
        # Variantes latines : wallah, wallahi, w'allah, w'llah, wAllah, WALLAH...
        [Ww][Aa][Ll]{1,2}[Aa][Hh][Ii]?           |   # wallah / wallahi
        [Ww][''\u2019\u02bc]?[Aa][Ll]{1,2}[Aa][Hh][Ii]?  |   # w'allah / w'llah
        [Ww][Aa][Ll]{1,2}[Aa][Hh][Ii]?           |   # wallah sans apostrophe
        # "jure sur allah" / "je jure sur allah" / "jure par allah"
        (?:je\s+)?jure\s+(?:sur|par)\s+[Aa]ll[aâ]h  |
        # Mix latin+arabe : w'الله / W'الله / wالله / wallالله
        [Ww][''\u2019\u02bc]?\s*\u0627\u0644\u0644\u0647  |   # w'الله
        [Ww][Aa][Ll]?\s*\u0627\u0644\u0644\u0647  |   # walالله
        # Arabe pur : والله
        \u0648\u0627\u0644\u0644\u0647              |   # والله
        # وَاللَّهِ avec diacritiques
        \u0648\u064e\u0627\u0644\u0644\u0651\u064e\u0647\u0650
    )
    """,
    re.VERBOSE | re.UNICODE,
)


def build_embed(sourate: dict) -> discord.Embed:
    embed = discord.Embed(
        title=f"📖 Sourate {sourate['numero']} — {sourate['nom_ar']}",
        description=f"**{sourate['nom_fr']}**",
        color=0x1a6b3c,
    )
    embed.add_field(name="🕌 Texte arabe", value=sourate["texte"], inline=False)
    embed.add_field(name="🇫🇷 Traduction", value=sourate["traduction"], inline=False)
    embed.set_footer(text="بارك الله فيك • Qu'Allah vous bénisse")
    return embed


# ─────────────────────────────────────────────
#  Événements
# ─────────────────────────────────────────────
@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user} (ID: {bot.user.id})")
    print("─────────────────────────────────────────────")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if MOTS_CLES.search(message.content):
        sourate = random.choice(SOURATES)
        await message.channel.send(
            f"🌙 *{message.author.display_name}* a mentionné Allah — voici une sourate :",
            embed=build_embed(sourate),
        )

    await bot.process_commands(message)


# ─────────────────────────────────────────────
#  Commandes
# ─────────────────────────────────────────────
@bot.command(name="sourate")
async def sourate_cmd(ctx: commands.Context):
    sourate = random.choice(SOURATES)
    await ctx.send(
        f"📖 Voici une sourate pour toi, {ctx.author.mention} :",
        embed=build_embed(sourate),
    )


@bot.command(name="liste")
async def liste_cmd(ctx: commands.Context):
    lignes = [f"**{s['numero']}** — {s['nom_ar']} ({s['nom_fr']})" for s in SOURATES]
    embed = discord.Embed(
        title="📚 Sourates disponibles",
        description="\n".join(lignes),
        color=0x1a6b3c,
    )
    await ctx.send(embed=embed)


# ─────────────────────────────────────────────
#  Lancement
# ─────────────────────────────────────────────
bot.run(TOKEN)

