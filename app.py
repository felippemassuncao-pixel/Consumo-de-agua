tipo = input("Qual seu estilo de localidade entre: casa, apartamento ou comercio?.")
if tipo == "casa" or tipo == "apartamento":
  custo = int(input("Quanto você gasta de água em m3?."))
if (tipo == "casa" or tipo =="apartamento") and custo < 10:
  print("Consumo econômico - exelente controle de água.")
elif (tipo == "casa" or tipo =="apartamento") and 10 <= custo <= 25:
  print("Consumo moderado - dentro do padrão residencial.")
elif tipo == "comercial":
  print("Comercial aplicada - procure o plano corporativo.")
else:
  print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")