numInt=5
numFloat=2.5
valString="IFSP"
valorFinal=0

valorFinal=numInt/numFloat
print("O valor apresentado é:", valorFinal)

#comando format

faturamento=1000
custo=500

print("o faturamento da empresa foi= {} e o custo foi de {}".format(faturamento, custo))

#comando f string

faturamento=10000
custo=5000

lucro=faturamento-custo

print(f"o lucro doi de R$ {lucro}")

margem=lucro/faturamento
print(f"a margem foi de {margem}")

#comando .nf

faturamento=7000
custo=2500

lucro=faturamento-custo
print(f"o lucro foi de {lucro:,.2f}")

margem= lucro/faturamento
print(f"a  margem foi de {margem:.2%}")
