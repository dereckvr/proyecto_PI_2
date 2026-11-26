"""Se importan librerías necesarias"""
import tkinter
from tkinter import simpledialog

"""Se preguntará el tamaño de la ventanaal usuario"""
cua_tam=simpledialog.askinteger("Tamaño de la cuadricula", "Ingrese el tamaño de la cuadricula:", minvalue=20, maxvalue=100)
if cua_tam is None: #En caso de cancelar la ventana de ingreso de datos, se cierra el programa
    exit()

PIX_TAM=700/cua_tam
SUB_PIX_TAM=round(PIX_TAM/7)


matriz_bas=[]
sub_matrices=[]

elementos={0:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"], #Aire
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"]],

           1:[["#E0D3A0","#EDE3B6","#E0D3A0","#D3C48A","#E0D3A0","#EDE3B6","#D3C48A"], #Arena
              ["#D3C48A","#E0D3A0","#C1B074","#E0D3A0","#EDE3B6","#D3C48A","#E0D3A0"],
              ["#EDE3B6","#D3C48A","#E0D3A0","#EDE3B6","#C1B074","#E0D3A0","#D3C48A"],
              ["#E0D3A0","#C1B074","#D3C48A","#E0D3A0","#D3C48A","#EDE3B6","#C1B074"],
              ["#D3C48A","#EDE3B6","#E0D3A0","#C1B074","#E0D3A0","#D3C48A","#E0D3A0"],
              ["#C1B074","#D3C48A","#EDE3B6","#D3C48A","#EDE3B6","#C1B074","#D3C48A"],
              ["#E0D3A0","#E0D3A0","#C1B074","#E0D3A0","#D3C48A","#E0D3A0","#EDE3B6"]],

           2:[["#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4"], #Agua
              ["#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4","#5FA6F5"],
              ["#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4","#5FA6F5","#3F76E4"],
              ["#2E5CC7","#1E43A3","#2E5CC7","#3F76E4","#5FA6F5","#3F76E4","#2E5CC7"],
              ["#1E43A3","#2E5CC7","#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3"],
              ["#2E5CC7","#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7"],
              ["#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4"]],

           3:[["#828282","#9E9E9E","#828282","#6E6E6E","#828282","#828282","#6E6E6E"], #Piedra
              ["#6E6E6E","#545454","#6E6E6E","#828282","#9E9E9E","#6E6E6E","#545454"],
              ["#828282","#828282","#9E9E9E","#6E6E6E","#545454","#828282","#828282"],
              ["#9E9E9E","#6E6E6E","#545454","#828282","#828282","#9E9E9E","#6E6E6E"],
              ["#6E6E6E","#828282","#828282","#9E9E9E","#6E6E6E","#545454","#828282"],
              ["#545454","#6E6E6E","#828282","#6E6E6E","#828282","#828282","#9E9E9E"],
              ["#828282","#9E9E9E","#6E6E6E","#545454","#6E6E6E","#828282","#6E6E6E"]],

           4:[["#866043","#9B6E4C","#866043","#6E4E35","#866043","#9B6E4C","#6E4E35"], #Tierra
              ["#6E4E35","#866043","#563B27","#866043","#7A7A7A","#6E4E35","#866043"],
              ["#9B6E4C","#6E4E35","#866043","#9B6E4C","#6E4E35","#866043","#563B27"],
              ["#866043","#563B27","#6E4E35","#866043","#866043","#9B6E4C","#6E4E35"],
              ["#6E4E35","#9B6E4C","#866043","#563B27","#6E4E35","#866043","#866043"],
              ["#563B27","#6E4E35","#7A7A7A","#6E4E35","#9B6E4C","#563B27","#6E4E35"],
              ["#866043","#866043","#6E4E35","#866043","#6E4E35","#866043","#9B6E4C"]],


           5:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"], #Fuego
              ["#87CEEB","#87CEEB","#87CEEB","#FF0000","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#FF0000","#FFA500","#FF0000","#87CEEB","#87CEEB"],
              ["#87CEEB","#FF0000","#FFA500","#FFFF00","#FFA500","#FF0000","#87CEEB"],
              ["#FF0000","#FFA500","#FFFF00","#FFFF00","#FFFF00","#FFA500","#FF0000"],
              ["#FFA500","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFA500"],
              ["#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00"]],


           6:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"], #Semilla
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#5C3A21","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#5C3A21","#D2B48C","#5C3A21","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#A67B5B","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"]],


           7:[["#7CBD42","#59982B","#7CBD42","#59982B","#7CBD42","#59982B","#3F721C"], #Pasto
              ["#59982B","#3F721C","#59982B","#7CBD42","#59982B","#3F721C","#59982B"],
              ["#3F721C","#866043","#3F721C","#59982B","#3F721C","#866043","#3F721C"],
              ["#866043","#563B27","#866043","#3F721C","#866043","#9B6E4C","#563B27"],
              ["#9B6E4C","#866043","#563B27","#866043","#7A7A7A","#866043","#866043"],
              ["#866043","#563B27","#866043","#9B6E4C","#563B27","#866043","#563B27"],
              ["#563B27","#866043","#7A7A7A","#866043","#866043","#563B27","#866043"]],


           8:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"], #Planta fase 1
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#7CBD42","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#7CBD42","#4C9A2A","#7CBD42","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"]],


           9:[["#87CEEB","#87CEEB","#87CEEB","#7CBD42","#87CEEB","#87CEEB","#87CEEB"], #Planta fase 2
              ["#87CEEB","#87CEEB","#7CBD42","#4C9A2A","#7CBD42","#87CEEB","#87CEEB"],
              ["#87CEEB","#4C9A2A","#7CBD42","#2D5A1E","#7CBD42","#4C9A2A","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#4C9A2A","#7CBD42","#2D5A1E","#7CBD42","#4C9A2A","#87CEEB"],
              ["#87CEEB","#87CEEB","#4C9A2A","#2D5A1E","#4C9A2A","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"]],


           10:[["#87CEEB","#87CEEB","#7CBD42","#7CBD42","#7CBD42","#87CEEB","#87CEEB"], #Planta fase 3
               ["#87CEEB","#7CBD42","#4C9A2A","#7CBD42","#000000","#7CBD42","#87CEEB"],
               ["#7CBD42","#4C9A2A","#7CBD42","#4C9A2A","#7CBD42","#4C9A2A","#7CBD42"],
               ["#4C9A2A","#7CBD42","#4C9A2A","#2D5A1E","#4C9A2A","#7CBD42","#4C9A2A"],
               ["#4C9A2A","#4C9A2A","#2D5A1E","#6E4E35","#2D5A1E","#4C9A2A","#4C9A2A"],
               ["#2D5A1E","#C9A2A","#4C9A2A","#6E4E35","#4C9A2A","#4C9A2A","#2D5A1E"],
               ["#87CEEB","#2D5A1E","#2D5A1E","#6E4E35","#2D5A1E","#2D5A1E","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#4A3321","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#4A3321","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#4A3321","#6E4E35","#4A3321","#87CEEB","#87CEEB"]],


           11:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#87CEEB","#87CEEB","#87CEEB","#87CEEB"], #Animal
               ["#87CEEB","#87CEEB","#FFFFFF","#FFFFFF","#FFFFFF","#D9D9D9","#FFFFFF","#FFFFFF","#D9D9D9","#FFFFFF","#FFFFFF","#FFFFFF","#87CEEB","#87CEEB"],
               ["#87CEEB","#FFFFFF","#E5B89B","#E5B89B","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#D9D9D9","#87CEEB"],
               ["#87CEEB","#E5B89B","#2B2B2B","#E5B89B","#FFFFFF","#D9D9D9","#FFFFFF","#FFFFFF","#D9D9D9","#FFFFFF","#FFFFFF","#D9D9D9","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#E5B89B","#E5B89B","#D9D9D9","#FFFFFF","#FFFFFF","#D9D9D9","#FFFFFF","#FFFFFF","#D9D9D9","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#5C4033","#5C4033","#87CEEB","#87CEEB","#87CEEB","#5C4033","#5C4033","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#5C4033","#5C4033","#87CEEB","#87CEEB","#87CEEB","#5C4033","#5C4033","#87CEEB","#87CEEB","#87CEEB"]]}

