# MAIÚSCULO (.upper) 
# MINÚSCULO (.lower)


def tratarTexto(texto):
  texto = texto.upper() # transforma tetras minúsculas em maiúsculas (.upper)
  texto = texto.strip() # retira o espaço entra a strig e as aspas (.strip)

  return texto

t = 'abc1234'
texto_t = tratarTexto(t)
print(texto_t) 