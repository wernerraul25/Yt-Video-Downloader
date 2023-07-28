import os
from pytube import YouTube

def local_download():
    if os.name == 'posix':  # Verifica se é um sistema tipo Unix (Linux e macOS)
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    elif os.name == 'nt':  # Verifica se é um sistema Windows
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
                download_folder = winreg.QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
                return download_folder
        except Exception as e:
            print(f"Erro ao acessar a pasta de downloads: {e}")
            return None
    else:
        print("Sistema operacional não suportado.")
        return None
def limpar_tela():
    os.system("cls")


#*-*-*-*-*-*-*-*RAUL WERNER*-*-*-*-*-*-*-*

rodando = True
pasta_download = local_download()

while rodando:
    limpar_tela()
    print("Bem vindo ao Downloader de vídeos!")
    opcao = input("Digite (0) para baixar vídeo \nDigite (1) para fechar programa\n")
    print("By: Raul Werner")
    if opcao == "0":
        limpar_tela()
        link = input("Digite o link do vídeo a ser baixado: ")
        yt = YouTube(link)
        titulo = yt.title
        views = yt.views
        autor = yt.author

        print("Título do vídeo:", titulo)
        print("Autor do vídeo:", autor)
        print("Visualizações do vídeo:", views)

        opcao2 = input("Esse é o vídeo correto?\nSe sim digite (0), se não digite(1)\n")
        if opcao2 == "0":
            yd = yt.streams.get_highest_resolution()
            try:
                yd.download(pasta_download)
                print("Local do download: ", pasta_download)
                print("Download concluído com sucesso!")
            except:
                print("Erro no download")
            input("Pressione ENTER para continuar...")
        elif opcao2 == "1":
            pass
        else:
            pass
    elif opcao == "1":
        break
    else:
        pass
limpar_tela()