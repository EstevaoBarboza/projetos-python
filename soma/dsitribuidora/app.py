import json


faturamento_mensal = '''
{
    "faturamento": [200, 500, 0, 300, 800, 0, 600, 100, 0, 900]
}
'''

dados = json.loads(faturamento_mensal)
faturamentos = [f for f in dados['faturamento'] if f > 0]  


menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_faturamento = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = len([f for f in faturamentos if f > media_faturamento])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
