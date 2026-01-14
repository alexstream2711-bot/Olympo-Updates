import subprocess
import sys
import os
import hashlib

def instalar_dependencias():
    print("🚀 Instalando motores de O.L.Y.M.P.U.S...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def configurar_identidad():
    print("\n--- REGISTRO DE IDENTIDAD AEGIS ---")
    curp = input("Introduce tu CURP (Para registro legal de socio): ").strip().upper()
    token = input("Introduce tu Token de ngrok: ").strip()
    
    # Generar Hash Aegis (ID Pública)
    aegis_id = hashlib.sha256(curp.encode()).hexdigest()[:12].upper()
    
    # Guardar en archivo .env (oculto)
    with open(".env", "w") as f:
        f.write(f"CURP={curp}\n")
        f.write(f"NGROK_TOKEN={token}\n")
        f.write(f"AEGIS_ID={aegis_id}\n")
    
    print(f"\n✅ Configuración guardada. Tu ID de Socio es: {aegis_id}")
    print("Ahora puedes iniciar el nodo con: python main_nodo.py")

if __name__ == "__main__":
    instalar_dependencias()
    configurar_identidad()
