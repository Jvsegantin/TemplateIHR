# pip install gTTS
from gtts import gTTS

# pip install python-vlc
import vlc
def ao_tocar_tela():
    p = vlc.MediaPlayer("tablet.mp3")
    p.play()


def main():
    tts = gTTS('Sejam bem vindos!!, Por favor selecione no tablet a baixo a sua bebida!', lang ="pt",)
    tts.save('tablet.mp3')
    p = vlc.MediaPlayer("tablet.mp3")
    p.play()

    tts = gTTS('Basta selecionar a bebida e concluir pedido. Depois só esperar que vou começar o preparo!', lang ="pt",)
    tts.save('tablet.mp3')
    p = vlc.MediaPlayer("tablet.mp3")
    p.play()
    
    tts = gTTS('Bebida Pronta! Pegue com cuidado dos meus dedos, pode escorregar!', lang ="pt",)
    tts.save('tablet.mp3')
    p = vlc.MediaPlayer("tablet.mp3")
    p.play()

    tts = gTTS('Espero que tenha gostado! Obrigado e volte sempre!', lang ="pt",)
    tts.save('tablet.mp3')
    p = vlc.MediaPlayer("tablet.mp3")
    p.play()