"""Gera index.html a partir do conteúdo da página (pagina.html) com o cabeçalho de app instalável."""
import re, sys, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
body = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8') if len(sys.argv) > 1 else (raiz / 'tools' / 'pagina.html').read_text(encoding='utf-8')
head = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Monte seu orçamento de foto, vídeo, Reels, storymaker e sites com a Bellos Cliks e veja o valor na hora.">
<meta property="og:title" content="Orçamento Bellos Cliks">
<meta property="og:description" content="Foto, vídeo, Reels, storymaker e sites. Monte seu orçamento em 2 minutos e veja o valor na hora.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://belloscliks.netlify.app/">
<meta property="og:image" content="https://belloscliks.netlify.app/assets/og-bellos-clicks.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://belloscliks.netlify.app/">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#5E3A84">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Bellos Cliks">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="/icons/favicon-64.png">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
'''
title = re.search(r'<title>.*?</title>', body).group(0)
body = body.replace(title, '', 1).replace('<meta name="claude:viewport-fit-sides" content="cover">', '', 1)
(raiz / 'index.html').write_text(head + title + '\n</head>\n<body>\n' + body.strip() + '\n</body>\n</html>\n', encoding='utf-8')
print('index.html gerado')
