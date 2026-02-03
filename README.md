# 🧮 Calculadora PASSE-UFMS

Script em Python desenvolvido para auxiliar estudantes no cálculo da média final do **PASSE (Programa de Avaliação Seriada Seletiva)** da UFMS.

## ⚠️ Aviso Importante
Este projeto é uma ferramenta de apoio **não oficial**. 
* **Valor Aproximado:** Os cálculos realizados por este script fornecem uma **estimativa** baseada nas fórmulas do edital.
* **Não é 100% exato:** O resultado final pode variar ligeiramente devido a critérios específicos de arredondamento ou padronização da banca examinadora.
* **Uso Informativo:** Use esta calculadora apenas para planejamento pessoal. O resultado oficial é o publicado exclusivamente pela **UFMS**.

---

## 🚀 Como funciona
A calculadora processa os dados seguindo a regra de média ponderada das Notas de Competência (NC):
1. **Pesos:** Você define os pesos específicos do curso (conforme o Anexo II do edital).
2. **Escores Padronizados (EP):** Insere-se o EP das três etapas para cada área (Humanas, Natureza, Linguagens e Matemática).
3. **Redação:** Informa-se a nota da redação obtida na Etapa 3.

A fórmula utilizada para cada competência é:  
`NC = (0.2 * EP1) + (0.3 * EP2) + (0.5 * EP3)`

---

## 📋 Requisitos

Para correr este script, precisa de ter instalado no seu computador:
* **Python 3.6** ou superior.
---

## 🛠️ Como Clonar e Executar

1. **Clone o repositório:**
   Abra o terminal e digite:
   ```bash
   git clone [https://github.com/JhonnPA/Calculadora-PASSE.git](https://github.com/JhonnPA/Calculadora-PASSE.git)

2. **Entre na pasta do projeto:**
   ```bash
   cd Calculadora-PASSE

3. **Execute o script:**
   ```bash
   python CALC_PASSE_UFMS.py
