from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox, Tk, PhotoImage

operador = ''
precios_sopa = [1.25, 2.34, 3.43, 2.78, 2.30, 3.00, 1.78, 1.95, 1.24]
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 2.65, 3.56, 2.56, 3.45]
precios_ensaladas = [0.95, 1.50, 1.85, 2.34, 1.37, 0.80, 1.48, 1.27, 1.65]
precios_bebida = [0.25, 0.99, 1.21, 1.08, 1.10, 2.00, 1.58, 2.76, 1.18]
precios_postres = [1.54, 1.68, 1.32, 2.55, 2.14, 1.74, 3.25, 4.25, 2,70]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)
    
    
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)   
    

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    
    x = 0
    
    for c in cuadros_sopa:
        if variables_sopa[x].get() == 1:
            cuadros_sopa[x].config(state=NORMAL)
            
            if cuadros_sopa[x].get() == '0':
                cuadros_sopa[x].delete(0, END)
            
            cuadros_sopa[x].delete(0,END)
            cuadros_sopa[x].focus()
            
        else:
            cuadros_sopa[x].config(state=DISABLED)
            texto_sopa[x].set('0')
            
        x += 1
        
        
    x = 0
    
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            
            cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
            
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
            
        x += 1
     
        
    x = 0
    
    for c in cuadros_ensalada:
        if variables_ensalada[x].get() == 1:
            cuadros_ensalada[x].config(state=NORMAL)
            
            if cuadros_ensalada[x].get() == '0':
                cuadros_ensalada[x].delete(0, END)
            
            cuadros_ensalada[x].delete(0,END)
            cuadros_ensalada[x].focus()
            
        else:
            cuadros_ensalada[x].config(state=DISABLED)
            texto_ensalada[x].set('0')
            
        x += 1
               
    x = 0
    
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
                
            cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
            
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
            
        x += 1
     
     
    x = 0
    
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
                
            cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
            
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
            
        x += 1


def total():
    
    sub_total_sopa = 0
    p = 0
    for cantidad in texto_sopa:
        sub_total_sopa = sub_total_sopa + (float(cantidad.get()) * precios_sopa[p])
        p += 1
        
        
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    
    
    sub_total_ensalada = 0
    p = 0
    for cantidad in texto_ensalada:
        sub_total_ensalada = sub_total_ensalada + (float(cantidad.get()) * precios_ensaladas[p])
        p += 1
 
    
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    
    
    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
        
    
    sub_total = sub_total_sopa + sub_total_comida + sub_total_ensalada + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos
    
    var_costo_sopa.set(f'$ {round(sub_total_sopa, 2)}')
    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_ensalada.set(f'$ {round(sub_total_ensalada, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}')
    texto_recibo.insert(END, f'*' * 60 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 66 + '\n')
    
    x = 0
    for sopa in texto_sopa:
        if sopa.get() != '0':
            texto_recibo.insert(END, f'{lista_sopa[x]}\t\t{sopa.get()}\t$ {int(sopa.get()) * precios_sopa[x]}\n')
            
        x += 1
       
        
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')
            
        x += 1
    
    
    x = 0
    for ensalada in texto_ensalada:
        if ensalada.get() != '0':
            texto_recibo.insert(END, f'{lista_ensaladas[x]}\t\t{comida.get()}\t$ {int(ensalada.get()) * precios_ensaladas[x]}\n')
            
        x += 1
       
       
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
            
        x += 1
      
        
    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t$ {int(postres.get()) * precios_postres[x]}\n')
            
        x += 1
        
    
    texto_recibo.insert(END, f'-' * 60 + '\n')
    texto_recibo.insert(END, f' Costo de la Sopa: \t\t\t{var_costo_sopa.get()}\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Ensalada: \t\t\t{var_costo_ensalada.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    
    texto_recibo.insert(END, f'-' * 60 + '\n')
    texto_recibo.insert(END, f' Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    
    texto_recibo.insert(END, f'-' * 60 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


def guardar():
    
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode = 'w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','Su recibo ha sido guardado')
    

def resetear():
    
    texto_recibo.delete(0.1, END)
    
    for texto in texto_sopa:
        texto.set('0')
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_ensalada:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')       
    for texto in texto_postres:
        texto.set('0')
        
    for cuadro in cuadros_sopa:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_ensalada:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)   
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)      
        
    for v in variables_sopa:
        v.set(0)
    for v in variables_comida:
        v.set(0)
    for v in variables_ensalada:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)
        
    var_costo_sopa.set('')
    var_costo_comida.set('')
    var_costo_ensalada.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')
   
#iniciar tkinter
aplicacion = Tk()

# tamano de la ventana
aplicacion.geometry('1740x600+0+0')

