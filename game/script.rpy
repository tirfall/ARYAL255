# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg mainroomcrew = "images/Bg/mainroomcrew.jpg"
image bg dictor = "images/Bg/dictor.jpg"
image bg rocketstart = "images/Bg/rocketstart.jpg"
default protocols_read = False
define d = Character("Диктор" )
define j = Character("Жанна")
define l = Character("Лео")
image janna = "images/Characters/janna.png"
image leo = "images/Characters/leo.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene
    show bg dictor

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    d "2471 год. 15 июня."
    d "Сегодня восемь первооткрывателей покидают Землю."
    d "Впервые в истории человечества они пересекут такое расстояние в глубоком космосе."
    d "Их миссия — найти новый дом. Для нас. Для наших детей."
    d "Давайте же возрадуемся новой главе человеческой истории."

    scene bg rocketstart
    d "Вот-вот и запуск ракеты стартует!"
    d "3..."
    d "2..."
    d "1..."
    "......"
    
    play sound "Sounds/rocketlaunch.mp3"
    
    scene bg mainroomcrew

    show leo
    show janna
    j "Добро пожаловать на борт. Меня зовут Жанна Адельман. С этого момента — я ваш капитан.
Лео — мой заместитель. Он отвечает за навигацию и безопасность."
    l "Рад знакомству. Мы здесь не ради личных рекордов. Только как команда мы сможем выжить — и выполнить миссию."
    j "Уверена, вы все ознакомлены со своими ролями.
Это будет долгое и сложное путешествие.
Вы обязаны знать аварийные протоколы. Они уже отправлены в ваш интерфейс."
    
    #choice to read manual

    menu:
        "Прочитать аварийные протоколы?"

        "Да, изучить протокол":
            $ protocols_read = True
            
            "Вы открываете интерфейс и внимательно изучаете каждый пункт."
            """ 
            Дыры заделывай.
            Мусор выкидывай.
            Окна не открывай.
            Пиво не пей.
            Не падай.

            """

        "Нет, потом как-нибудь":
            $ protocols_read = False

            "Вы закрываете уведомление. Всё это можно будет посмотреть позже..."
    


    j "Расположитесь. Через полчаса начнётся распаковка модулей, медосмотры и первичный осмотр станции.
Удачи. И не забывайте: вы — лицо человечества. Мы одни, и мы вместе."
    l "Надеюсь, вы оказались теми, кого действительно стоит было послать."

    return
