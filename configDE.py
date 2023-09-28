import random
token = '6534499024:AAGhXpMnyUctJ6iaWDXaqOdKLTOTSL4fysg'
gif = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Rotating_earth_%28large%29.gif/274px-Rotating_earth_%28large%29.gif'
def get_random_audio():

    # links_of_audio = ['https://raw.githubusercontent.com/AND1ofthewrld/DeminTGBot/a3dbbadac80d78af7d07fbb89fb8e26cd47d656d/BennyBenassiFeat.Gary%20Go_Cinema.mp3',
    #                   'https://raw.githubusercontent.com/AND1ofthewrld/DeminTGBot/blob/a3dbbadac80d78af7d07fbb89fb8e26cd47d656d/CalvinHarris%20_Pray.mp3']
    #
    # random_link = random.choice(links_of_audio)
    # return random_link
    link = 'https://github.com/AND1ofthewrld/DeminTGBot/raw/a3dbbadac80d78af7d07fbb89fb8e26cd47d656d/BennyBenassiFeat.Gary%20Go_Cinema.mp3'
    return link
def get_random_photo():
    mass_photo = ['https://lh6.googleusercontent.com/cJVy4vk4etKXoT0lvKDVTgcctVaez6f4Im2EM2U4SPomoK84iwdwDJQivZWksR9vAt09DYIjmin19y5EQDmUzh18dCUdXeac8Ts0YDUPusTI3uZmZeqjwqwQp2EPd_IVElBziV9bUrIruQuWyg',
                  'https://a.d-cd.net/826fd84s-960.jpg','https://cs7.pikabu.ru/post_img/big/2017/10/25/9/150894277615715407.jpg',
                  'https://rider-skill.ru/wp-content/uploads/2020/08/mount-fuji-1313x875-1.jpg',
                  'https://fototips.ru/wp-content/uploads/2018/05/image7.jpg']
    random_photo = random.choice(mass_photo)
    return random_photo