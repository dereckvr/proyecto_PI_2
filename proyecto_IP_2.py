"""Se importan librerías necesarias"""
import json,random,tkinter
from tkinter import filedialog,messagebox,simpledialog

"""Se preguntará el tamaño de la cuadrícula al usuario"""
cua_tam=simpledialog.askinteger("Tamaño de la cuadricula","Ingrese el tamaño de la cuadricula:",minvalue=20,maxvalue=100)
if cua_tam is None:  # En caso de cancelar la ventana de ingreso de datos, se cierra el programa
    exit()

"""Constantes relacionadas a las cuadriculas"""
SUB_CUA=7 #Subcuadricula será de 7x7
SUB_CUA_PIX=cua_tam*SUB_CUA #Subpixeles
CANVAS_TAM=700 #Tamaño del canvas
BAR_ELEM_ALTO=50 #Alto de barra de herramientas
TICK_MS=50 #Tiempo de actualización en ms

"""Constantes relacionadas a bloques y archivos"""
ALCANCE_AGUA=20 #Qué tan lejos "ve" el agua un hueco por donde bajar
FLUJO_AGUA=0.3 #Probabilidad de avanzar de lado en cada ciclo
PASO_ANIM=6 #El anim da un paso cada 6 ciclos
DES_ANIM=0.02 #Probabilidad de que se quede descansando
VECINOS=((-1,0),(1,0),(0,-1),(0,1)) #Arriba, abajo, izquierda, derecha
ALREDEDOR=VECINOS+((-1,-1),(-1,1),(1,-1),(1,1)) #Incluye las diagonales
TIEM_ARD_PAS=5 #Ciclos que arde el pasto antes de volverse tierra
TIEM_PLA1=6000 #5 minutos a 50 ms por ciclo
TIEM_PLA2=6000 #5 minutos a 50 ms por ciclo
INFLA=(6,8,9,10) #Bloques inflamables
PLAN_COM=(8,9) #Plantas comibles por el animal
NOM_ELEM={0:"Borrar",1:"Arena",2:"Agua",3:"Piedra",4:"Tierra",5:"Fuego",6:"Semilla",8:"Planta 1",9:"Planta 2",10:"Árbol",11:"anim"}
ARCHIVOS=[("Escenario de Chafaria","*.json")]

