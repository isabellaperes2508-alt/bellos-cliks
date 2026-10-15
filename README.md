# Bellos Cliks · Orçamento online

Página pública para o cliente montar o orçamento de foto, vídeo, Reels, storymaker e sites e enviar o pedido direto para a Isa.

- Hospedagem: Netlify, ligado a este repositório (cada envio para a branch `main` publica sozinho)
- Endereço: https://belloscliks.netlify.app/
- Modo teste: endereço + `#teste`
- Os pedidos são gravados no Supabase (função `bellos-pedido`) e aparecem no painel privado da Isa no Claude.

## App instalável
- `manifest.webmanifest`, `icons/` e `sw.js` fazem a página abrir em tela cheia quando adicionada à tela inicial.
- Para atualizar a página: edite `tools/pagina.html` e rode `python3 tools/build.py`, que gera o `index.html`.
