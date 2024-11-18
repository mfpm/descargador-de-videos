from pytube import YouTube 


def  accion(link):
     video= YouTube(link)
     stream=video.streams.get_highest_resolution()
     stream.download()
     print("Descarga exitosa")

enlace=input('Ingresa la url del video: ')

accion(enlace)