from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Preciosa IA – API MVP")

# CORS p/ localhost do front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
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
