![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%235C3EE8.svg?&style=for-the-badge&logo=opencv&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

# :computer: Sobre o Projeto

O projeto foi criado com o intuito de demonstrar o que foi aprendido na materia de Computação Gráfica e Processamento de Imagens.

# :page_facing_up: Proposta
<details>
  <summary><b>Criar um Stories do "Instagram"</b></summary><br />
  
  1. Este projeto tem como objetivo desenvolver uma pequena aplicação que que simule os efeitos e funcionalidades ao estilo Instagram.

  2. A aplicação deve permitir ao usuário:
      - Carregar uma imagem ou vídeo
      - Aplicar diferentes filtros (você deve oferecer pelo menos 4 opções diferentes)
      - Adicionar stickers (figurinhas predefinidas)
      - Adicionar outro elemento a sua escolha (gif, texto, temperatura, local, selfie, etc...)
      - Salvar a foto ou vídeo editado
      - Interação por teclado e/ou mouse
  
  ### Obrigatoriedade
   - Utilizar OpenCV na sua linguagem de preferência.
</details>

# :hammer_and_wrench: Como utilizar a aplicação
- <b>Ambiente:</b> Necessita ter python instalado, OpenCV, TkInter e PIL. 
- <b>Ferramenta:</b> Utilizei o Visual Code como IDE para desenvolver e rodar a aplicação. 
- <b>Rodando o projeto:</b> A tela inicial é a [Menu Oficial](Oficial/menuOficial.py).
- <b>Outros:</b> Usar duas câmeras para poder executar função de inversão de câmera simulando a de perfil.

# :speech_balloon: Linguagem usada
A linguagem escolhida para esse projeto foi o [Python](https://python.org.br/), que possui diversos materiais vinculados [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) que torna o estudo de Computação Gráfica mais prático, mesmo sendo um conteúdo de Processamento de Imagens sendo complexo.

# :woman_technologist: Sobre o código

<details>
  <summary>Explicação detalhada de cada interação na tela assim como o seu devido código</summary><br />
  
A tela do sistema que permite interação com mouse foi desenvolvida usando uma biblioteca Pyhton chamada [Tkinter](https://docs.python.org/3/library/tkinter.html) que permite fazer uma tela GUI com opção de janelas.

<p align="center">
  <img src="ImagensReadme/tela_inicial.PNG">
</p>

O TkInter tem funções próprias que facilitam a montagem de uma tela de uma tela:

```bash
  window = tk.Tk()
  window.title("InstaKath")
  window.wm_iconbitmap('Icons/instakath.ico')
  window.geometry("250x500")
  window.resizable(True, True)
```

Abaixo explico como funciona cada um dos botões do Menu:

<table align="center">
  <tr>
    <td><img src="ImagensReadme/botao1.PNG"></td>
    <td><b>O primeiro botão é para adicionar filtros em uma imagem pré-definida.<b></td>
  </tr>
  <tr>
    <td colspan="2">
      Ao carregar a tela com a imagem - clicar a <i>tecla 1</i>: <b>Adiciona o filtro em Tons de Cinza</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 2</i>: <b>Adiciona o filtro Radiativo</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 3</i>: <b>Adiciona o filtro Pintura</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 4</i>: <b>Adiciona o filtro Luminosidade</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 5</i>: <b>Adiciona o filtro Detecção de cores vermelhas</b><br />
    </td>
  </tr>
  <tr>
    <td colspan="2">
      Toda vez que clica no filtro salva a imagem no StoriesDownloads/Imagem
    </td>
  </tr>
      
  <table align="center">
  <tr>
    <th>Original</th>
    <th>Tons de Cinza</th>
    <th>Radioativo</th>
  </tr>  
  <tr>
    <td align="center"><img height="300em" widht="600em" src="ImagensReadme/teste.png"></td>
    <td align="center"><img height="300em" src="ImagensReadme/maskgreyscale.png"></td>      
    <td align="center"><img height="300em" src="ImagensReadme/radioactive.png"></td>
  </tr>
  <tr>
    <th>Pintura</th>
    <th>Luminosidade</th>
    <th>Detecção de Cores Vermelhas</th>
  </tr>
  <tr>
    <td align="center"><img height="300em" src="ImagensReadme/painting.png"></td>
    <td align="center"><img height="300em" src="ImagensReadme/light.png"></td>
    <td align="center"><img height="300em" src="ImagensReadme/rouge.png"></td>
  </tr>
</table>

 <table align="center">
  <tr>
    <td><img src="ImagensReadme/botao2.PNG"></td>
    <td><b>O segundo botão é para adicionar filtros em capturas de vídeos.<b></td>
  </tr>
  <tr>
    <td colspan="2">
      Ao carregar a tela de vídeo - clicar a <i>tecla 1</i>: <b>Adiciona o filtro em Tons de Cinza</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 2</i>: <b>Adiciona o filtro Radiativo</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 3</i>: <b>Adiciona o filtro Pintura</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 4</i>: <b>Adiciona o filtro Luminosidade</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 5</i>: <b>Adiciona o filtro Detecção de cores vermelhas</b><br />
    </td>
  </tr>
  <tr>
    <td colspan="2">
      Toda vez que clica no filtro salva a imagem dos efeitos no StoriesDownloads/Imagem
    </td>
  </tr>
  
  <table align="center">
    <tr>
      <th>Tons de Cinza</th>
      <th>Radioativo</th>
    </tr>  
    <tr>
      <td align="center"><img height="300em" src="ImagensReadme/videoGrayCF.png"></td>      
      <td align="center"><img height="300em" src="ImagensReadme/videoRadioactiveCF.png"></td>
    </tr>
    <tr>
      <th>Pintura</th>
      <th>Luminosidade</th>
    </tr>
    <tr>      
      <td align="center"><img height="300em" src="ImagensReadme/videoPaintingCF.png"></td>
      <td align="center"><img height="300em" src="ImagensReadme/videoLightCF.png"></td>
    </tr>
    <tr> 
      <th colspan="2">Detecção de Cores Vermelhas</th>
    </tr>  
    <tr>
      <td align="center" colspan="2"><img height="300em" src="ImagensReadme/videoRougeCF.png"></td>
    </tr>
  </table>

 <table align="center">
  <tr>
    <td><img src="ImagensReadme/botao3.PNG"></td>
    <td><b>O terceiro botão é para adicionar filtros em capturas de vídeos, só que com outra câmera.</td>
  </tr>
  <tr>
    <td colspan="2">
      Ao carregar a tela de vídeo - clicar a <i>tecla 1</i>: <b>Adiciona o filtro em Tons de Cinza</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 2</i>: <b>Adiciona o filtro Radiativo</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 3</i>: <b>Adiciona o filtro Pintura</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 4</i>: <b>Adiciona o filtro Luminosidade</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 5</i>: <b>Adiciona o filtro Detecção de cores vermelhas</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 6</i>: <b>Salva a imagem do filtro que está usando.</b><br />
    </td>
  </tr>
  <tr>
    <td colspan="2">
      Toda vez que clica no filtro salva a imagem dos efeitos no StoriesDownloads/Imagem
    </td>
  </tr>
  
  <table align="center">
    <tr>
      <th>Tons de Cinza</th>
      <th>Radioativo</th>
    </tr>  
    <tr>
      <td align="center"><img height="300em" src="ImagensReadme/videoGray.png"></td>      
      <td align="center"><img height="300em" src="ImagensReadme/videoRadioactive.png"></td>
    </tr>
    <tr>
      <th>Pintura</th>
      <th>Luminosidade</th>
    </tr>
    <tr>      
      <td align="center"><img height="300em" src="ImagensReadme/videoPainting.png"></td>
      <td align="center"><img height="300em" src="ImagensReadme/videoLight.png"></td>
    </tr>
    <tr> 
      <th colspan="2">Detecção de Cores Vermelhas</th>
    </tr>  
    <tr>
      <td align="center" colspan="2"><img height="300em" src="ImagensReadme/videoRouge.png"></td>
    </tr>
  </table>
   
   <table align="center">
  <tr>
    <td><img src="ImagensReadme/botao4.PNG"></td>
    <td><b> O quarto botão é para adicionar filtros em capturas de vídeos adicionando acessórios em tempo real.</td>
  </tr>
  <tr>
    <td colspan="2">
      Ao carregar a tela de vídeo - clicar a <i>tecla 1</i>: <b>Adiciona um filtro Chapéu de Formanda</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 2</i>: <b>Adiciona um filtro com guampinhas de Diabinho</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 3</i>: <b>Adiciona um filtro com uma coroa</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 4</i>: <b>Adiciona um filtro com um sombrero</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 5</i>: <b>Adiciona um filtro Detecção de cores vermelhas</b><br />
      Na mesma tela incial normal - clicar a <i>tecla 6</i>: <b>Salva a imagem do filtro que está usando.</b><br />
    </td>
  </tr>
  <tr>
    <td colspan="2">
      Toda vez que clica no filtro salva a imagem dos efeitos no StoriesDownloads/Imagem e um vídeo de todo o processo desde que iniciou o sistema StoriesDownloads/Video
    </td>
  </tr>
  
  <table align="center">
    <tr>
      <th>Chapéu de Formanda</th>
      <th>Diabinha</th>
    </tr>
    <tr>
      <td align="center"><img height="300em" widht="800em" src="ImagensReadme/graduate1.png"></td>
      <td align="center"><img height="300em" widht="800em" src="ImagensReadme/diablo.PNG"></td>
    </tr>    
    <tr>
      <th>Rainha</th>
      <th>Chapúe de Natal</th>
    </tr>  
    <tr>
      <td align="center"><img height="300em" widht="800em" src="ImagensReadme/queen.PNG"></td>  
      <td align="center"><img height="300em" widht="800em" src="ImagensReadme/noel.PNG"></td>
    </tr>   
    <tr>
      <th colspan="2">Sombrero</th>
    </tr>  
    <tr>
      <td align="center" colspan="2"><img height="300em" widht="800em" src="ImagensReadme/sombrero.PNG"></td>
    </tr>
  </table>
     
  [Vídeo Gravado](ImagensReadme/graduateVideo.mp4)

<br />
</details>

# :rocket: Melhorias

Em um futuro não muito distante quero melhorar a aplicação para deixar o mais semelhante ao stories do Instagram.
     
# :woman_student: Curiosidade
     
A pessoa de todas as imagens (no caso eu mesma) realmente está se formando, por isso o motivo da felicidade.
<p align="center">
  <img height="300em" src="ImagensReadme/foto_filtro_graduanda.png">
</p>

# :books: Fontes das Imagens

[PNGs dos Filtros](https://www.pngegg.com/)

[Icones da Tela](https://www.iconsdb.com/)