class Sandbox:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("Chafaria")
        self.root.geometry("750x750")
        self.root.resizable(False,False)

        #Se crea el canvas principal y se dibuja la cuadricula en la que dibujará el usuario
        self.canvas=tkinter.Canvas(self.root,width=700,height=700)
        for i in range(cua_tam):
            matriz_bas.append([])
            sub_matrices.append([])
            for j in range(cua_tam):
                self.canvas.create_rectangle(i*PIX_TAM,j*PIX_TAM,(i+1)*PIX_TAM,(j+1)*PIX_TAM,fill="#87CEEB",outline="")
                matriz_bas[i].append(0)
                sub_matrices[i].append([])

        #se crea la subcuadricula para cada pixel de la cuadricula principal, para la representación de los elementos
        for i in range(len(matriz_bas)):
            for j in range(len(matriz_bas[0])):
                for k in range(7):
                    sub_matrices[i][j].append([])
                    for l in range(7):
                        sub_matrices[i][j][k].append(self.canvas.create_rectangle(i*PIX_TAM+l*SUB_PIX_TAM,j*PIX_TAM+k*SUB_PIX_TAM,i*PIX_TAM+(l+1)*SUB_PIX_TAM,j*PIX_TAM+(k+1)*SUB_PIX_TAM,fill="#87CEEB",outline=""))

        self.canvas.pack()

    def cambiar_bloque(self,x,y,elemento):
        #Función que cambia el bloque de la cuadricula principal y la subcuadricula
        matriz_bas[x][y]=elemento

        if elemento==10:
            pass
        elif elemento==11:
            pass
        else:
            for i in range(7):
                for j in range(7):
                    self.canvas.itemconfig(sub_matrices[x][y][i][j],fill=elementos[elemento][i][j])



        

if __name__=="__main__":
    sandbox=Sandbox()
    sandbox.root.mainloop()