#evitar maximizar
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# color de fundo de la ventana
aplicacion.config(bg = 'LightPink') 

#aplicacion.config(bg_image)
#panel superior
panel_superior = Frame(aplicacion, bd = 1, relief =SUNKEN)
#flat, raised, sunken, groove, ridge
panel_superior.pack(side = TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text = 'Sistema de Facturacion', fg = 'LightPink', font=('Lexend', 62),bg = 'azure4',width=20)
etiqueta_titulo.grid(row = 0, column =0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd = 1, relief=SUNKEN)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=SUNKEN, bg = 'azure4',padx=40)
panel_costos.pack(side=BOTTOM)

#panel sopa
panel_sopa = LabelFrame(panel_izquierdo, text='Sopa', font=('Dosis', 10,'bold'), bd = 1, relief=SUNKEN, fg='azure4')
panel_sopa.pack(side=LEFT)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 10,'bold'), bd = 1, relief=SUNKEN, fg='azure4')
panel_comidas.pack(side=LEFT)

#panel ensaladas
panel_ensaladas = LabelFrame(panel_izquierdo, text='Ensalada', font=('Dosis', 10,'bold'), bd = 1, relief=SUNKEN, fg='azure4')
panel_ensaladas.pack(side=LEFT)

#panel bebidas
panel_bebidas= LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 10,'bold'), bd = 1, relief=SUNKEN, fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres= LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 10,'bold'), bd = 1, relief=SUNKEN, fg='azure4')
panel_postres.pack(side=LEFT)

