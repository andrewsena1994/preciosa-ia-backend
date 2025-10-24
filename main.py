from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from pydantic import BaseModel

app = FastAPI(title="Preciosa IA – API MVP")

# --- CORS (ajuste o domínio da Vercel aqui) ---
app.add_middleware
    CORSMiddleware,
   
ALLOWED_ORIGINS = [
    "https://precoisa-ia-frontend.vercel.app",  # seu domínio Vercel
    "http://localhost:3000",                    # dev local (opcional)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- Healthcheck ---
@app.get("/health")
def health():
    return {"status": "ok"}

# --- (Opcional) Stub de geração para o front funcionar já em produção ---
class CaptionIn(BaseModel):
    categoria: str
    preco: str
    tamanhos: str
    tom: str = "amigavel"

@app.post("/caption/generate")
def caption_generate(inp: CaptionIn):
    base = f"{inp.categoria} disponível! {inp.tamanhos} por R$ {inp.preco}."
    variacoes = [
        base + " Peça já o seu 💖",
        base + " Últimas unidades!",
        base + " Frete rápido 🚚",
        base + " Qualidade premium ✨",
        base + " Garanta hoje!",
    ]
    return {"variacoes": variacoes}

# --- Docs customizados (PINNED CDN URLs) ---
@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Preciosa IA – API MVP",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )

# --- Redoc como alternativa ---
@app.get("/redoc", include_in_schema=False)
def custom_redoc():
    return get_redoc_html(openapi_url=app.openapi_url, title="Preciosa IA – API Docs")
