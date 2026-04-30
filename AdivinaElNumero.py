import tkinter as tk
from tkinter import ttk, messagebox
import random

class AdivinaNumeroProgresivo:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 Adivina el Número - Modo Calor 🔥")
        self.root.geometry("550x650")
        self.root.configure(bg="#0F172A")  # Fondo azul muy oscuro (Slate 900)
        
        self.secreto = random.randint(1, 100)
        self.intentos = 0
        
        # Configurar estilo de la barra de progreso
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Calor.Horizontal.TProgressbar", 
                       background="#F59E0B",  # Ámbar brillante
                       troughcolor="#1E293B",  # Fondo de la barra
                       bordercolor="#F59E0B",
                       lightcolor="#F59E0B",
                       darkcolor="#B45309",
                       thickness=25)
        
        # === TÍTULO PRINCIPAL ===
        self.titulo = tk.Label(root, 
                               text="🎲 ¿PUEDES ADIVINARLO? 🎲", 
                               font=("Helvetica", 20, "bold"), 
                               bg="#0F172A", 
                               fg="#FBBF24")  # Amarillo dorado
        self.titulo.pack(pady=25)
        
        # === SUBTÍTULO ===
        self.subtitulo = tk.Label(root, 
                                  text="La computadora ya eligió un número entre 1 y 100", 
                                  font=("Helvetica", 10), 
                                  bg="#0F172A", 
                                  fg="#94A3B8")  # Gris claro
        self.subtitulo.pack()
        
        # === ENTRADA DE NÚMERO ===
        self.entrada = tk.Entry(root, 
                                font=("Courier New", 36, "bold"), 
                                justify="center", 
                                bg="#1E293B",  # Fondo gris azulado
                                fg="#F8FAFC",  # Texto blanco
                                insertbackground="#FBBF24",  # Cursor dorado
                                relief="flat", 
                                bd=0,
                                highlightthickness=2,
                                highlightcolor="#F59E0B",
                                highlightbackground="#334155")
        self.entrada.pack(pady=30, padx=50, ipady=15)
        self.entrada.bind("<Return>", self.adivinar)
        
        # === BOTÓN PRINCIPAL ===
        self.boton = tk.Button(root, 
                               text="🔍 COMPROBAR NÚMERO 🔍", 
                               command=self.adivinar,
                               font=("Helvetica", 13, "bold"),
                               bg="#EF4444",  # Rojo vibrante
                               fg="white",
                               activebackground="#DC2626",  # Rojo más oscuro al click
                               activeforeground="white",
                               cursor="hand2",
                               relief="flat", 
                               bd=0, 
                               padx=25, 
                               pady=12)
        self.boton.pack(pady=10)
        
        # === BARRA DE CALOR (CERCANÍA) ===
        self.barra_label = tk.Label(root, 
                                    text="🌡️ CERCANÍA AL NÚMERO SECRETO 🌡️", 
                                    font=("Helvetica", 11, "bold"), 
                                    bg="#0F172A", 
                                    fg="#A78BFA")  # Púrpura suave
        self.barra_label.pack(pady=(25, 5))
        
        self.barra = ttk.Progressbar(root, 
                                     length=400, 
                                     mode='determinate', 
                                     style="Calor.Horizontal.TProgressbar")
        self.barra.pack(pady=10)
        
        # === ETIQUETA DE PORCENTAJE DE CERCANÍA ===
        self.porcentaje_label = tk.Label(root, 
                                         text="0%", 
                                         font=("Helvetica", 14, "bold"), 
                                         bg="#0F172A", 
                                         fg="#F59E0B")
        self.porcentaje_label.pack()
        
        # === MENSAJE DE PISTA ===
        self.pista = tk.Label(root, 
                              text="💡 Escribe un número y presiona ENTER", 
                              font=("Helvetica", 12), 
                              bg="#0F172A", 
                              fg="#34D399",  # Verde menta
                              wraplength=450,
                              justify="center")
        self.pista.pack(pady=25)
        
        # === CONTADOR DE INTENTOS ===
        self.intentos_label = tk.Label(root, 
                                       text=f"📊 INTENTOS REALIZADOS: {self.intentos}", 
                                       font=("Helvetica", 12, "bold"), 
                                       bg="#0F172A", 
                                       fg="#60A5FA")  # Azul cielo
        self.intentos_label.pack(pady=5)
        
        # === BOTÓN DE REINICIO ===
        self.reinicio_boton = tk.Button(root, 
                                        text="🔄 NUEVO JUEGO 🔄", 
                                        command=self.reiniciar,
                                        font=("Helvetica", 10, "bold"),
                                        bg="#3B82F6",  # Azul brillante
                                        fg="white",
                                        activebackground="#2563EB",
                                        cursor="hand2",
                                        relief="flat",
                                        padx=15,
                                        pady=8)
        self.reinicio_boton.pack(pady=10)
        
        # Enfocar entrada automáticamente
        self.entrada.focus()
    
    def adivinar(self, event=None):
        try:
            guess = int(self.entrada.get())
            
            # Validar rango
            if guess < 1 or guess > 100:
                self.pista.config(text="⚠️ ¡NÚMERO FUERA DE RANGO! (1-100) ⚠️", 
                                 fg="#F87171")  # Rojo claro
                self.entrada.delete(0, tk.END)
                return
            
            self.intentos += 1
            self.intentos_label.config(text=f"📊 INTENTOS REALIZADOS: {self.intentos}")
            
            # Calcular cercanía
            diferencia = abs(guess - self.secreto)
            cercania = max(0, 100 - (diferencia / 50) * 100)
            self.barra['value'] = cercania
            self.porcentaje_label.config(text=f"{int(cercania)}%")
            
            # Cambiar color de la barra según cercanía
            style = ttk.Style()
            if cercania < 30:
                style.configure("Calor.Horizontal.TProgressbar", background="#EF4444")  # Rojo (frío)
            elif cercania < 70:
                style.configure("Calor.Horizontal.TProgressbar", background="#F59E0B")  # Ámbar (tibio)
            else:
                style.configure("Calor.Horizontal.TProgressbar", background="#10B981")  # Verde (caliente)
            
            # Dar pistas
            if guess < self.secreto:
                self.pista.config(text=f"📈 ¡DEMASIADO BAJO! El número {guess} es menor al secreto\n💡 Prueba con un número más GRANDE", 
                                 fg="#FBBF24")  # Amarillo
                self.root.configure(bg="#0F172A")
            elif guess > self.secreto:
                self.pista.config(text=f"📉 ¡DEMASIADO ALTO! El número {guess} es mayor al secreto\n💡 Prueba con un número más PEQUEÑO", 
                                 fg="#F87171")  # Rojo claro
                self.root.configure(bg="#0F172A")
            else:
                # Mensaje de victoria personalizado según intentos
                if self.intentos <= 5:
                    mensaje = f"🏆 ¡INCREÍBLE! 🏆\n¡Adivinaste en solo {self.intentos} intentos!\n¡Eres un genio!"
                elif self.intentos <= 10:
                    mensaje = f"🎉 ¡FELICIDADES! 🎉\nAdivinaste en {self.intentos} intentos.\n¡Buen trabajo!"
                else:
                    mensaje = f"🎯 ¡LO LOGRASTE! 🎯\nAdivinaste en {self.intentos} intentos.\n¡Sigue practicando!"
                
                messagebox.showinfo("🎉 ¡VICTORIA! 🎉", 
                                   f"{mensaje}\n\nEl número secreto era {self.secreto}")
                self.reiniciar()
            
            self.entrada.delete(0, tk.END)
            self.entrada.focus()
            
        except ValueError:
            self.pista.config(text="❌ ¡ESO NO ES UN NÚMERO VÁLIDO! ❌\nPor favor, ingresa solo números enteros", 
                             fg="#F87171")
            self.entrada.delete(0, tk.END)
    
    def reiniciar(self):
        self.secreto = random.randint(1, 100)
        self.intentos = 0
        self.barra['value'] = 0
        self.porcentaje_label.config(text="0%")
        self.intentos_label.config(text=f"📊 INTENTOS REALIZADOS: {self.intentos}")
        self.pista.config(text="🎲 ¡NUEVO JUEGO! 🎲\nLa computadora eligió otro número secreto.\n¡Adivínalo!", 
                         fg="#34D399")
        self.entrada.delete(0, tk.END)
        self.entrada.focus()
        
        # Resetear color de la barra
        style = ttk.Style()
        style.configure("Calor.Horizontal.TProgressbar", background="#F59E0B")

if __name__ == "__main__":
    root = tk.Tk()
    juego = AdivinaNumeroProgresivo(root)
    root.mainloop()
