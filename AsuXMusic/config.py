from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQAmZxM_O6gZprGdNZxZoHwjhIZQ-lKZ0aPz9ATKfncwQXSVw0gPCnUe_SWTPYwNwns0NK2hRsmMdaFAB5PO_0KCsVsTo_3TEHBOGPtgn5x9S0irAfOK6z50cw1zJVuwA5abLiovfm-N0vFxAoRFaXX1IfnqS9liG2wjiqZSPHmEbM8n9w3zlBAOpL4K5P-EnCV6c3lgh2oFWziVd4GibBLa57wKzeH5vZjGraH8TIr24zoP2E7h7u4zf9JgOn-Q9lmUp_fQDOjZu34UyMIrfxLM-JXygXZkNme5Ao0fdLX6nltPLyRB90HRHQFf7H19dRWOy5_3noQwDDOoiXWoAAAAATNT7VoA")

BOT_TOKEN = getenv("BOT_TOKEN", "6072123540:AAGnL13XvbdxN0qCqk0n0CJNnb_Oy7IyfHI")
API_ID = int(getenv("API_ID", "15104173"))
API_HASH = getenv("API_HASH", "6aff375c0543375c5d5949d851dad72c")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "arkonsbotsupport)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "arkonsbotupdate)
OWNER_ID = list(map(int, getenv("OWNER_ID", "5156105562").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5938660179").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