#panel derecha 
panel_derecha = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_derecha.pack(side=LEFT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd = 1, relief=SUNKEN, bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd = 1, relief=SUNKEN, bg='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd = 1, relief=SUNKEN, bg='burlywood')
panel_botones.pack()

#lista de productos
lista_sopa = ['gazpacho', 'caldo verde','harira','ezogelin', 'menudo','yayla','kharcho', 'borş','bouillabaisse']
lista_comidas = ['pollo','coredero', 'salmon', 'merluza', 'kebab', 'pizza','paella','empanadas','tortilla']
lista_ensaladas = ['tropikal', 'azifa','solterito','panzanella','sezar','zaaluk','salpicao','snezhanka','çoban']
lista_bebidas = ['agua', 'soda','jugo','cola','vino','cerveza','sangría','queimada','kalimotxo']
lista_postres = ['helado','fruta', 'brownies','flan','mousse','pastel','baklava','churros','torrija']

#generar items sopa
variables_sopa = []
cuadros_sopa = []
texto_sopa = []
contador = 0
for sopa in lista_sopa:
    
    #crear checkbutton
    variables_sopa.append('')
    variables_sopa[contador] = IntVar()
    sopa = Checkbutton(panel_sopa, 
                         text=sopa.title(),
                         font=('Lexend',19,'bold'), 
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_sopa[contador],
                         command = revisar_check)
    
    sopa.grid(row=contador, 
                column = 0, 
                sticky=W)
    
    #crear los cuadros de entrada
    cuadros_sopa.append('')
    texto_sopa.append('')
    texto_sopa[contador] = StringVar()
    texto_sopa[contador].set('0')
    
    cuadros_sopa[contador] = Entry(panel_sopa,
                                     font=('Lexend',8, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_sopa[contador])
    
    
    cuadros_sopa[contador].grid(row=contador,
                                  column=1)
    
    contador += 1


#generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    
    #crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(),
                         font=('Lexend',19,'bold'), 
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_comida[contador],
                         command = revisar_check)
    
    
    comida.grid(row=contador, 
                column = 0, 
                sticky=W)
    
    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Lexend',8, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    
    
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    
    contador += 1

#generar items ensalada
variables_ensalada = []
cuadros_ensalada = []
texto_ensalada = []
contador = 0
for ensalada in lista_ensaladas:
    
    #crear checkbutton
    variables_ensalada.append('')
    variables_ensalada[contador] = IntVar()
    ensalada = Checkbutton(panel_ensaladas, 
                         text=ensalada.title(),
                         font=('Lexend',19,'bold'), 
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_ensalada[contador],
                         command = revisar_check)
    
    ensalada.grid(row=contador, 
                column = 0, 
                sticky=W)
    
    #crear los cuadros de entrada
    cuadros_ensalada.append('')
    texto_ensalada.append('')
    texto_ensalada[contador] = StringVar()
    texto_ensalada[contador].set('0')
    
    cuadros_ensalada[contador] = Entry(panel_ensaladas,
                                     font=('Lexend',8, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_ensalada[contador])
    
    
    cuadros_ensalada[contador].grid(row=contador,
                                  column=1)
    
    contador += 1

#generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    
    #crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    
    bebida = Checkbutton(panel_bebidas, 
                         text=bebida.title(),
                         font=('Lexend',19,'bold'), 
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_bebida[contador],
                         command = revisar_check)
    
    
    bebida.grid(row=contador, 
                column = 0, 
                sticky=W)
    
    #crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Lexend',8, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    
    contador += 1

#yemekkkkkkkk 
#generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    
    #crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    
    postres = Checkbutton(panel_postres, 
                          text=postres.title(),
                          font=('Lexend',19,'bold'), 
                          onvalue=1, offvalue=0, 
                          variable=variables_postres[contador],
                          command = revisar_check)
    
    postres.grid(row=contador, 
                 column = 0, 
                 sticky=W)
    
    
    #crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=('Lexend',8, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    
    
    cuadros_postres[contador].grid(row=contador,
                                  column=1)
        
    contador += 1


#variables
var_costo_sopa = StringVar()
var_costo_comida = StringVar()
var_costo_ensalada = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

#etiquetas de costo y campos de entrada

#etiqueta costo sopa
etiqueta_costo_sopa = Label(panel_costos,
                              text='Costo Sopa    ',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_sopa.grid(row=0,column=0)

texto_costo_sopa = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_sopa)

texto_costo_sopa.grid(row=0,column=1,padx=41)

#etiqueta costo comida
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_comida.grid(row=1,column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=1,column=1,padx=41)

#etiqueta costo ensalada
etiqueta_costo_ensalada = Label(panel_costos,
                              text='Costo Ensalada',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_ensalada.grid(row=0,column=2)

texto_costo_ensalada = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_ensalada)

texto_costo_ensalada.grid(row=0,column=3,padx=41)

#etiqueta costo bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida ',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_bebida.grid(row=1,column=2)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1,column=3,padx=41)

#etiqueta costo postres
etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Postres',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_costo_postres.grid(row=0,column=4)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_costo_postres)

texto_costo_postres.grid(row=0,column=5,padx=41)

#etiqueta subtotal
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal       ',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_subtotal.grid(row=1,column=4)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_subtotal)

texto_subtotal.grid(row=1,column=5,padx=41)

#etiqueta impuestos
etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_impuestos.grid(row=0,column=6)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_impuestos)

texto_impuestos.grid(row=0,column=7,padx=41)

#etiqueta total
etiqueta_total = Label(panel_costos,
                              text='Total        ',
                              font=('Dosis',10, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_total.grid(row=1,column=6)

texto_total = Entry(panel_costos,
                           font=('Dosis',10,'bold'),
                           bd=1,
                           width=12,
                           state='readonly',
                           textvariable=var_total)

texto_total.grid(row=1,column=7,padx=41)


#botones
botones = ['total', 'recibo','guardar','resetear']
botones_creados = []

columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text= boton.title(),
                   font=('Dosis', 10, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd =1,
                   width=9)
                             
    botones_creados.append(boton)          
                   
    boton.grid(row = 0,
               column = columnas)
    columnas += 1

botones_creados[0].config(command = total)
botones_creados[1].config(command = recibo)
botones_creados[2].config(command = guardar)
botones_creados[3].config(command = resetear)

#area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd = 1,
                    width=42,
                    height=10)

texto_recibo.grid(row=0, column=0)

#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 15, 'bold'),
                          width=32,
                          bd=1)

visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora =['7','8','9','+','4','5','6','-',
                      '1','2','3','X','R','B','0','/']

botones_guardados = []


fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg='white',
                   bg ='azure4',
                   bd =1,
                   width=8)
    
    botones_guardados.append(boton)
    
    boton.grid(row=fila,column=columna)
    if columna == 3:
        fila += 1
        
    columna += 1
    
    if columna == 4:
        columna = 0
        
botones_guardados[0].config(command = lambda : click_boton('7'))
botones_guardados[1].config(command = lambda : click_boton('8'))
botones_guardados[2].config(command = lambda : click_boton('9'))
botones_guardados[3].config(command = lambda : click_boton('+'))
botones_guardados[4].config(command = lambda : click_boton('4'))
botones_guardados[5].config(command = lambda : click_boton('5'))
botones_guardados[6].config(command = lambda : click_boton('6'))
botones_guardados[7].config(command = lambda : click_boton('-'))
botones_guardados[8].config(command = lambda : click_boton('1'))
botones_guardados[9].config(command = lambda : click_boton('2'))
botones_guardados[10].config(command = lambda : click_boton('3'))
botones_guardados[11].config(command = lambda : click_boton('*'))
botones_guardados[12].config(command = obtener_resultado)
botones_guardados[13].config(command = borrar)
botones_guardados[14].config(command = lambda : click_boton('0'))
botones_guardados[15].config(command = lambda : click_boton('/'))

#evitar que la pantalla se cierrre
aplicacion.mainloop()

