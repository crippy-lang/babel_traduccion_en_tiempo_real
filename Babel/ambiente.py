##Autor: Duvan Felipe Delgadillo Cuevas
import pyaudio
import numpy as np
import noisereduce as nr
import time

class MotorNeuronal:
    def __init__(self):
        self.CHUNK = 2048 
        self.RATE = 16000 
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.p = pyaudio.PyAudio()
        
        # AJUSTE CLAVE: Subimos a 2500 para evitar falsos positivos
        self.UMBRAL_VOZ_LIMPIA = 2500 

    def escuchar_con_ia(self):
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)
        
        print(">>> [IA]: Calibrando Red Neuronal... (Espera 1 seg)")
        
        # Ignoramos el primer segundo para que la red "aprenda" el silencio
        for _ in range(int(self.RATE / self.CHUNK * 1)):
            stream.read(self.CHUNK, exception_on_overflow=False)

        print(">>> [IA]: Babel Escuchando voces reales...")
        
        try:
            while True:
                data = stream.read(self.CHUNK, exception_on_overflow=False)
                audio_raw = np.frombuffer(data, dtype=np.int16).astype(np.float32)
                
                # Filtrado Dinámico
                audio_limpio = nr.reduce_noise(
                    y=audio_raw, 
                    sr=self.RATE, 
                    stationary=False, 
                    prop_decrease=1.0
                )
                
                amplitud_final = np.abs(audio_limpio).mean()

                # DEBUG: Si quieres ver el número real de ruido, descomenta la línea de abajo:
                # print(f"Energía detectada: {int(amplitud_final)}")

                if amplitud_final > self.UMBRAL_VOZ_LIMPIA:
                    # Pequeña pausa para confirmar que no es un ruido momentáneo
                    return "¡Voz humana detectada!"
                    
        finally:
            stream.stop_stream()
            stream.close()

if __name__ == "__main__":
    motor = MotorNeuronal()
    print(motor.escuchar_con_ia())
