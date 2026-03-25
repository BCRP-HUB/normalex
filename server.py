"""
NormaLex - Servidor local
Ejecutar: python server.py
"""
import http.server, socketserver, webbrowser, os, sys

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists(os.path.join("data", "instrumentos.json")):
    print("Generando datos...")
    os.system(f"{sys.executable} generate_data.py")

Handler = http.server.SimpleHTTPRequestHandler
print(f"\n  NormaLex — Inteligencia Regulatoria")
print(f"  http://localhost:{PORT}")
print(f"  Ctrl+C para detener\n")
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
