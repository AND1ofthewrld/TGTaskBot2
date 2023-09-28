import random
token = '6534499024:AAGhXpMnyUctJ6iaWDXaqOdKLTOTSL4fysg'
gif = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Rotating_earth_%28large%29.gif/274px-Rotating_earth_%28large%29.gif'
def get_random_audio():

    links_of_audio = ['https://github.com/AND1ofthewrld/TGTaskBot2/raw/master/BennyBenassiFeat.Gary%20Go_Cinema.mp3',
                      'https://github.com/AND1ofthewrld/TGTaskBot2/raw/master/CalvinHarris%20_Pray.mp3',
                      'https://github.com/AND1ofthewrld/TGTaskBot2/raw/master/Modestep_Snake.mp3',
                      'https://github.com/AND1ofthewrld/TGTaskBot2/raw/master/OhLand_Sun.mp3',
                      'https://github.com/AND1ofthewrld/TGTaskBot2/raw/master/VAMPS%20-%20Wake%20Up%20(supermusic.me).mp3']
    random_link = random.choice(links_of_audio)
    return random_link
def get_random_photo():
    mass_photo = ['https://github.com/AND1ofthewrld/TGTaskBot2/blob/master/%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20(1).jpg?raw=true',
                  'https://github.com/AND1ofthewrld/TGTaskBot2/blob/master/%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20(2).jpg?raw=true',
                  'https://github.com/AND1ofthewrld/TGTaskBot2/blob/master/%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20(3).jpg?raw=true',
                  'https://github.com/AND1ofthewrld/TGTaskBot2/blob/master/%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20(4).jpg?raw=true',
                  'https://github.com/AND1ofthewrld/TGTaskBot2/blob/master/%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.jpg?raw=true']
    random_photo = random.choice(mass_photo)
    return random_photo