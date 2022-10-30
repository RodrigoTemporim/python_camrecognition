from email.mime import base
import cv2 
import face_recognition
import sys
import os

n1 = []
n2 = []
n3 = []
n4 = ["rodrigo"]

DirPath = 'conhecidos'
Files = os.listdir(DirPath)

nAll = [n1,n2,n3,n4]

def procurarNome(nome, listas): # função para procurar os "login dentro das listas // enquanto não implemento um bd"
    for alistas in listas:        
        if nome in alistas:
            return True
    return False

def tirarFotoCadastro():
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
    
def analisarFotos():
    print("ok")
    
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
    print(results)
    
#tirando foto !!!!!!!!

print(" Sistema Florestal ! ")

menu_res = input("Selecione a opção desejada:\n0- Sair \n1- Cadastro de Usuário \n2- Login de Usuario\n")
while menu_res != "0":
    if menu_res == "1":
        nome = input("Crie um login para vocÊ:\n ").lower()  
        if procurarNome(nome, [n1,n2,n3,n4]):
            print("usuario ja cadastrado!!!")
            break;             
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
            break;                   
        input("Apete qualquer tecla para tirar a foto!")
        tirarFotoCadastro()        
    elif menu_res == "2":
        nome_autent = input("Digite o seu login!\n").lower()
        if procurarNome(nome_autent, [n1,n2,n3, n4]):
            print("Login encontrado!!")
            input("Aperte qualquer tecla para analizarmos seu rosto!") 
            analisarUsuario() 
            break;
        else:
            print("Login não encontrado!!!!!")
            break;         
    else: 
        print("Digite um valor valido!")    
else:
    print("/nFinalizando o Programa!!!")
    print("...")
    input("Aperte qualquer tecla para sair!/n")
    os.system("cls") 



    

    

#tirarFoto()
#analisarUsuario()