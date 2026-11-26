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
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#277B22","#87CEEB"],
              ["#87CEEB","#87CEEB","#5C3A21","#A67B5B","#277B22","#87CEEB","#87CEEB"],
              ["#87CEEB","#5C3A21","#5C3A21","#A67B5B","#A67B5B","#87CEEB","#87CEEB"],
              ["#87CEEB","#5C3A21","#5C3A21","#5C3A21","#5C3A21","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#5C3A21","#5C3A21","#87CEEB","#87CEEB","#87CEEB"],
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
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#4C9A2A","#2D5A1E","#4C9A2A","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"]],


           10:[["#87CEEB","#87CEEB","#7CBD42","#7CBD42","#7CBD42","#87CEEB","#87CEEB"], #Planta fase 3
               ["#87CEEB","#7CBD42","#4C9A2A","#7CBD42","#7CBD42","#7CBD42","#87CEEB"],
               ["#7CBD42","#4C9A2A","#7CBD42","#4C9A2A","#7CBD42","#4C9A2A","#7CBD42"],
               ["#4C9A2A","#7CBD42","#4C9A2A","#2D5A1E","#4C9A2A","#7CBD42","#4C9A2A"],
               ["#4C9A2A","#4C9A2A","#2D5A1E","#6E4E35","#2D5A1E","#4C9A2A","#4C9A2A"],
               ["#2D5A1E","#4C9A2A","#4C9A2A","#6E4E35","#4C9A2A","#4C9A2A","#2D5A1E"],
               ["#87CEEB","#2D5A1E","#2D5A1E","#6E4E35","#2D5A1E","#2D5A1E","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#4A3321","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#4A3321","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#6E4E35","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#4A3321","#6E4E35","#4A3321","#87CEEB","#87CEEB"]],


           11:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#F898BC","#F898BC","#F898BC","#F898BC","#F898BC","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#F898BC","#000000","#F898BC","#F898BC","#000000","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#F06A9C","#F06A9C","#F06A9C","#F898BC","#000000","#F898BC","#F898BC","#000000","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#F06A9C","#F06A9C","#F06A9C","#F898BC","#F898BC","#F898BC","#EB1C5C","#F898BC","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#F06A9C","#F06A9C","#F06A9C","#F485AF","#F898BC","#F898BC","#F485AF","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#F06A9C","#87CEEB","#87CEEB","#F485AF","#87CEEB","#87CEEB","#F485AF","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
               ["#87CEEB","#87CEEB","#F06A9C","#87CEEB","#87CEEB","#F485AF","#87CEEB","#87CEEB","#F485AF","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"]]}

class Sandbox:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("Chafaria")
        self.root.geometry("750x750")
        self.root.resizable(False,False)

        #Se crea el canvas principal y se dibuja la cuadricula en la que dibujará el usuario
        #Se crea subcuadricula de 7x7 en cada bloque de la cuadricula principal, para poder dibujar los elementos
        self.canvas=tkinter.Canvas(self.root,width=700,height=700)
        for fila in range(cua_tam):
            matriz_bas.append([])
            sub_matrices.append([])
            for colum in range(cua_tam):
                self.canvas.create_rectangle(colum*PIX_TAM,fila*PIX_TAM,(colum+1)*PIX_TAM,(fila+1)*PIX_TAM,fill="",outline="")
                matriz_bas[fila].append(0)
                sub_matrices[fila].append([])
                for sub_fila in range(7):
                    sub_matrices[fila][colum].append([])
                    for sub_colum in range(7):
                        x1=colum*PIX_TAM+sub_colum*SUB_PIX_TAM
                        y1=fila*PIX_TAM+sub_fila*SUB_PIX_TAM
                        x2=colum*PIX_TAM+(sub_colum+1)*SUB_PIX_TAM
                        y2=fila*PIX_TAM+(sub_fila+1)*SUB_PIX_TAM
                        sub_matrices[fila][colum][sub_fila].append(self.canvas.create_rectangle(x1,y1,x2,y2,fill="#87CEEB",outline=""))

        self.canvas.pack()

    def cambiar_bloque(self,fila,colum,elemento):
        #Función que cambia el bloque de la cuadricula principal y la subcuadricula
        matriz_bas[fila][colum]=elemento

        if elemento==10:
            for sub_fila in range(7):
                for sub_colum in range(7):
                    self.canvas.itemconfig(sub_matrices[fila-1][colum][sub_fila][sub_colum],fill=elementos[elemento][sub_fila][sub_colum])
                    self.canvas.itemconfig(sub_matrices[fila][colum][sub_fila][sub_colum],fill=elementos[elemento][sub_fila+7][sub_colum])
        elif elemento==11:
            for sub_fila in range(7):
                for sub_colum in range(7):
                    self.canvas.itemconfig(sub_matrices[fila][colum][sub_fila][sub_colum],fill=elementos[elemento][sub_fila][sub_colum])
                    self.canvas.itemconfig(sub_matrices[fila][colum+1][sub_fila][sub_colum],fill=elementos[elemento][sub_fila][sub_colum+7])
        else:
            for sub_fila in range(7):
                for sub_colum in range(7):
                    self.canvas.itemconfig(sub_matrices[fila][colum][sub_fila][sub_colum],fill=elementos[elemento][sub_fila][sub_colum])



        

if __name__=="__main__":
    sandbox=Sandbox()
    sandbox.cambiar_bloque(1,1,10)

    sandbox.root.mainloop()