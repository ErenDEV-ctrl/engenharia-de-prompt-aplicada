# Simulação acadêmica de um radar de velocidade
# Projeto: Engenharia de Prompt Aplicada

# Define o limite de velocidade da via
LIMITE_VIA = 80

# Define a tolerância utilizada no exemplo acadêmico
TOLERANCIA = 0.10

# Calcula o limite considerando 10% de tolerância
limite_com_tolerancia = LIMITE_VIA * (1 + TOLERANCIA)

print("=== Simulação de Radar de Velocidade ===")
print(f"Limite da via: {LIMITE_VIA} km/h")
print(f"Limite considerado com tolerância: {limite_com_tolerancia:.0f} km/h")

# Solicita ao usuário a velocidade registrada
velocidade_veiculo = float(
    input("\nDigite a velocidade registrada do veículo em km/h: ")
)

# Estrutura condicional IF/ELSE
if velocidade_veiculo > limite_com_tolerancia:
    print("\n⚠️ Veículo acima do limite considerado no exemplo.")
else:
    print("\n✅ Velocidade dentro do limite considerado no exemplo.")
