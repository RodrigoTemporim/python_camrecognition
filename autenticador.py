import cv2 
import face_recognition
import os
import webbrowser


n1 = ["amanda"]
n2 = ["pedro"]
n3 = ["alex"]
n4 = ["rodrigo"]

DirPath = 'conhecidos'
Files = os.listdir(DirPath)


def shownv(nome):
    if (nome in n1):
        print("Acesso de nível 1")
    elif (nome in n2):
        print("Acesso de nível 2")
    elif (nome in n3):
        print("Acesso de nível 3")
    elif (nome in n4):
        print("Acesso de nível 4")
        
def procurarNome(nome_autent, listas): # função para procurar os "login dentro das listas // enquanto não implemento um bd"
    for alistas in listas:        
        if nome_autent in alistas:
            return True
    return False

def tirarFotoCadastro(nome):
    print("Tirando foto")   # So fala no terminal
    cap = cv2.VideoCapture(0) # Define cap como video.capture
    ret, frame = cap.read()  
   
    if verficiarFotosCadastro(cap) == True:
        print("Rosto já reconhecido!!!!!!")       
    else:    
        cv2.imwrite("conhecidos/{}.jpg".format(nome), frame) # salva como picture
        cv2.destroyAllWindows()  #quebra a janela da cam
        cap.release()        
        print("Foto Tirada!")
   
def verficiarFotosCadastro(cap):
        for File in Files:
            imgPath = os.path.join(DirPath, File)        
            imagemDesconhecida = face_recognition.load_image_file(imgPath)
            imageConhecida = face_recognition.load_image_file(cap) 
            
            desconhecidaEncoding = face_recognition.face_encodings(imagemDesconhecida)[0]
            conhecidaEncoding = face_recognition.face_encodings(imageConhecida)[0]
    
    
            results = face_recognition.compare_faces([conhecidaEncoding], desconhecidaEncoding)   
            
            return results

def analisarUsuario():   
    # print("Tirando foto")   # So fala no terminal
    # cap = cv2.VideoCapture(0) # Define cap como video.capture
    # ret, frame = cap.read() 
    # cv2.destroyAllWindows()  #quebra a janela da cam
    # cap.release()        
    # imagemDesconhecida = face_recognition.load_image_file(cap)
    # imageConhecida = face_recognition.load_image_file("{}.jpg".format(nome_autent))
    
    imagemDesconhecida = face_recognition.load_image_file("C:/Users/Rodrigo/Documents/GitHub/python_camrecognition/conhecidos/b.jpg")
    imageConhecida = face_recognition.load_image_file("C:/Users/Rodrigo/Documents/GitHub/python_camrecognition/a.jpg")
    
    desconhecidaEncoding = face_recognition.face_encodings(imagemDesconhecida)[0]
    conhecidaEncoding = face_recognition.face_encodings(imageConhecida)[0]
    
    
    results = face_recognition.compare_faces([conhecidaEncoding], desconhecidaEncoding)
    return results
    
def menuApl(nome_autent):
    while True:
        print("Bem vindo {} ao SFI\n".format(nome_autent.capitalize()))
        shownv(nome_autent)        
        try :
            sel = int(input("""-------------------------------------\n0- Sair\n1- Registro de Queimadas ( nível 1 )\n2- Registro de Aldeias ( nível 2 )\n3- Portal Transparencia Funai ( nível 3 )\n4- Portal de Transparencia Receita ( nivel 4 )\n5- Deslogar\n-------------------------------------\n"""))
            if sel == 5:
                input("Deslogando!!!!\n")
                os.system("cls")
                break;
            elif (sel > 5 or sel < 0):
                input("Digite um numero válido\n")
                os.system("cls")                
        except ValueError:            
            input("Apenas numeros são aceitos!")
            os.system("cls")
            continue
        
        switchSel(nome_autent, sel)    
               
