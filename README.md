# Bellos Clicks · Orçamento online

Página pública para o cliente pedir site, agendamento online ou sistema (valor só na proposta) e montar o orçamento de foto, vídeo, Reels e storymaker, enviando o pedido direto para a Isa.

- Hospedagem: Netlify, ligado a este repositório (cada envio para a branch `main` publica sozinho)
- Endereço: https://belloscliks.netlify.app/
- Modo teste: endereço + `#teste`
- Os pedidos são gravados no Supabase (função `bellos-pedido`, tabela `bellos_pedidos`). Um gatilho no banco (`bc_pedido_para_funil`) cria o lead no Funil do Portal (`bc_leads`, etapa Lead, origem "Orçamento online"). Pedidos de teste não entram no Funil.
- Sites e sistemas não mostram preço: aparecem como "Na proposta" e o pedido pede a conversa de 20 minutos.

## App instalável
- `manifest.webmanifest`, `icons/` e `sw.js` fazem a página abrir em tela cheia quando adicionada à tela inicial.
- Para atualizar a página: edite `tools/pagina.html` e rode `python3 tools/build.py`, que gera o `index.html`.
