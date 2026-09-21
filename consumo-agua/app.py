# Solicitando o tipo de imóvel e convertendo para minúsculas para evitar erros de digitação
tipo_imovel = input('Informe o tipo de imóvel (comercial, casa ou apartamento): ').strip().lower()

# Solicitando o consumo de água em m³
try:
  consumo = float(
      input('Informe o consumo mensal de água em metros cúbicos (m³): ')
  )

  # Regras de negócio / Estrutura condicional
  if tipo_imovel == 'comercial':
    print('Tarifa comercial aplicada – consulte o plano corporativo.')
  elif tipo_imovel == 'apartamento' and consumo < 10:
    print('Consumo econômico – excelente controle de água!')
  elif tipo_imovel in ['apartamento', 'casa'] and consumo <= 25:
    print('Consumo moderado – dentro do padrão residencial.')
  else:
    print(
        'Consumo excessivo – adote medidas de economia e verifique vazamentos.'
    )

except ValueError:
  print('Por favor, informe um valor numérico válido para o consumo.')