def switchMenuRes(menu_res):
    if menu_res == "1":
        nome = input("Crie um login para vocÊ:\n ").lower()  
        if procurarNome(nome, [n1,n2,n3,n4]):
            print("usuario ja cadastrado!!!")                         
        nivel = int(input("Qual o nivel de acesso desejado?"))       
        if nivel == 1:
            n1.append(nome)
            print("Nivel Selecionado com sucesso!!") 
            input("Aperte qualquer tecla para continuar!")  
        elif nivel == 2:
            n1.append(nome)
            print("Nivel Selecionado com sucesso!!") 
            input("Aperte qualquer tecla para continuar!")  
        elif nivel == 3:
            n1.append(nome)
            print("Nivel Selecionado com sucesso!!") 
            input("Aperte qualquer tecla para continuar!")  
        elif nivel == 4:
            n1.append(nome)
            print("Nivel Selecionado com sucesso!!") 
            input("Aperte qualquer tecla para continuar!")   
        else: 
            print("Digite um valor valido!!!")
            
                                         
        input("Apete qualquer tecla para tirar a foto!")
        tirarFotoCadastro(nome)        
    elif menu_res == "2":
        os.system("cls")
        nome_autent = input("-------------------------------------\nDigite o seu login!\n-------------------------------------\n").lower()
        if procurarNome(nome_autent, [n1,n2,n3, n4]):
            print("\n...\nLogin encontrado!!\n")
            input("Aperte qualquer tecla para analizarmos seu rosto!\n-------------------------------------\n") 
            analisarUsuario()
            if analisarUsuario():
                os.system("cls") 
                menuApl(nome_autent)
            else:
                input("Rosto não reconhecido")                
                
        else:
            input("Login não encontrado!!!!!")
            os.system("cls")
    
    elif menu_res == "0":
        input("Finalizando o Sistema ...")
        quit()                  
    elif int(menu_res) > 2 or int(menu_res) < 0:
        input("Digite um valor valido!")  
        os.system("cls")      
        return False
        
def switchSel(nome_autent, sel):
        if sel == 1:
            os.system("cls")
            input("-------------------------------------\nRegistro de Queimadas!!!\n-------------------------------------")
            webbrowser.open("https://queimadas.dgi.inpe.br/queimadas/bdqueimadas")
            os.system("cls")
        elif sel == 2:
            if procurarNome(nome_autent, [n2,n3,n4]):
                os.system("cls")
                input("-------------------------------------\nRegistro de Aldeias!!!\n-------------------------------------")
                webbrowser.open("https://terrasindigenas.org.br/#pesquisas")
                os.system("cls")
            else: 
                os.system("cls")
                input("VocÊ não tem autorização para acessar o conteudo!!")
                os.system("cls")
        elif sel == 3:
            if procurarNome(nome_autent, [n3,n4]):
                os.system("cls")
                input("-------------------------------------\nPortal Transparencia Funai!!!\n-------------------------------------")
                webbrowser.open("https://www.portaltransparencia.gov.br/orgaos/30202-fundacao-nacional-do-indio")
                os.system("cls")
            else: 
                os.system("cls")
                input("VocÊ não tem autorização para acessar o conteudo!!")
                os.system("cls")
        elif sel == 4:
            if procurarNome(nome_autent, [n4]):
                os.system("cls")
                input("-------------------------------------\nPortal de Transparencia Receita!!!\n-------------------------------------")
                webbrowser.open("http://www.transparencia.am.gov.br/pessoal/")
                os.system("cls")
            else: 
                os.system("cls")
                input("VocÊ não tem autorização para acessar o conteudo!!")
                os.system("cls")
        elif sel == 0:
            print("Programa finalizado ...")
            exit()          
            
os.system("cls")
print("-------------------------------------\nSistema Florestal !\n-------------------------------------\n ")
while True:
    menu_res = input("Selecione a opção desejada:\n \n0- Sair \n1- Cadastro de Usuário \n2- Login de Usuario\n-------------------------------------\n")
    try:
        switchMenuRes(menu_res)
    except ValueError:
        input("Apenas numeros são aceitos!")
        os.system("cls")
        continue
