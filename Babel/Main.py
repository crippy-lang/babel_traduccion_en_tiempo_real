import customtkinter as ctk

class Babel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Babel - Universal Listener v1.0")
        self.geometry("400x520")

        # --- DICCIONARIO DE INTERFAZ ---
        # Esto permite que la app se traduzca sola al instante
        self.textos_idiomas = {
            "Español": {"titulo": "TU IDIOMA DE PREFERENCIA", "boton": "INICIAR", "activo": "[ACTIVO]: Escuchando...", "off": "[OFF]: Traductor desactivado."},
            "Inglés": {"titulo": "YOUR PREFERRED LANGUAGE", "boton": "START", "activo": "[ACTIVE]: Listening...", "off": "[OFF]: Translator deactivated."},
            "Portugués": {"titulo": "SEU IDIOMA DE PREFERÊNCIA", "boton": "INICIAR", "activo": "[ATIVO]: Ouvindo...", "off": "[OFF]: Tradutor desativado."},
            "Francés": {"titulo": "VOTRE LANGUE PRÉFÉRÉE", "boton": "DÉMARRER", "activo": "[ACTIF]: Écoute...", "off": "[OFF]: Traducteur désactivé."},
            "Italiano": {"titulo": "LA TUA LINGUA PREFERITA", "boton": "INIZIA", "activo": "[ATTIVO]: Ascolto...", "off": "[OFF]: Traduttore disattivato."}
        }
        
        # --- PANEL PRINCIPAL ---
        self.label_main = ctk.CTkLabel(self, text=self.textos_idiomas["Español"]["titulo"], font=("Roboto", 16, "bold"))
        self.label_main.pack(pady=30)

        # SELECTOR DE IDIOMA DESTINO
        self.idioma_destino = ctk.CTkComboBox(self, values=list(self.textos_idiomas.keys()), 
                                             width=250, height=40, font=("Roboto", 14),
                                             command=self.actualizar_al_vuelo) 
        self.idioma_destino.set("Español")
        self.idioma_destino.pack(pady=10)

        # --- SECCIÓN INICIAR ---
        self.label_iniciar = ctk.CTkLabel(self, text=self.textos_idiomas["Español"]["boton"], font=("Roboto", 14, "bold"))
        self.label_iniciar.pack(pady=(30, 5))

        self.switch_var = ctk.StringVar(value="off")
        self.switch_escudo = ctk.CTkSwitch(self, text="", 
                                          command=self.toggle_escudo, variable=self.switch_var, 
                                          onvalue="on", offvalue="off", switch_width=80, switch_height=40)
        self.switch_escudo.pack(pady=10)

        # MONITOR DE ACTIVIDAD
        self.log = ctk.CTkTextbox(self, width=350, height=100, font=("Consolas", 12))
        self.log.pack(pady=20)
        self.actualizar_log("Sistema Babel listo.")

    def actualizar_log(self, mensaje):
        """Limpia el cuadro y pone solo el último registro"""
        self.log.delete("0.0", "end")
        self.log.insert("0.0", mensaje)

    def toggle_escudo(self):
        idioma = self.idioma_destino.get()
        textos = self.textos_idiomas[idioma]
        
        if self.switch_var.get() == "on":
            self.actualizar_log(textos["activo"])
        else:
            self.actualizar_log(textos["off"])

    def actualizar_al_vuelo(self, nuevo_idioma):
        """Traduce la interfaz y el log al instante según el idioma escogido"""
        textos = self.textos_idiomas[nuevo_idioma]
        
        # Actualizar etiquetas de la interfaz
        self.label_main.configure(text=textos["titulo"])
        self.label_iniciar.configure(text=textos["boton"])
        
        # Actualizar el log basado en el estado del switch
        if self.switch_var.get() == "on":
            self.actualizar_log(textos["activo"])
        else:
            self.actualizar_log(textos["off"])

if __name__ == "__main__":
    app = Babel()
    app.mainloop()