ELEMENTOS={0:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],  # Aire
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"]],

           1:[["#E0D3A0","#EDE3B6","#E0D3A0","#D3C48A","#E0D3A0","#EDE3B6","#D3C48A"],  # Arena
              ["#D3C48A","#E0D3A0","#C1B074","#E0D3A0","#EDE3B6","#D3C48A","#E0D3A0"],
              ["#EDE3B6","#D3C48A","#E0D3A0","#EDE3B6","#C1B074","#E0D3A0","#D3C48A"],
              ["#E0D3A0","#C1B074","#D3C48A","#E0D3A0","#D3C48A","#EDE3B6","#C1B074"],
              ["#D3C48A","#EDE3B6","#E0D3A0","#C1B074","#E0D3A0","#D3C48A","#E0D3A0"],
              ["#C1B074","#D3C48A","#EDE3B6","#D3C48A","#EDE3B6","#C1B074","#D3C48A"],
              ["#E0D3A0","#E0D3A0","#C1B074","#E0D3A0","#D3C48A","#E0D3A0","#EDE3B6"]],

           2:[["#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4"],  # Agua
              ["#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4","#5FA6F5"],
              ["#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4","#5FA6F5","#3F76E4"],
              ["#2E5CC7","#1E43A3","#2E5CC7","#3F76E4","#5FA6F5","#3F76E4","#2E5CC7"],
              ["#1E43A3","#2E5CC7","#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3"],
              ["#2E5CC7","#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7"],
              ["#3F76E4","#5FA6F5","#3F76E4","#2E5CC7","#1E43A3","#2E5CC7","#3F76E4"]],

           3:[["#828282","#9E9E9E","#828282","#6E6E6E","#828282","#828282","#6E6E6E"],  # Piedra
              ["#6E6E6E","#545454","#6E6E6E","#828282","#9E9E9E","#6E6E6E","#545454"],
              ["#828282","#828282","#9E9E9E","#6E6E6E","#545454","#828282","#828282"],
              ["#9E9E9E","#6E6E6E","#545454","#828282","#828282","#9E9E9E","#6E6E6E"],
              ["#6E6E6E","#828282","#828282","#9E9E9E","#6E6E6E","#545454","#828282"],
              ["#545454","#6E6E6E","#828282","#6E6E6E","#828282","#828282","#9E9E9E"],
              ["#828282","#9E9E9E","#6E6E6E","#545454","#6E6E6E","#828282","#6E6E6E"]],

           4:[["#866043","#9B6E4C","#866043","#6E4E35","#866043","#9B6E4C","#6E4E35"],  # Tierra
              ["#6E4E35","#866043","#563B27","#866043","#7A7A7A","#6E4E35","#866043"],
              ["#9B6E4C","#6E4E35","#866043","#9B6E4C","#6E4E35","#866043","#563B27"],
              ["#866043","#563B27","#6E4E35","#866043","#866043","#9B6E4C","#6E4E35"],
              ["#6E4E35","#9B6E4C","#866043","#563B27","#6E4E35","#866043","#866043"],
              ["#563B27","#6E4E35","#7A7A7A","#6E4E35","#9B6E4C","#563B27","#6E4E35"],
              ["#866043","#866043","#6E4E35","#866043","#6E4E35","#866043","#9B6E4C"]],

           5:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],  # Fuego
              ["#87CEEB","#87CEEB","#87CEEB","#FF0000","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#FF0000","#FFA500","#FF0000","#87CEEB","#87CEEB"],
              ["#87CEEB","#FF0000","#FFA500","#FFFF00","#FFA500","#FF0000","#87CEEB"],
              ["#FF0000","#FFA500","#FFFF00","#FFFF00","#FFFF00","#FFA500","#FF0000"],
              ["#FFA500","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFA500"],
              ["#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00","#FFFF00"]],

           6:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],  # Semilla
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#277B22","#87CEEB"],
              ["#87CEEB","#87CEEB","#5C3A21","#A67B5B","#277B22","#87CEEB","#87CEEB"],
              ["#87CEEB","#5C3A21","#5C3A21","#A67B5B","#A67B5B","#87CEEB","#87CEEB"],
              ["#87CEEB","#5C3A21","#5C3A21","#5C3A21","#5C3A21","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#5C3A21","#5C3A21","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"]],

           7:[["#7CBD42","#59982B","#7CBD42","#59982B","#7CBD42","#59982B","#3F721C"],  # Pasto (excluido de botones)
              ["#59982B","#3F721C","#59982B","#7CBD42","#59982B","#3F721C","#59982B"],
              ["#866043","#563B27","#866043","#3F721C","#866043","#9B6E4C","#563B27"],
              ["#9B6E4C","#866043","#563B27","#866043","#7A7A7A","#866043","#866043"],
              ["#866043","#563B27","#866043","#9B6E4C","#563B27","#866043","#563B27"],
              ["#563B27","#866043","#7A7A7A","#866043","#866043","#563B27","#866043"],
              ["#563B27","#866043","#7A7A7A","#866043","#866043","#563B27","#866043"]],

           8:[["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],  # Planta fase 1
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#7CBD42","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#7CBD42","#4C9A2A","#7CBD42","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"]],

           9:[["#87CEEB","#87CEEB","#87CEEB","#7CBD42","#87CEEB","#87CEEB","#87CEEB"],  # Planta fase 2
              ["#87CEEB","#87CEEB","#7CBD42","#4C9A2A","#7CBD42","#87CEEB","#87CEEB"],
              ["#87CEEB","#4C9A2A","#7CBD42","#2D5A1E","#7CBD42","#4C9A2A","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#4C9A2A","#2D5A1E","#4C9A2A","#87CEEB","#87CEEB"],
              ["#87CEEB","#87CEEB","#87CEEB","#2D5A1E","#87CEEB","#87CEEB","#87CEEB"]],

          10:[["#87CEEB","#87CEEB","#7CBD42","#7CBD42","#7CBD42","#87CEEB","#87CEEB"],  # Planta fase 3 (Árbol)
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

PASTO_ARDIENDO=[["#FFA500","#FF4500","#FFA500","#FF4500","#FFA500","#FF4500","#B22222"], #Pasto al arder
                ["#FF4500","#B22222","#FF4500","#FFA500","#FF4500","#B22222","#FF4500"],
                ["#866043","#563B27","#866043","#B22222","#866043","#9B6E4C","#563B27"],
                ["#9B6E4C","#866043","#563B27","#866043","#7A7A7A","#866043","#866043"],
                ["#866043","#563B27","#866043","#9B6E4C","#563B27","#866043","#563B27"],
                ["#563B27","#866043","#7A7A7A","#866043","#866043","#563B27","#866043"],
                ["#563B27","#866043","#7A7A7A","#866043","#866043","#563B27","#866043"]]

ICON_BORRA=[["#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B"], #Borrador
            ["#2B2B2B","#2B2B2B","#2B2B2B","#F48FB1","#EC407A","#2B2B2B","#2B2B2B"],
            ["#2B2B2B","#2B2B2B","#F48FB1","#EC407A","#64B5F6","#2B2B2B","#2B2B2B"],
            ["#2B2B2B","#F48FB1","#EC407A","#64B5F6","#1E88E5","#2B2B2B","#2B2B2B"],
            ["#2B2B2B","#2B2B2B","#64B5F6","#1E88E5","#1565C0","#2B2B2B","#2B2B2B"],
            ["#2B2B2B","#2B2B2B","#2B2B2B","#1565C0","#2B2B2B","#2B2B2B","#2B2B2B"],
            ["#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B","#2B2B2B"]]

matriz_bas=[] #Matriz de elementos, se llena en crear_mundo


class Sandbox:
    def __init__(self):
        """Crea la ventana, el lienzo y conecta el mouse."""
        self.root=tkinter.Tk()
        self.root.title("Chafaria")
        self.root.geometry(f"{CANVAS_TAM}x{CANVAS_TAM+BAR_ELEM_ALTO}")
        self.root.resizable(False,False)
        self.canvas=tkinter.Canvas(self.root,width=CANVAS_TAM,height=CANVAS_TAM,highlightthickness=0)

        self.elemen_selec=tkinter.IntVar(value=0)
        self.modo_rectangulo=tkinter.BooleanVar(value=False)

        self.niv_zoom=1
        self.max_zoom=4
        self.offset_x=self.offset_y=0
        self.ultimo_x=self.ultimo_y=0
        self.rect_inicio=self.rect_actual=self.rect_preview=None
        self.pausado=False
        self.ult_pinc=None
        self.refr_pro=False
        self.cre_mundo(cua_tam)

        self.img_base=tkinter.PhotoImage(width=CANVAS_TAM,height=CANVAS_TAM)
        self.img_actual=self.img_base
        self.item_cuadricula=self.canvas.create_image(0,0,anchor="nw",image=self.img_actual)
        self._py_sucio_min,self._py_sucio_max=0,SUB_CUA_PIX-1 #La primera vez se dibuja todo
        self.refr()

        self.canvas.bind("<Button-1>",self.clic_izq)
        self.canvas.bind("<B1-Motion>",self.arras_izq)
        self.canvas.bind("<ButtonRelease-1>",self.solt_izq)
        self.canvas.bind("<Button-3>",self.ini_mov)
        self.canvas.bind("<B3-Motion>",self.mov_cam)
        self.canvas.bind("<MouseWheel>",self.rued_zoom)

        self.canvas.pack(side="top")
        self.cre_barra_bot()
        self.root.after(TICK_MS,self.cic_sim)

    # ---------- Mundo ----------
    def cre_mundo(self,tam):
        """Crea un mundo vacío del tamaño indicado."""
        global cua_tam,SUB_CUA_PIX,matriz_bas
        cua_tam=tam
        SUB_CUA_PIX=tam*SUB_CUA

        def capa(valor):
            matriz=[]
            for i in range(tam):
                matriz.append([])
                for j in range(tam):
                    matriz[i].append(valor)
            return matriz

        matriz_bas=capa(0)
        self.vida_fuego=capa(0)
        self.edad_planta=capa(0)
        self.edad_semilla=capa(0)
        self.arena_quieta=capa(False)
        self.dir_anim=capa(1)
        self.espera_anim=capa(0)
        self.parte=capa(0) #Árbol: 0 arriba, 1 abajo. anim: 0 izquierda, 1 derecha
        self.pasto_ardiendo=capa(0) #Mayor que 0 si el pasto se está quemando

        # Todos los datos de cada celda: se mueven juntos y se guardan en el archivo
        self.capas={"elementos":matriz_bas,"vida_fuego":self.vida_fuego,"edad_planta":self.edad_planta,"edad_semilla":self.edad_semilla,
                    "arena_quieta":self.arena_quieta,"dir_anim":self.dir_anim,"espera_anim":self.espera_anim,"parte":self.parte,"pasto_ardiendo":self.pasto_ardiendo}

        self._py_sucio_min=SUB_CUA_PIX
        self._py_sucio_max=-1
        self._mapa_y=[]
        for i in range(CANVAS_TAM):
            self._mapa_y.append(i*SUB_CUA_PIX//CANVAS_TAM)

        self._mapa_x=[]
        for j in range(CANVAS_TAM):
            self._mapa_x.append(j*SUB_CUA_PIX//CANVAS_TAM)

        self.pixeles=[]
        for i in range(SUB_CUA_PIX):
            self.pixeles.append(["#87CEEB"]*SUB_CUA_PIX)

    # ---------- Barra de botones ----------
    def cre_barra_bot(self):
        """Crea los botones de herramientas, elementos y archivos."""
        barra=tkinter.Frame(self.root,width=CANVAS_TAM,height=BAR_ELEM_ALTO,bg="#2B2B2B")
        barra.pack(side="bottom",fill="x")
        barra.pack_propagate(False)
        estilo={"activebackground":"#555555","bd":2}

        def usar_pinc():
            self.camb_modo(False)

        def usar_rect():
            self.camb_modo(True)

        self.btn_pincel=tkinter.Button(barra,text="Pincel",font=("Arial",8,"bold"),bg="#5A7D9A",fg="#FFFFFF",activeforeground="#FFFFFF",
                                       relief="sunken",command=usar_pinc,**estilo)
        self.btn_rect=tkinter.Button(barra,text="Rect",font=("Arial",8,"bold"),bg="#3C3C3C",fg="#FFD700",activeforeground="#FFD700",
                                     relief="raised",command=usar_rect,**estilo)
        for boton in (self.btn_pincel,self.btn_rect):
            boton.pack(side="left",expand=True,fill="both",padx=2,pady=2)

        self._miniaturas=[]
        self._botones={}
        for elem_id in ELEMENTOS:
            if elem_id!=7: #El pasto no tiene botón
                self.cre_bot(barra,elem_id)

        columna=tkinter.Frame(barra,bg="#2B2B2B")
        columna.pack(side="left",fill="both",padx=2,pady=2)
        for texto,accion in (("Guardar",self.guar_esc),("Cargar",self.carg_esc)):
            tkinter.Button(columna,text=texto,font=("Arial",7,"bold"),bg="#2E7D32",fg="#FFFFFF",activebackground="#555555",
                           activeforeground="#FFFFFF",bd=1,pady=0,command=accion).pack(side="top",expand=True,fill="both")
        self.selec_elem(self.elemen_selec.get())

    def cre_bot(self,barra,elem_id,tam=26):
        """Crea el botón de un elemento con su miniatura."""
        if elem_id==0:
            matriz=ICON_BORRA
        else:
            matriz=ELEMENTOS[elem_id]
        mini=tkinter.PhotoImage(width=tam,height=tam)
        for i in range(tam):
            for j in range(tam):
                color=matriz[i*len(matriz)//tam][j*len(matriz[0])//tam]
                mini.put(color,to=(j,i))
        self._miniaturas.append(mini) #Se guarda para que la imagen no se borre

        def cmd_bot():
            self.selec_elem(elem_id)

        btn=tkinter.Button(barra,image=mini,text=NOM_ELEM.get(elem_id),compound="top",font=("Arial",7),bg="#3C3C3C",fg="#FFFFFF",
                           activebackground="#555555",activeforeground="#FFFFFF",relief="raised",bd=2,
                           command=cmd_bot)
        btn.pack(side="left",expand=True,fill="both",padx=1,pady=2)
        self._botones[elem_id]=btn

    def camb_modo(self,rectangulo):
        """Cambia entre pincel y rectángulo."""
        self.modo_rectangulo.set(rectangulo)
        if rectangulo:
            activo=self.btn_rect
            inactivo=self.btn_pincel
        else:
            activo=self.btn_pincel
            inactivo=self.btn_rect
        activo.config(relief="sunken",bg="#5A7D9A")
        inactivo.config(relief="raised",bg="#3C3C3C")
        if not rectangulo:
            self.limp_prev_rect()

    def selec_elem(self,elem_id):
        """Selecciona un elemento y resalta su botón."""
        self.elemen_selec.set(elem_id)
        for id_bot,btn in self._botones.items():
            if id_bot==elem_id:
                btn.config(relief="sunken",bg="#5A7D9A")
            else:
                btn.config(relief="raised",bg="#3C3C3C")

    # ---------- Dibujo y cámara ----------
    def pint_cel(self,fila,colum):
        """Dibuja una celda según su estado."""
        elemento=matriz_bas[fila][colum]
        inicio=self.parte[fila][colum]*SUB_CUA
        dibujo=ELEMENTOS[elemento]

        if elemento==7 and self.pasto_ardiendo[fila][colum]>0:
            dibujo=PASTO_ARDIENDO
        elif elemento==10:  # El árbol mide 14 de alto
            dibujo=dibujo[inicio:inicio+SUB_CUA]
        elif elemento==11:  # El anim mide 14 de ancho
            if self.dir_anim[fila][colum]==-1:  # Mira hacia la izquierda
                invertido=[]
                for linea in dibujo:
                    invertido.append(linea[::-1])
                dibujo=invertido
            recorte=[]
            for linea in dibujo:
                recorte.append(linea[inicio:inicio+SUB_CUA])
            dibujo=recorte

        base_y=fila*SUB_CUA
        base_x=colum*SUB_CUA
        for i in range(SUB_CUA):
            for j in range(SUB_CUA):
                self.pixeles[base_y+i][base_x+j]=dibujo[i][j]

        # Marca las filas de píxeles que hay que volver a dibujar
        self._py_sucio_min=min(self._py_sucio_min,base_y)
        self._py_sucio_max=max(self._py_sucio_max,base_y+SUB_CUA-1)

    def refr(self):
        """Pasa a la pantalla solo las filas que cambiaron."""
        self.refr_pro=False
        if self._py_sucio_min>self._py_sucio_max:
            return
        py_min,py_max=self._py_sucio_min,self._py_sucio_max
        self._py_sucio_min,self._py_sucio_max=SUB_CUA_PIX,-1

        for i in range(CANVAS_TAM):
            py=self._mapa_y[i]
            if py_min<=py<=py_max:
                colores=[]
                for pix_col in self._mapa_x:
                    colores.append(self.pixeles[py][pix_col])
                self.img_base.put("{"+" ".join(colores)+"}",to=(0,i))
        self.act_img_zoom()

    def act_img_zoom(self):
        """Muestra la imagen con el zoom actual."""
        if self.niv_zoom==1:
            self.img_actual=self.img_base
        else:
            self.img_actual=self.img_base.zoom(self.niv_zoom,self.niv_zoom)
        self.canvas.itemconfig(self.item_cuadricula,image=self.img_actual)

    def mov_vista(self,x,y):
        """Mueve la cámara sin salirse del mundo."""
        limite=CANVAS_TAM-CANVAS_TAM*self.niv_zoom
        self.offset_x=max(limite,min(0,x))
        self.offset_y=max(limite,min(0,y))
        self.canvas.coords(self.item_cuadricula,self.offset_x,self.offset_y)
        self.act_prev_rect()

    # ---------- Manejo de celdas ----------
    def dentro(self,fila,colum):
        """True si la celda está dentro del mundo."""
        return 0<=fila<cua_tam and 0<=colum<cua_tam

    def es_elem(self,fila,colum,elemento):
        """True si la celda existe y contiene ese elemento."""
        return self.dentro(fila,colum) and matriz_bas[fila][colum]==elemento

    def pon_cel(self,fila,colum,elemento,parte=0,direccion=None):
        """Pone un elemento en una celda y reinicia sus datos."""
        if not self.dentro(fila,colum):
            return
        matriz_bas[fila][colum]=elemento
        self.vida_fuego[fila][colum]=0
        self.edad_planta[fila][colum]=0
        self.edad_semilla[fila][colum]=0
        self.arena_quieta[fila][colum]=False
        al_azar=random.choice((-1,1))
        if direccion is None:
            self.dir_anim[fila][colum]=al_azar
        else:
            self.dir_anim[fila][colum]=direccion
        self.espera_anim[fila][colum]=0
        self.parte[fila][colum]=parte
        self.pasto_ardiendo[fila][colum]=0
        if elemento==5:
            self.vida_fuego[fila][colum]=random.randint(12,22)
        self.pint_cel(fila,colum)

    def pon_par(self,celdas,elemento,direccion):
        """Coloca las dos mitades de un árbol o de un anim."""
        for parte,(i,j) in enumerate(celdas):
            self.pon_cel(i,j,elemento,parte,direccion)

    def pos_par(self,fila,colum):
        """Devuelve la otra mitad de un árbol o anim, o None."""
        if not self.dentro(fila,colum) or matriz_bas[fila][colum] not in (10,11):
            return None
        elemento=matriz_bas[fila][colum]
        parte=self.parte[fila][colum]
        if parte==0:
            paso=1
        else:
            paso=-1
        if elemento==10:
            f,c=fila+paso,colum
        else:
            f,c=fila,colum+paso
        if self.es_elem(f,c,elemento) and self.parte[f][c]!=parte:
            return f,c
        return None

    def borr_par(self,fila,colum):
        """Borra una celda y su otra mitad si tiene."""
        pareja=self.pos_par(fila,colum)
        if pareja is not None:
            self.pon_cel(pareja[0],pareja[1],0)
        self.pon_cel(fila,colum,0)

    def pon_bloq(self,fila,colum,elemento):
        """Coloca el bloque que elige el usuario (o que crece solo)."""
        if not self.dentro(fila,colum):
            return  # Nunca se pone nada fuera del lienzo
        if elemento==0:
            self.borr_par(fila,colum)
            return

        # El árbol y el anim ocupan 2 celdas: en el borde se corren hacia adentro
        if elemento==10:
            fila=max(fila,1)
            celdas=[(fila-1,colum),(fila,colum)]
        elif elemento==11:
            colum=min(colum,cua_tam-2)
            celdas=[(fila,colum),(fila,colum+1)]
        else:
            celdas=[(fila,colum)]

        # Se quita completo lo que hubiera en esas celdas
        for i,j in celdas:
            self.borr_par(i,j)

        if elemento==10:
            self.pon_par(celdas,10,1)
        elif elemento==11:
            self.pon_par(celdas,11,random.choice((-1,1)))
        else:
            self.pon_cel(fila,colum,elemento)

    def desp_aren(self,fila,colum):
        """Reactiva la arena que está alrededor."""
        for i in range(fila-1,fila+2):
            for j in range(colum-1,colum+2):
                if self.es_elem(i,j,1):
                    self.arena_quieta[i][j]=False

    def mov_cel(self,f1,c1,f2,c2,visitado):
        """Intercambia dos celdas junto con todos sus datos."""
        for datos in self.capas.values():
            datos[f1][c1],datos[f2][c2]=datos[f2][c2],datos[f1][c1]
        for i,j in ((f1,c1),(f2,c2)):
            self.pint_cel(i,j)
            self.desp_aren(i,j)
            visitado.add((i,j))

    # ---------- Simulación de elementos ----------
    def sim_aren(self,fila,colum,visitado):
        """La arena cae hacia abajo o en diagonal."""
        if self.arena_quieta[fila][colum]:
            return
        if fila+1>=cua_tam:
            self.arena_quieta[fila][colum]=True
            return

        if matriz_bas[fila+1][colum] in (0,2):
            self.mov_cel(fila,colum,fila+1,colum,visitado)
            return

        dirs=[-1,1]
        random.shuffle(dirs)
        for lado in dirs:
            nc=colum+lado
            if 0<=nc<cua_tam and matriz_bas[fila+1][nc] in (0,2) and matriz_bas[fila][nc] in (0,2):
                self.mov_cel(fila,colum,fila+1,nc,visitado)
                return

        self.arena_quieta[fila][colum]=True

    def dist_baj(self,fila,colum,lado):
        """Pasos hasta un hueco por donde caer, o None si no hay."""
        for paso in range(1,ALCANCE_AGUA+1):
            c=colum+lado*paso
            if not self.es_elem(fila,c,0):
                return None  # Hay una pared u otra cosa en el camino
            if self.es_elem(fila+1,c,0):
                return paso
        return None

    def sim_agua(self,fila,colum,visitado):
        """El agua cae, fluye, apaga fuego y crea pasto."""
        # Si cae sobre fuego, lo apaga
        if self.es_elem(fila+1,colum,5):
            self.pon_cel(fila,colum,0)
            self.pon_cel(fila+1,colum,0)
            visitado.update(((fila,colum),(fila+1,colum)))
            return

        # La tierra que recibe agua desde arriba se vuelve pasto
        if self.es_elem(fila+1,colum,4):
            self.pon_cel(fila+1,colum,7)
            self.pon_cel(fila,colum,0)
            visitado.update(((fila,colum),(fila+1,colum)))
            return

        # Cae hacia abajo
        if self.es_elem(fila+1,colum,0):
            self.mov_cel(fila,colum,fila+1,colum,visitado)
            return

        lados=[-1,1]
        random.shuffle(lados)

        # Resbala en diagonal
        for lado in lados:
            c=colum+lado
            if self.es_elem(fila,c,0) and self.es_elem(fila+1,c,0):
                self.mov_cel(fila,colum,fila+1,c,visitado)
                return

        if random.random()>FLUJO_AGUA:
            return

        # Avanza una celda hacia la bajada más cercana
        mejor_lado=None
        mejor_distancia=None
        for lado in lados:
            distancia=self.dist_baj(fila,colum,lado)
            if distancia is not None and (mejor_distancia is None or distancia<mejor_distancia):
                mejor_lado,mejor_distancia=lado,distancia

        if mejor_lado is not None:
            self.mov_cel(fila,colum,fila,colum+mejor_lado,visitado)
            return

        # Si tiene agua encima, la presión la empuja hacia un lado
        if self.es_elem(fila-1,colum,2):
            for lado in lados:
                if self.es_elem(fila,colum+lado,0):
                    self.mov_cel(fila,colum,fila,colum+lado,visitado)
                    return

    def sim_sem(self,fila,colum,visitado):
        """La semilla cae, se quema o germina sobre pasto."""
        if self.es_elem(fila+1,colum,5):
            self.vida_fuego[fila+1][colum]=random.randint(12,22)
            self.pon_cel(fila,colum,0)
            visitado.update(((fila,colum),(fila+1,colum)))
        elif self.es_elem(fila+1,colum,0):  # Solo cae por aire, no por agua
            self.mov_cel(fila,colum,fila+1,colum,visitado)
        elif self.es_elem(fila+1,colum,7):  # Germina
            self.pon_cel(fila,colum,8)
            visitado.add((fila,colum))

    def sim_plan(self,fila,colum,etapa,visitado):
        """La planta crece con agua o con el tiempo."""
        # La fase 2 necesita espacio arriba para volverse árbol
        if etapa==9 and not (self.es_elem(fila-1,colum,0) or self.es_elem(fila-1,colum,2)):
            return

        # Busca agua arriba o a los lados
        agua=None
        for i,j in ((fila-1,colum),(fila,colum-1),(fila,colum+1)):
            if self.es_elem(i,j,2):
                agua=(i,j)
                break

        self.edad_planta[fila][colum]+=1
        if etapa==8:
            tiempo=TIEM_PLA1
        else:
            tiempo=TIEM_PLA2
        if agua is None and self.edad_planta[fila][colum]<tiempo:
            return

        if agua is not None:
            self.pon_cel(agua[0],agua[1],0)
            visitado.add(agua)

        visitado.add((fila,colum))
        if etapa==8:
            self.pon_cel(fila,colum,9)
        else:
            self.pon_bloq(fila,colum,10)
            visitado.add((fila-1,colum))

    def prop_fue(self,fila,colum,visitado):
        """Quema lo que hay alrededor. True si encendió algo."""
        encendio=False
        for des_fil,des_col in ALREDEDOR:
            i,j=fila+des_fil,colum+des_col
            if not self.dentro(i,j):
                continue

            if matriz_bas[i][j]==7 and self.pasto_ardiendo[i][j]==0:  # Pasto
                self.pasto_ardiendo[i][j]=TIEM_ARD_PAS
                self.pint_cel(i,j)
                visitado.add((i,j))
                if self.es_elem(i-1,j,0):  # Sale una llama encima
                    self.pon_cel(i-1,j,5)
                    visitado.add((i-1,j))
                encendio=True

            elif matriz_bas[i][j]==6:  # La semilla desaparece
                if matriz_bas[fila][colum]==5:
                    self.vida_fuego[fila][colum]=random.randint(12,22)
                self.pon_cel(i,j,0)
                visitado.add((i,j))
                encendio=True

            elif matriz_bas[i][j] in INFLA:  # Plantas y árbol (se quema completo)
                pareja=self.pos_par(i,j)
                celdas=[(i,j)]
                if pareja is not None:
                    celdas.append(pareja)
                for fil_que,col_que in celdas:
                    self.pon_cel(fil_que,col_que,5)
                    visitado.add((fil_que,col_que))
                encendio=True
        return encendio

    def sim_pas_ard(self,fila,colum,visitado):
        """El pasto arde un rato y luego queda como tierra."""
        self.pasto_ardiendo[fila][colum]-=1
        if self.pasto_ardiendo[fila][colum]!=0:
            return

        # Si tiene agua a un lado y espacio arriba, vuelve a ser pasto
        agua=None
        if self.es_elem(fila-1,colum,0) or self.es_elem(fila-1,colum,2):
            for col_lado in (colum-1,colum+1):
                if self.es_elem(fila,col_lado,2):
                    agua=(fila,col_lado)
                    break

        self.prop_fue(fila,colum,visitado)
        self.pon_cel(fila,colum,4)
        visitado.add((fila,colum))
        if agua is not None:
            self.pon_cel(agua[0],agua[1],0)
            self.pon_cel(fila,colum,7)
            visitado.add(agua)

    def sim_fue(self,fila,colum,visitado):
        """El fuego se propaga o se va apagando."""
        if self.prop_fue(fila,colum,visitado):
            self.vida_fuego[fila][colum]=random.randint(12,22)
            return
        self.vida_fuego[fila][colum]-=1
        if self.vida_fuego[fila][colum]<=0:
            self.pon_cel(fila,colum,0)
            visitado.add((fila,colum))

    # ---------- anim ----------
    def cabe_anim(self,fila,c_izq,c_actual=None,f_actual=None,permitir_agua=False):
        """True si el anim cabe en ese lugar."""
        for j in (c_izq,c_izq+1):
            if fila==f_actual and j in (c_actual,c_actual+1):
                continue  # Es una celda que él mismo ocupa
            if not self.dentro(fila,j):
                return False
            elemento=matriz_bas[fila][j]
            if not (elemento==0 or elemento in PLAN_COM or (permitir_agua and elemento==2)):
                return False
        return True

    def suelo_anim(self,fila,c_izq):
        """True si hay suelo firme bajo las dos mitades."""
        if fila+1>=cua_tam:  # El borde de abajo del mapa también es suelo
            return True
        for j in (c_izq,c_izq+1):
            if not self.dentro(fila+1,j):
                return False
            if matriz_bas[fila+1][j] in (0,2):
                return False
        return True

    def puede_bajar(self,fila,c_izq,col_baj):
        """True si el anim puede bajar un solo bloque."""
        if not self.cabe_anim(fila,col_baj,c_izq,fila):  # Paso libre al frente
            return False
        if not self.cabe_anim(fila+1,col_baj):  # Destino libre, no borra bloques
            return False
        fila_suelo=fila+2
        for j in (col_baj,col_baj+1):
            if self.es_elem(fila_suelo,j,2):  # No baja sobre agua
                return False
        if fila_suelo>=cua_tam:  # Llega al borde de abajo del mapa
            return True
        for j in (col_baj,col_baj+1):
            if matriz_bas[fila_suelo][j]!=0:  # Basta con apoyar una mitad
                return True
        return False  # La caída es de más de 1 bloque

    def mov_anim(self,fila,c_izq,nueva_fila,nueva_col,direccion,visitado):
        """Mueve las dos mitades del anim."""
        antes=[(fila,c_izq),(fila,c_izq+1)]
        despues=[(nueva_fila,nueva_col),(nueva_fila,nueva_col+1)]

        for i,j in despues:
            if (i,j) not in antes:
                if matriz_bas[i][j] in PLAN_COM:
                    self.borr_par(i,j)
                elif matriz_bas[i][j]==2:  # Se bebe el agua
                    self.pon_cel(i,j,0)

        for i,j in antes:
            self.pon_cel(i,j,0)
        self.pon_par(despues,11,direccion)

        visitado.update(antes+despues)
        for i,j in antes+despues:
            self.desp_aren(i,j)

    def sim_anim(self,fila,colum,visitado):
        """Controla al anim: comer, caer, caminar, saltar y girar."""
        if self.pos_par(fila,colum) is None:  # Quedó solo una mitad
            self.pon_cel(fila,colum,0)
            visitado.add((fila,colum))
            return

        f,c=fila,colum-self.parte[fila][colum]  # c es la mitad izquierda
        if (f,c) in visitado or (f,c+1) in visitado:
            return
        visitado.update(((f,c),(f,c+1)))
        celdas=[(f,c),(f,c+1)]

        # Muere si toca fuego
        toca_fuego=False
        for j in (c,c+1):
            for des_fil,des_col in VECINOS:
                if self.es_elem(f+des_fil,j+des_col,5):
                    toca_fuego=True
        if toca_fuego:
            for i,j in celdas:
                self.pon_cel(i,j,0)
            return

        # Come las plantas cercanas
        for i in (f-1,f):
            for j in range(c-1,c+3):
                if self.dentro(i,j) and matriz_bas[i][j] in PLAN_COM:
                    self.borr_par(i,j)
                    visitado.add((i,j))

        d=self.dir_anim[f][c]
        if self.cabe_anim(f+1,c):  # Cae
            self.mov_anim(f,c,f+1,c,d,visitado)
            return

        # Espera su turno y a veces descansa
        self.espera_anim[f][c]+=1
        if self.espera_anim[f][c]<PASO_ANIM:
            return
        self.espera_anim[f][c]=0
        if random.random()<DES_ANIM:
            self.espera_anim[f][c]=-40
            return

        nueva_col=c+d
        if d==1:
            frente=c+2
        else:
            frente=c-1

        # Agua adelante y abajo: salta si es de un solo bloque, si no gira
        if self.es_elem(f+1,frente,2):
            salto=c+3*d
            if not self.es_elem(f+1,frente+d,2) and self.cabe_anim(f,salto,c,f):
                if self.suelo_anim(f,salto):
                    self.mov_anim(f,c,f,salto,d,visitado)
                    return
            self.pon_par(celdas,11,-d)
            return

        # Camina si hay suelo firme; si no, intenta bajar un bloque o gira
        if self.cabe_anim(f,nueva_col,c,f,permitir_agua=True):
            col_baj=c+2*d  # Avanza 2 para quedar completo fuera del borde
            if self.suelo_anim(f,nueva_col):
                self.mov_anim(f,c,f,nueva_col,d,visitado)
            elif self.puede_bajar(f,c,nueva_col):  # Baja avanzando 1
                self.mov_anim(f,c,f+1,nueva_col,d,visitado)
            elif self.puede_bajar(f,c,col_baj):  # Baja avanzando 2
                self.mov_anim(f,c,f+1,col_baj,d,visitado)
            else:
                self.pon_par(celdas,11,-d)
            return

        # Sube un escalón; si no puede, gira
        sobre_agua=self.es_elem(f,nueva_col,2) or self.es_elem(f,nueva_col+1,2)
        if not self.es_elem(f,frente,11) and self.cabe_anim(f-1,nueva_col) and not sobre_agua:
            self.mov_anim(f,c,f-1,nueva_col,d,visitado)
        else:
            self.pon_par(celdas,11,-d)

    def cic_sim(self):
        """Actualiza todo el mundo cada cierto tiempo."""
        if not self.pausado:
            visitado=set()
            for i in range(cua_tam-1,-1,-1):
                cols=list(range(cua_tam))
                random.shuffle(cols)
                for j in cols:
                    if (i,j) in visitado:
                        continue
                    elem=matriz_bas[i][j]
                    if elem==1:
                        self.sim_aren(i,j,visitado)
                    elif elem==2:
                        self.sim_agua(i,j,visitado)
                    elif elem==7 and self.pasto_ardiendo[i][j]>0:
                        self.sim_pas_ard(i,j,visitado)
                    elif elem==5:
                        self.sim_fue(i,j,visitado)
                    elif elem==6:
                        self.sim_sem(i,j,visitado)
                    elif elem in (8,9):
                        self.sim_plan(i,j,elem,visitado)
                    elif elem==11:
                        self.sim_anim(i,j,visitado)
            self.refr()
        self.root.after(TICK_MS,self.cic_sim)

    # ---------- Guardar y cargar ----------
    def guar_esc(self):
        """Guarda el mundo en un archivo JSON."""
        self.pausado=True
        ruta=filedialog.asksaveasfilename(title="Guardar escenario",defaultextension=".json",filetypes=ARCHIVOS)
        if ruta:
            try:
                with open(ruta,"w",encoding="utf-8") as archivo:
                    json.dump({"tam":cua_tam,"capas":self.capas},archivo)
            except OSError as error:
                messagebox.showerror("Error",f"No se pudo guardar el escenario:\n{error}")
        self.pausado=False

    def carg_esc(self):
        """Carga un mundo desde un archivo JSON."""
        self.pausado=True
        ruta=filedialog.askopenfilename(title="Cargar escenario",filetypes=ARCHIVOS)
        if ruta:
            try:
                tam,capas=self.leer_esc(ruta)
                self.limp_prev_rect()
                self.ult_pinc=None
                self.cre_mundo(tam)
                for nombre,destino in self.capas.items():
                    for i in range(tam):
                        destino[i][:]=capas[nombre][i]
                for i in range(tam):
                    for j in range(tam):
                        self.pint_cel(i,j)
                self.niv_zoom=1
                self.mov_vista(0,0)
                self.refr()
            except (OSError,ValueError,KeyError,TypeError) as error:
                messagebox.showerror("Error",f"No se pudo cargar el escenario:\n{error}")
        self.pausado=False

    def leer_esc(self,ruta):
        """Lee el archivo y revisa que sea válido."""
        with open(ruta,"r",encoding="utf-8") as archivo:
            datos=json.load(archivo)

        tam=datos["tam"]
        if type(tam) is not int or not 20<=tam<=100:
            raise ValueError("Tamaño de cuadrícula no válido")

        capas=datos["capas"]
        for nombre,actual in self.capas.items():
            capa=capas[nombre]
            if len(capa)!=tam:
                raise ValueError(f"Datos incompletos en '{nombre}'")
            for fila_dat in capa:
                if len(fila_dat)!=tam:
                    raise ValueError(f"Datos incompletos en '{nombre}'")
            tipo=type(actual[0][0])
            for fila_dat in capa:
                for valor in fila_dat:
                    if type(valor) is not tipo:
                        raise ValueError(f"Datos incorrectos en '{nombre}'")

        for fila_dat in capas["elementos"]:
            for valor in fila_dat:
                if valor not in ELEMENTOS:
                    raise ValueError("Hay un elemento desconocido")
        for fila_dat in capas["parte"]:
            for valor in fila_dat:
                if valor not in (0,1):
                    raise ValueError("Datos incorrectos en 'parte'")
        return tam,capas

    # ---------- Mouse ----------
    def even_cel(self,event):
        """Convierte la posición del mouse en (fila, columna)."""
        if not (0<=event.x<CANVAS_TAM and 0<=event.y<CANVAS_TAM):
            return None
        tam_bloque=(CANVAS_TAM*self.niv_zoom)/cua_tam
        fila=int((event.y-self.offset_y)//tam_bloque)
        colum=int((event.x-self.offset_x)//tam_bloque)
        if self.dentro(fila,colum):
            return fila,colum
        return None

    def limp_prev_rect(self):
        """Quita el rectángulo amarillo de vista previa."""
        if self.rect_preview is not None:
            self.canvas.delete(self.rect_preview)
        self.rect_inicio=self.rect_actual=self.rect_preview=None

    def act_prev_rect(self):
        """Dibuja el rectángulo amarillo de vista previa."""
        if self.rect_inicio is None or self.rect_actual is None:
            return
        f1,c1=self.rect_inicio
        f2,c2=self.rect_actual
        tam_bloque=(CANVAS_TAM*self.niv_zoom)/cua_tam
        coords=(self.offset_x+min(c1,c2)*tam_bloque,self.offset_y+min(f1,f2)*tam_bloque,
                self.offset_x+(max(c1,c2)+1)*tam_bloque,self.offset_y+(max(f1,f2)+1)*tam_bloque)
        if self.rect_preview is None:
            self.rect_preview=self.canvas.create_rectangle(*coords,outline="#FFFF00",width=2,dash=(4,2))
        else:
            self.canvas.coords(self.rect_preview,*coords)

    def clic_izq(self,event):
        """Pinta un bloque o empieza un rectángulo."""
        celda=self.even_cel(event)
        if celda is None:
            return
        if self.modo_rectangulo.get():
            self.rect_inicio=self.rect_actual=celda
            self.act_prev_rect()
        else:
            elemento=self.elemen_selec.get()
            self.ult_pinc=(celda[0],celda[1],elemento)
            self.pon_bloq(celda[0],celda[1],elemento)
            self.refr()

    def arras_izq(self,event):
        """Pinta una línea o cambia el tamaño del rectángulo."""
        celda=self.even_cel(event)
        if celda is None:
            self.ult_pinc=None
            return
        if self.modo_rectangulo.get():
            if self.rect_inicio is None:
                self.rect_inicio=celda
            self.rect_actual=celda
            self.act_prev_rect()
            return

        elemento=self.elemen_selec.get()
        f1,c1=celda
        nuevo=(f1,c1,elemento)
        if self.ult_pinc==nuevo:
            return

        if self.ult_pinc is not None and self.ult_pinc[2]==elemento:
            # Rellena los espacios entre la posición anterior y la actual
            f0,c0=self.ult_pinc[:2]
            pasos=max(abs(f1-f0),abs(c1-c0))
            for num_paso in range(pasos+1):
                t=num_paso/pasos
                self.pon_bloq(int(round(f0+(f1-f0)*t)),int(round(c0+(c1-c0)*t)),elemento)
        else:
            self.pon_bloq(f1,c1,elemento)

        self.ult_pinc=nuevo
        if not self.refr_pro:
            self.refr_pro=True
            self.root.after(16,self.refr)

    def solt_izq(self,event):
        """Al soltar el clic, rellena el rectángulo."""
        self.ult_pinc=None
        if not self.modo_rectangulo.get() or self.rect_inicio is None:
            return
        f1,c1=self.rect_inicio
        celda=self.even_cel(event)
        if celda is not None:
            self.rect_actual=celda
        if self.rect_actual is not None:
            f2,c2=self.rect_actual
        else:
            f2,c2=self.rect_inicio
        elemento=self.elemen_selec.get()
        if elemento==10:
            paso_fila=2
        else:
            paso_fila=1
        if elemento==11:
            paso_col=2
        else:
            paso_col=1

        for i in range(min(f1,f2),max(f1,f2)+1,paso_fila):
            for j in range(min(c1,c2),max(c1,c2)+1,paso_col):
                self.pon_bloq(i,j,elemento)
        self.refr()
        self.limp_prev_rect()

    def ini_mov(self,event):
        """Guarda dónde empezó el clic derecho."""
        self.ultimo_x,self.ultimo_y=event.x,event.y

    def mov_cam(self,event):
        """Mueve la cámara al arrastrar con clic derecho."""
        dx,dy=event.x-self.ultimo_x,event.y-self.ultimo_y
        self.ultimo_x,self.ultimo_y=event.x,event.y
        self.mov_vista(self.offset_x+dx,self.offset_y+dy)

    def rued_zoom(self,event):
        """Acerca o aleja con la rueda, hacia donde está el cursor."""
        if event.delta>0:
            paso=1
        else:
            paso=-1
        nuevo_nivel=max(1,min(self.max_zoom,self.niv_zoom+paso))
        if nuevo_nivel==self.niv_zoom:
            return
        factor=nuevo_nivel/self.niv_zoom
        self.niv_zoom=nuevo_nivel
        self.act_img_zoom()
        self.mov_vista(int(round(event.x-(event.x-self.offset_x)*factor)),
                          int(round(event.y-(event.y-self.offset_y)*factor)))


if __name__=="__main__":
    sandbox=Sandbox()
    sandbox.root.mainloop()