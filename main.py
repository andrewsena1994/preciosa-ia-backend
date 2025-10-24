from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(title="Preciosa IA – API MVP")

# CORS p/ localhost do front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://preciosa-ia-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CaptionIn(BaseModel):
    categoria: str
    preco: str
    tamanhos: str
    tom: str

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/docs", include_in_schema=False)
def custom_docs():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Preciosa IA – API MVP",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )

@app.post("/caption/generate")
def caption_generate(payload: CaptionIn):
    base = f"{payload.categoria} disponível {payload.tamanhos} por R$ {payload.preco}. Pronta entrega!"
    variacoes = [
        f"{base} Garanta já no atacado 💎",
        f"{base} Qualidade que valoriza suas vendas 💗",
        f"{base} Estoque limitado — peça agora!",
        f"{base} Direto para seu catálogo no WhatsApp.",
        f"{base} Nova coleção Preciosa.",
    ]
    return {"variacoes": variacoes[:5]}
git add main.py
git commit -m "CORS: inclui domínio da Vercel"
git push
