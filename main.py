from pytube import YouTube
from historique import*
from modifVideo import*

# URL de la vidéo YouTube à télécharger
video1_url = input("entré le liens de la vidéo principal ici:")
video2_url = input("entré le liens de la vidéo inférieur ici:")

nomVideo = input("entré le nom de la vidéo ici:")

if recherche_video("list.txt",video1_url)==True:
    # Téléchargement de la vidéo suppérieur
    yt = YouTube(video1_url)
    stream = yt.streams.first()
    stream.download(output_path=f'Video/{nomVideo}', filename=f'{nomVideo}.mp4')
    print("La vidéo principal est téléchargé")
    
    # Téléchargement de la vidéo inférieur
    yt = YouTube(video2_url)
    stream = yt.streams.first()
    stream.download(output_path=f'Video/{nomVideo}', filename=f'VideoInf.mp4')
    print("La vidéo inférieur est téléchargé")
    
else:
    print("La vidéo a déja été téléchargé")

chemin =f'Video/{nomVideo}'
video1 = f'{chemin}/{nomVideo}.mp4'  
video2 = f'{chemin}/VideoInf.mp4'

superposer(video1,video2,chemin)


video = f'{chemin}/video_superposee.mp4'

couper_video(video,chemin)
